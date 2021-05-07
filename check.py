import argparse
from tinydb import TinyDB, Query

parser = argparse.ArgumentParser(description='Check if id is valid/used.')
parser.add_argument('--id', type=str, required=True, help='ID to validate')
parser.add_argument('--used', required=False, action='store_true',
                    help='Add this flag to check if the ID has been used')

args = parser.parse_args()
id_to_check = args.id
check_if_used = args.used


def validate(some_id):
    # Basic checks: len == 7 and first two chars are not numbers
    if len(some_id) != 7:
        return False
    if some_id[0].isdecimal() or some_id[1].isdecimal():
        return False

    # Use check digit algorithm
    id_array = []
    id_array.append(ord(some_id[0]))
    id_array.append(ord(some_id[1]))
    id_array = id_array + list(some_id[2:6])

    check_digit_array = []
    for pos in range(0, len(id_array)):
        check_digit_array.append(int(id_array[pos]) * (pos+1))
    check_digit = sum(check_digit_array) % 10

    if int(some_id[6]) != check_digit:
        return False

    return True


def used(some_id):
    # Initialize or open DB and tables
    db = TinyDB('ids.json')
    site_table = db.table(some_id[0:2])
    IdQuery = Query()
    found = site_table.search(IdQuery.id == some_id)
    if len(found) == 0:
        return False
    else:
        return True


if not validate(id_to_check):
    raise ValueError('ID is invalid')
elif check_if_used == True:
    if used(id_to_check):
        print('ID is valid and has been used')
    else:
        print('ID is valid, but has not been used')
else:
    print('ID is valid')
