# subject-id-validator
Python scripts to check subject IDs

### Requirements
Python 3

### Installation

No installation required, just clone the git repo or download the code.

```sh
git clone https://github.com/PREDICT-DPACC/subject-id-validator.git
```

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

### Tests

You may run our test suite with the following command:

```sh
python test.py
```

This may also give you ideas for how to test your own implementation.