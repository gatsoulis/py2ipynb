#!/usr/bin/env python
"""Converts a .py file to a V.4 .ipynb notebook

Modified from http://stackoverflow.com/questions/23292242/converting-to-not-from-ipython-notebook-format
"""

import argparse
import nbformat
from nbformat.v4 import new_code_cell,new_markdown_cell,new_notebook
import codecs
from os import linesep


CELLMARKS = {"pycharm": "##",
             "spyder": "#%%"}


def parsePy(py_filename, cellmode, other_ignores=[]):
    """Converts a .py file to a V.4 .ipynb notebook using special cell markers.

    :param py_filename: .py filename
    :param cellmode: Determines cell marker based on IDE, {"pycharm": "##", "spyder": "#%%"}
    :param other_ignores: Other lines to ignore
    :return: A string containing one or more lines
    """
    # ignores = ['"""', "'''"] + [v for k, v in CELLMARKS.items() if k != cellmode] + other_ignores
    ignores = ['"""', "'''"] + CELLMARKS.values() + other_ignores
    with open(py_filename, "r") as f:
        lines = []
        codecell = True
        for l in f:
            l1 = l.strip()
            if lines and ((l1.startswith('# In[') and l1.endswith(']:')) or l1 == CELLMARKS[cellmode]):
                yield (codecell, "".join(lines).strip(linesep))
                lines = []
                codecell = True
                continue

            if l1 in ("#md", "# md", "#markdown", "# markdown"):
                codecell = False
                continue

            if l1 not in ignores:
                lines.append(l)

        if lines:
            yield (codecell, "".join(lines).strip(linesep))

def py2ipynb(input, output, cellmode, other_ignores=[]):
    """Converts a .py file to a V.4 .ipynb notebook usiing `parsePy` function

    :param input: Input .py filename
    :param output: Output .ipynb filename
    :param cellmode: Determines cell marker based on IDE, see parsePy documentation for values
    :param other_ignores: Other lines to ignore
    """
    # Create the code cells by parsing the file in input
    cells = []
    for c in parsePy(input, cellmode, other_ignores):
        codecell, code = c
        cells.append(new_code_cell(source=code) if codecell else new_markdown_cell(source=code))

    # This creates a V4 Notebook with the code cells extracted above
    nb0 = new_notebook(cells=cells,
                       metadata={'language': 'python',})

    with codecs.open(output, encoding='utf-8', mode='w') as f:
        nbformat.write(nb0, f, 4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="input python file")
    parser.add_argument("-o", "--output", required=True, help="output notebook file")
    parser.add_argument("-c", "--cell-mode", help="pycharm|spyder (pycharm)")
    args = parser.parse_args()

    if not args.cell_mode:
        args.cell_mode = "pycharm"

    py2ipynb(args.input, args.output, args.cell_mode,
             ["# ----------------------------------------------------------------------------"])

