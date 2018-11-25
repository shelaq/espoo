import requests
import json
import csv
import os
from .models import EspooRegionalData, EspooPopulations


# headers=['district', 'year', 'language_type', 'value']
# output = csv.DictWriter(open('file3.csv','w'), delimiter=',', fieldnames=headers)
# output.writerow(dict((fn,fn) for fn in headers))
# for row in rows:
#     output.writerow(row)


def load_language():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "data/native.csv"
    with open(os.path.join(script_dir, rel_path), 'r') as data_file:
        data = csv.reader(data_file, delimiter=',')
        next(data)
        for row in data:
            espoo_region = EspooRegionalData()
            espoo_region.district_id = row[0]
            espoo_region.year = row[1]
            espoo_region.language_type = row[2]
            espoo_region.language_num_ppl_speak = row[3]
            espoo_region.save()
            print('saved ', row[0])

def load():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "data/population.csv"
    with open(os.path.join(script_dir, rel_path), 'r') as data_file:
        data = csv.reader(data_file, delimiter=',')
        next(data)
        for row in data:
            espoo_region = EspooPopulations()
            espoo_region.district_id = int(row[0])
            espoo_region.year = int(row[1])
            if not int(row[2]) == 99999999:
                espoo_region.total_population = int(row[2])

            espoo_region.save()
            print('saved ', row[0])

def load_migrations():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "data/migration.csv"
    with open(os.path.join(script_dir, rel_path), 'r') as data_file:
        data = csv.reader(data_file, delimiter=',')
        next(data)
        for row in data:
            if row[3] == 'total':
                espoo_region = EspooPopulations(district_id = int(row[0]), year=int(row[1]))
                type_migration = row[2]
                if type_migration == 'Moved_to_the_municipality':
                    espoo_region.moved_to_municipality = int(row[4])
                elif type_migration == 'Sisainen_in-migration':
                    espoo_region.sisainen_in_migration = int(row[4])
                elif type_migration == 'Moved_from_the_municipality':
                    espoo_region.moved_from_municipality = int(row[4])
                elif type_migration == 'Sisainen_out-migration':
                    espoo_region.sisainen_out_migration = int(row[4])
                elif type_migration == 'Total_Net_Migration':
                    espoo_region.total_net_migration = int(row[4])
                espoo_region.save()
