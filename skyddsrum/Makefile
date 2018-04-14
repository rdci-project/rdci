.PHONY: all

all: skyddsrum.json 

skyddsrum.json:
	ogr2ogr -f GeoJSON skyddsrum.json -t_srs EPSG:4326 skyddsrum-data/Inspire_skyddsrum.shp

# db-schema:
# 	docker build -t naturalearthtiles/db-schema src/db-schema

# import-naturalearth:
# 	docker build -t naturalearthtiles/import-naturalearth src/import-naturalearth

# raster-datasource:
# 	docker build -t naturalearthtiles/raster-datasource src/raster-datasource
