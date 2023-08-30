import pandas as pd
import json

# Path ke file XLSX
path_to_xlsx = 'daftar_kelurahan.xlsx'

# Membaca file XLSX menjadi DataFrame
daftar_kelurahan = pd.read_excel(path_to_xlsx)

# Menampilkan DataFrame
print(daftar_kelurahan)

import osmnx
import geopandas as gpd

results = []

for index, row in daftar_kelurahan.iterrows():
    kelurahan = row['kelurahan']
    provinsi = row['provinsi']
    negara = row['negara']
    
    PLACE_NAME = f"{kelurahan}, {provinsi}, {negara}"
    
    try:
            # Mengambil data area dengan menggunakan geocode_to_gdf
            area = osmnx.geocode_to_gdf(PLACE_NAME, which_result=1, by_osmid=True)
            # figure, ax = osmnx.plot_graph(area)

            results.append(area)

    except ValueError as e:
        print(f"Ignored error for {index, row}: {e}")
        continue

# Menggabungkan semua hasil menjadi satu GeoDataFrame
kelurahan_name_combined = gpd.GeoDataFrame(pd.concat(results, ignore_index=True))

# Menampilkan 20 data pertama
print(kelurahan_name_combined.head(20))

# Menyimpan GeoDataFrame ke dalam file GeoJSON
geojson_file_path = 'dataResult/kelurahan_data2.geojson'
kelurahan_name_combined.to_file(geojson_file_path, driver='GeoJSON')

print(f"Data tersimpan dalam file GeoJSON: {geojson_file_path}")