# py2ipynb

Converts a .py file to a V.4 .ipynb jupyter/ipython notebook.

Modified from http://stackoverflow.com/questions/23292242/converting-to-not-from-ipython-notebook-format

## Usage

Default and pycharm style:
```bash
py2ipynb.py example_pycharmlike.py example_from_pycharmlike.ipynb
```

Spyder style:
```bash
 py2ipynb.py -c spyder example_spyderlike.py example_from_spyderlike.ipynb
```

## Cell markers

### Code cell:
* pycharm style: `##`
* spyder style: `#%%`

**Default** is pycharm style (`##`).

### Markdown cell:

Use one of the code cell markers first, then in a newline follow by `#md` 
(also `# md`, `#markdown`, `# markdown`), and include your markdown code within a block comment below. 
Everything till the next cell mark (e.g. `##` if using pycharm style cell markers) will go to a 
markdown cell.

E.g.

```python
##
#md
"""
# Header

* item 1
* item 2
"""

##
print("hello world")
```

## Examples

See also examples: [pycharm-style](https://github.com/yianni/py2ipynb/blob/master/example_pycharmlike.py) | [spyder-style](https://github.com/yianni/py2ipynb/blob/master/example_spyderlike.py)
