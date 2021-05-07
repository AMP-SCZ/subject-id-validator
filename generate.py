import argparse
import csv
from tinydb import TinyDB, Query

parser = argparse.ArgumentParser(description='Generate ids for a site.')
parser.add_argument('--site', type=str, required=True, help='2-letter site ID')
parser.add_argument('-n', type=int, default=1, required=False,
                    help='Number of ids to generate (default: 1)')

# Validate Site ID
args = parser.parse_args()
if not len(args.site) == 2:
    raise ValueError('--site argument must be 2 letters')

site_id = args.site.upper()
found_site = False
with open('sites.csv', newline='') as csvfile:
    sites_reader = csv.DictReader(csvfile)
    for row in sites_reader:
        if row['id'] == site_id:
            print('Site: ' + row['name'])
            found_site = True

if found_site == False:
    raise ValueError('Site ID could not be found')


def get_id_seq(site):
    # Get the next number in the sequence from 1-9999 for this site
    IdSeq = Query()
    id_seq_for_site = id_seq_table.search(IdSeq.site == site)
    id_seq = 1
    if len(id_seq_for_site) == 0:
        id_seq_table.insert({'site': site, 'seq': 1})
    else:
        id_seq = id_seq_for_site[0]['seq']
    return id_seq


def generate_id(site, index, table, idseq):
    # Start array for check digit calc
    new_id_array = []

    # Convert two ASCII chars to ints
    new_id_array.append(ord(site[0]))
    new_id_array.append(ord(site[1]))

    # Get next 4 numerals based on index
    fournums = str(index).zfill(4)
    new_id_array = new_id_array + [int(s) for s in list(fournums)]

    # Calc and append check digit
    check_digit_array = []
    for pos in range(0, len(new_id_array)):
        check_digit_array.append(new_id_array[pos] * (pos+1))
    check_digit = sum(check_digit_array) % 10

    # Generate ID from site ID + array + check digit and insert
    new_id = site + fournums + str(check_digit)
    print(new_id)
    table.insert({'id': new_id})

    # Update id sequence
    IdSeqs = Query()
    id_seq_table.update({'site': site, 'seq': index+1}, IdSeqs.site == site)


# Initialize or open DB and tables
db = TinyDB('ids.json')
site_table = db.table(site_id)
id_seq_table = db.table('idseq')

# Get next ID in sequence
id_seq_current = get_id_seq(site_id)
if (id_seq_current + args.n) > 9999:
    raise ValueError('Cannot exceed 9999 IDs per site')

# Generate IDs
for i in range(id_seq_current, id_seq_current + args.n):
    generate_id(site_id, i, site_table, id_seq_table)
