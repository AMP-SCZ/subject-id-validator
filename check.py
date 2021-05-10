import argparse
from idvalidator import validate

parser = argparse.ArgumentParser(description='Check if id is valid.')
parser.add_argument('--id', type=str, required=True, help='ID to validate')

args = parser.parse_args()
id_to_check = args.id

if not validate(id_to_check):
    print('***ERROR: ID is invalid.')
else:
    print('ID is valid.')
