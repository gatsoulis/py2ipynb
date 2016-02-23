#!/usr/bin/env python
"""Converts a .py file to a V.4 .ipynb notebook

Modified from http://stackoverflow.com/questions/23292242/converting-to-not-from-ipython-notebook-format
"""

import argparse
import nbformat
from nbformat.v4 import new_code_cell,new_notebook
import codecs


def parsePy(py_filename, cellmode, other_ignores=[]):
    """Converts a .py file to a V.4 .ipynb notebook using special cell markers.

    :param py_filename: .py filename
    :param cellmode: Determines cell marker based on IDE, {"pycharm": "##", "spyder": "#%%"}
    :param other_ignores: Other lines to ignore
    :return: A string containing one or more lines
    """
    cellmarks = {"pycharm": "##",
                 "spyder": "#%%"}
    ignores = [v for k, v in cellmarks.items() if k != cellmode] + other_ignores
    with open(py_filename, "r") as f:
        lines = []
        for l in f:
            l1 = l.strip()
            if lines and ((l1.startswith('# In[') and l1.endswith(']:')) or l1 == cellmarks[cellmode]):
                yield "".join(lines)
                lines = []
                continue
            if l1 not in ignores:
                lines.append(l)
        if lines:
            yield "".join(lines)

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
        cells.append(new_code_cell(source=c))

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

