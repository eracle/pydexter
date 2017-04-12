**pydexter** -
Python 3 client for the `Dexter <http://www.dxtr.it/>`_ REST API (`documentation <http://dexterdemo.isti.cnr.it:8080/dexter-webapp/dev/#!/rest>`_)

Installation::
```bash
    python setup.py install
```

Usage example:

```python

	from pydexter import DexterClient
	url = 'http://dexterdemo.isti.cnr.it:8080/dexter-webapp/api/'
	text = 'Dexter is an American television drama.'
	dxtr = DexterClient(url)
	dxtr.nice_annotate(text, min_conf=0.8)
```

['Dexter is an ', ('American television', 'Television_in_the_United_States'), ' drama.']

Test::

```bash
    python -m unittest test_pydexter
```

Todo: some API arguments are missing.