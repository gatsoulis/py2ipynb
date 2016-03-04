# py2ipynb

Converts a .py python source file to a V.4 .ipynb jupyter/ipython notebook.

Based on [this](http://stackoverflow.com/a/32994192/4720148) and [this](http://stackoverflow.com/a/35720002/4720148) posts. Question originally asked on [stackoverflow](http://stackoverflow.com/questions/23292242/converting-to-not-from-ipython-notebook-format).

## Usage

Run from the examples folder, and don't forget to add the `py2ipynb` path to your system path.

_Default_:

```bash
py2ipynb.py example_default.py example_default.ipynb
```

_Pycharm style_:

```bash
py2ipynb.py example_pycharmlike.py example_from_pycharmlike.ipynb -c pycharm
```

_Spyder style_:

```bash
py2ipynb.py example_spyderlike.py example_from_spyderlike.ipynb -c spyder
```

## Cell Markers

### Default style

For `default` style, see the [source code](https://github.com/ipython/ipython/blob/rel-3.2.1/IPython/nbformat/v3/nbpy.py#L48) (look at the `if/elif line.startswith` statements).

From this, it seems that generally the markers are `# <codecell>`, `# <markdowncell`, `# <rawcell>`, and the deprecated in V.4 `# <htmlcell>` and `# <headingcell`.

### Pycharm/Spyder style

#### Code cell:

- pycharm style: `##`
- spyder style: `#%%`

#### Markdown cell:

Use one of the code cell markers first, then in a newline follow by `#md` (also `# md`, `#markdown`, `# markdown`), and include your markdown code within a block comment below. Everything till the next cell mark (e.g. `##` if using pycharm style cell markers) will go to a markdown cell.

E.g.

```python
##
# md
"""
# Header

* item 1
* item 2
"""

##
print("hello world")
```

#### Inline matplotlib

Simply add in a new line after the cell marker `#%matplotlib inline` or `# %matplotlib inline`, or instead of `inline` any [other supported backend](http://ipython.org/ipython-doc/stable/interactive/reference.html#plotting-with-matplotlib).

#### Slide metadata

Add after the cell marker in a new line an optional slide metadata marker `#slide: <slide_type>` (also `# slide: <slide_type>`), where `<slide_type>` can be one of the standard slide types `-`, `slide`, `sub-slide`, `fragment`, `skip` and `notes`.

**Default** when there is no slide tag is `slide`.

E.g.

````python
##
```python
##
# md
# slide:skip
"""
# Header

* item 1
* item 2
"""

##
#slide:slide
print("hello world")
````

On how to convert the notebook to a static format (including slides format) read [this doc-page](http://ipython.org/ipython-doc/3/notebook/nbconvert.html), or specifically for slides generation [this guide](http://www.damian.oquanta.info/posts/make-your-slides-with-ipython.html) is helpful.

## Examples

See also examples: [default](https://github.com/yianni/py2ipynb/blob/master/examples/example_default.py) | [pycharm-style](https://github.com/yianni/py2ipynb/blob/master/examples/example_pycharmlike.py) | [spyder-style](https://github.com/yianni/py2ipynb/blob/master/examples/example_spyderlike.py)
