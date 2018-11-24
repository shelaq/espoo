# espoo

Virtual environment:
$ mkdir venv
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate

Necessary installations in order for PostGIS to work:
$ brew install postgresql
$ brew install postgis
$ brew install gdal
$ brew install libgeoip
