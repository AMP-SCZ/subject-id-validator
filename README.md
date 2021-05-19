# subject-id-validator
Python scripts to check subject IDs

## ID Schema

A well-formed ID is 7 characters long, sequentially consisting of:

- 2 uppercase letters (Site ID)
- 4 digits
- 1 digit (check digit)

<details>
<summary>Details for the check digit algorithm</summary>

The check digit must correctly evaluate to the following:

```bash
{
  (ASCII value of 1st character * 1) +
  (ASCII value of 2nd character * 2) +
  (1st digit * 3) +
  (2nd digit * 4) +
  (3rd digit * 5) +
  (4th digit * 6)
} % 10
```

</details>

## Validator scripts

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

Where `ID` is the Subject ID to validate.

You may also import the module directly in the Python interpreter or your own scripts.

```python
>>> from idvalidator import validate
>>> validate('ME00011') # A valid ID
True
>>> validate('ME00012') # An invalid ID (wrong check digit)
False
```

The `validate` function will return `True` for valid IDs and `False` for invalid IDs.

**Note**: This validator accepts lowercase letters for the Site ID but will print a warning.

### Tests

You may run our test suite with the following command:

```sh
python test.py -b
```

This may also give you ideas for how to test your own implementation.
