# IndoVilExiOW
IndoVilExiOW is a unique tool designed to facilitate the extraction and exploration of individual village polygons across Indonesia by harnessing the power of OpenStreetMap (OSM) and Wikipedia data sources. With Indonesia's vast geographical diversity and rich cultural heritage, accurate village boundary data is essential for various applications such as geographic information systems, urban planning, and disaster management. This tool primarily utilizes the OSMNX library to iterate through all the listed kelurahan in the daftar_kelurahan.xlsx dataset and automatically retrieves village polygons from OpenStreetMap in bulk.

The village names used in this process were web-scrapped from Wikipedia and are compiled in the dataset daftar_kelurahan.xlsx. This Excel file contains three columns: 'kelurahan' (village name), 'provinsi' (province), and 'negara' (country). The dataset is the result of the method described in detail here: https://github.com/zakiulfahmijailani/Indonesia_Kelurahan_Names_From_Wikipedia.

The extracted village polygons are compiled into a single GeoJSON file, providing a comprehensive resource for exploring and analyzing village boundaries across Indonesia. 

## Result
