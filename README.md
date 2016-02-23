# py2ipynb

Converts a .py file to a V.4 .ipynb notebook.

Modified from http://stackoverflow.com/questions/23292242/converting-to-not-from-ipython-notebook-format

## Usage

Default and pycharm-like:
```bash
./py2ipynb.py -i example_pycharmlike.py -o example_from_pycharmlike.ipynb
```

Spyder-like:
```bash
 ./py2ipynb.py -i example_spyderlike.py -o example_from_spyderlike.ipynb -c spyder
```

## Cell markers

* pycharm-like: `##`
* spyder-like: `#%%`

Default is pycharm-like (`##`).
