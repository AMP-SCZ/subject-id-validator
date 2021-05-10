# subject-id-validator
Python scripts to check subject IDs

### Requirements
Python 3

### Usage

```sh
python check.py [-h] --id ID
```

Where ID is the id to validate.

You may also import the module directly in the Python interpreter or your own scripts.

```python
>>> from idvalidator import validate
>>> validate('ME00011')
True
>>> validate('ME00012')
False
```
