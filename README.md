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

### Slide metadata

Add after the cell marker in a new line an optional slide metadata marker `#slide: <slide_type>` (also `# slide: <slide_type>`), where `<slide_type>` can be one of the standard slide types `-`, `slide`, `sub-slide`, `fragment`, `skip` and `notes`.

**Default** when there is no slide tag is `slide`.

E.g.

```python
##
```python
##
#md
#slide:skip
"""
# Header

* item 1
* item 2
"""

##
#slide:slide
print("hello world")
```

On how to convert the notebook to a static format (including slides format) read [this doc-page](http://ipython.org/ipython-doc/3/notebook/nbconvert.html), or specifically for slides generation [this guide](http://www.damian.oquanta.info/posts/make-your-slides-with-ipython.html) is helpful.

## Examples

See also examples: [pycharm-style](https://github.com/yianni/py2ipynb/blob/master/example_pycharmlike.py) | [spyder-style](https://github.com/yianni/py2ipynb/blob/master/example_spyderlike.py)
