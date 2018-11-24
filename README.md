# espoo

Virtual environment:
```
$ mkdir venv
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
```

Necessary installations in order for PostGIS to work:
```
$ brew install postgresql
$ brew install postgis
$ brew install gdal
$ brew install libgeoip
```


Run the server:
```
cd espoo
python3 manage.py runserver
```


Setup for ingesting data easily:
```
python3 manage.py ogrinspect world/data/FILE_NAME.shp ClassName --srid=4326 --mapping --multi
```
- The --srid=4326 option sets the SRID for the geographic field.
- The --mapping option tells ogrinspect to also generate a mapping dictionary for use with LayerMapping.
- The --multi option is specified so that the geographic field is a MultiPolygonField instead of just a PolygonField.

The first part of the output should be copied to `models.py`
The second part should be copied to `load.py`, with the necessary modifications to the file (tranform = True maybe)


To migrate the data:
```
python3 manage.py makemigrations (create model)
python3 manage.py sqlmigrate world 000#
python3 manage.py migrate

python3 manage.py shell
>> from world import load
>> load.run()
```

To see the data, make appropriate changes to admin.py
