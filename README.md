# IndoVilExiOW

**Indo**nesia **Vil**lage **Ex**tractor via **O**penStreetMap & **W**ikipedia

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OSMnx-OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white" />
  <img src="https://img.shields.io/badge/Output-GeoJSON-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Coverage-Indonesia-red?style=flat-square" />
</p>

IndoVilExiOW is a Python tool for bulk extraction of individual village (kelurahan) polygons across Indonesia by combining **OpenStreetMap (OSM)** boundary data with village name lists scraped from **Wikipedia**. It produces a unified GeoJSON file ready for use in GIS analysis, urban planning, and spatial data pipelines.

---

## How It Works

1. Reads village names from `daftar_kelurahan.xlsx` — a dataset of Indonesian *kelurahan* names collected via Wikipedia scraping ([source repo](https://github.com/zakiulfahmijailani/Indonesia_Kelurahan_Names_From_Wikipedia))
2. For each village, queries OSM via `osmnx.geocode_to_gdf()` using the format `kelurahan, provinsi, Indonesia`
3. Collects all retrieved polygons into a single `GeoDataFrame`
4. Exports the result as a GeoJSON file to `dataResult/`

---

## Installation

```bash
# Clone the repository
git clone https://github.com/zakiulfahmijailani/IndoVilExiOW.git
cd IndoVilExiOW

# Install dependencies
pip install pandas openpyxl osmnx geopandas
```

---

## Usage

```bash
python kelurahanOSM.py
```

The script will:
- Read `daftar_kelurahan.xlsx` (columns: `kelurahan`, `provinsi`, `negara`)
- Query OSM for each village polygon
- Save results to `dataResult/kelurahan_data2.geojson`

Errors for villages not found in OSM are logged and skipped automatically.

---

## Results

An initial run across Indonesia produced the following coverage:

![Indonesia village polygons overview](https://github.com/zakiulfahmijailani/IndoVilExiOW/assets/30364443/73f7b449-a042-40db-a584-5bdd7a9a06a6)

**Coverage observations:**
- ✅ High coverage: Sumatra and Java
- ⚠️ Partial coverage: Kalimantan, Sulawesi, Nusa Tenggara, Bali
- ❌ Low coverage: Papua

**Known limitations:**
- Some polygons extend beyond land boundaries into adjacent sea territories (e.g., North Sumatera province)

  ![North Sumatera boundary issue](https://github.com/zakiulfahmijailani/IndoVilExiOW/assets/30364443/87a43bd4-175a-4da6-9a61-027b1a233dce)

- Maluku and North Maluku return an anomalously large polygon covering both provinces and surrounding seas

  ![Maluku anomaly](https://github.com/zakiulfahmijailani/IndoVilExiOW/assets/30364443/8be035b7-4418-4169-8090-c30a8eb96dd2)

- Jakarta (capital city) has near-complete coverage, with only 5 villages unretrieved

  ![Jakarta coverage](https://github.com/zakiulfahmijailani/IndoVilExiOW/assets/30364443/5d3b43b3-f75a-40f2-a1e1-85feaf279318)

---

## Dataset

| File | Description |
|---|---|
| `daftar_kelurahan.xlsx` | Village name list (kelurahan, provinsi, negara) scraped from Wikipedia |
| `dataResult/` | Output directory for GeoJSON results |
| `kelurahanOSM.py` | Main extraction script |

---

## Contributing

This tool is open to improvements, corrections, and collaborations — especially around:
- Improving OSM query accuracy for low-coverage regions
- Adding fallback strategies for failed retrievals
- Extending coverage to desa-level administrative units

Feel free to open an [Issue](https://github.com/zakiulfahmijailani/IndoVilExiOW/issues) or reach out directly: [zakiul.jailani@bakrie.ac.id](mailto:zakiul.jailani@bakrie.ac.id)

---

<p align="center">
  <sub>Built for Indonesia’s geographic diversity. Powered by open data.</sub>
</p>
