#!/usr/bin/env python3
"""Converts a .py file to a V.4 .ipynb notebook

Modified from http://stackoverflow.com/questions/23292242/converting-to-not-from-ipython-notebook-format
"""

import argparse
import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook
from nbformat import v3, v4
import codecs
from os import linesep


CELLMARKS = {"pycharm": "##",
             "spyder": "#%%"}


def parsePy(py_filename, cellmark_style, other_ignores=[]):
    """Converts a .py file to a V.4 .ipynb notebook using special cell markers.

    :param py_filename: .py filename
    :param cellmark_style: Determines cell marker based on IDE, {"pycharm": "##", "spyder": "#%%"}
    :param other_ignores: Other lines to ignore
    :return: A string containing one or more lines
    """
    codecell_ignores = list(CELLMARKS.values()) + list(other_ignores)
    nocodecell_ignores = ['"""', "'''"] + list(CELLMARKS.values()) + list(other_ignores)

    with open(py_filename, "r") as f:
        lines = []
        codecell = True
        metadata = {"slideshow": {"slide_type": "slide"}}
        for l in f:
            l1 = l.strip()

            if lines and ( l1.startswith(CELLMARKS[cellmark_style]) ):
                tmp=l1[len(CELLMARKS[cellmark_style]):].strip()
                yield (codecell, metadata, "".join(lines).strip(linesep))
                if (len(tmp)>0):
                    # append header
                    metadata = {"slideshow": {"slide_type": "slide"}}
                    yield (False, metadata, '# %s' % tmp)
                lines = []
                codecell = True
                metadata = {"slideshow": {"slide_type": "slide"}}
                continue
            
            if lines and ((l1.startswith('# In[') and l1.endswith(']:')) or l1 == CELLMARKS[cellmark_style]):
                yield (codecell, metadata, "".join(lines).strip(linesep))
                lines = []
                codecell = True
                metadata = {"slideshow": {"slide_type": "slide"}}
                continue

            if l1 in ("#md", "# md", "#markdown", "# markdown"):
                codecell = False
                continue

            if l1.startswith("#slide:") or l1.startswith("# slide:"):
                slidetype = l1.split(":")[-1].strip()
                slidetype = slidetype.strip(linesep)
                metadata["slideshow"]["slide_type"] = slidetype
                continue

            if "%matplotlib" in l1:
                l = l.strip()[1:].strip()

            if (codecell and l1 not in codecell_ignores) or (not codecell and l1 not in nocodecell_ignores):
                lines.append(l)

        if lines:
            yield (codecell, metadata, "".join(lines).strip(linesep))


def py2ipynb(input, output, cellmark_style, other_ignores=[]):
    """Converts a .py file to a V.4 .ipynb notebook usiing `parsePy` function

    :param input: Input .py filename
    :param output: Output .ipynb filename
    :param cellmark_style: Determines cell marker based on IDE, see parsePy documentation for values
    :param other_ignores: Other lines to ignore
    """
    # Create the code cells by parsing the file in input
    cells = []
    for c in parsePy(input, cellmark_style, other_ignores):
        codecell, metadata, code = c
        cell = new_code_cell(source=code, metadata=metadata) if codecell else new_markdown_cell(source=code, metadata=metadata)
        cells.append(cell)

    # This creates a V4 Notebook with the code cells extracted above
    nb0 = new_notebook(cells=cells,
                       metadata={'language': 'python',})

    with codecs.open(output, encoding='utf-8', mode='w') as f:
        nbformat.write(nb0, f, 4)


def py2ipynb_default(input, output):
    with open(input) as f:
        code = f.read()
    code += """
# <markdowncell>

# If you can read this, reads_py() is no longer broken!
"""

    nbook = v3.reads_py(code)
    nbook = v4.upgrade(nbook)  # Upgrade v3 to v4
    jsonform = v4.writes(nbook) + "\n"

    with open(output, "w") as f:
        f.write(jsonform)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input python file")
    parser.add_argument("output", help="output notebook file")
    cellmark_style_arg = parser.add_argument("-c", "--cellmark-style", default="default",
                        help="default|pycharm|spyder")
    args = parser.parse_args()

    cellmark_style_options = ("default", "pycharm", "spyder")
    if args.cellmark_style not in cellmark_style_options:
        raise argparse.ArgumentError(cellmark_style_arg,
                                     "invalid value, can only be one of "+ str(cellmark_style_options))

    if args.cellmark_style == "default":
        py2ipynb_default(args.input, args.output)
    else:
        py2ipynb(args.input, args.output, args.cellmark_style,
                 ["# ----------------------------------------------------------------------------"])

