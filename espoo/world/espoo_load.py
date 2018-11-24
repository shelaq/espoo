import requests
import json
import csv
import os
from .models import EspooRegionData


# headers=['district', 'year', 'language_type', 'value']
# output = csv.DictWriter(open('file3.csv','w'), delimiter=',', fieldnames=headers)
# output.writerow(dict((fn,fn) for fn in headers))
# for row in rows:
#     output.writerow(row)


def load():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "data/native.csv"
    with open(os.path.join(script_dir, rel_path), 'r') as data_file:
        data = csv.reader(data_file, delimiter=',')
        next(data)
        for row in data:
            row_list = row[0].split(',')
            # print(row_list[0])
            # print(int(row_list[1].replace('"','')))
            # print(row_list[2].replace('"',''))
            # print(row_list[3])
            espoo_region = EspooRegionData()
            espoo_region.district_id = row_list[0]
            espoo_region.year = int(row_list[1].replace('"',''))
            espoo_region.language_type = row_list[2].replace('"','')
            espoo_region.language_num_ppl_speak = row_list[3]
            espoo_region.save()
