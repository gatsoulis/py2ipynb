# py2ipynb

Converts a .py file to a V.4 .ipynb notebook.

Modified from http://stackoverflow.com/questions/23292242/converting-to-not-from-ipython-notebook-format

## Usage

Default and pycharm-like:
```bash
./py2ipynb.py example_pycharmlike.py example_from_pycharmlike.ipynb
```

Spyder-like:
```bash
 ./py2ipynb.py -c spyder example_spyderlike.py example_from_spyderlike.ipynb
```

## Cell markers

### Code cell:
* pycharm-like: `##`
* spyder-like: `#%%`

**Default** is pycharm-like (`##`).

### Markdown cell:

Use one of the code cell markers first, then in a newline follow by `#md` 
(also `# md`, `#markdown`, `# markdown`), and include your markdown code within a block comment below. 
Everything till the next cell mark (e.g. `##` if using pycharm-like cell markers) will go to a 
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
