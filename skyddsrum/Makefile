.PHONY: all

all: skyddsrum.json skyddsrum.mbtiles

skyddsrum.json:
	ogr2ogr -f GeoJSON skyddsrum.json -t_srs EPSG:4326 skyddsrum-data/Inspire_skyddsrum.shp

skyddsrum.mbtiles:
	tippecanoe -o skyddsrum.mbtiles skyddsrum.json	

