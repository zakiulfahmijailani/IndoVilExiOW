# IndoVilExiOW
IndoVilExiOW represents a distinctive tool crafted to simplify the process of extracting and investigating individual village polygons across Indonesia by seamlessly integrating the capabilities of OpenStreetMap (OSM) and Wikipedia data sources. In Indonesia, renowned for its expansive geographical diversity and cultural heritage, the precise delineation of village boundaries holds pivotal importance across various domains, encompassing geographic information systems, urban planning, and disaster management. At its core, this tool leverages the OSMNX library to systematically navigate through the comprehensive list of kelurahan provided within the daftar_kelurahan.xlsx dataset. It subsequently orchestrates the automated retrieval of village polygons from OpenStreetMap in a bulk fashion.

The village names that serve as the bedrock of this process have been meticulously collected through web scraping from Wikipedia. These names find their compilation in the daftar_kelurahan.xlsx dataset, which comprises three integral columns: 'kelurahan' (village name), 'provinsi' (province), and 'negara' (country). The origination of this dataset is attributed to a detailed method accessible at: https://github.com/zakiulfahmijailani/Indonesia_Kelurahan_Names_From_Wikipedia. The culmination of these efforts results in the creation of a unified GeoJSON file, which emerges as a comprehensive repository facilitating exploration and analysis of village boundaries across Indonesia.

## Result
An initial glimpse into the outcome of this method is visualized in the image below, where village polygons are strikingly distinguished by their pink hue. Further insights into the specifics of these results are discussed below:

![image](https://github.com/zakiulfahmijailani/IndoVilExiOW/assets/30364443/73f7b449-a042-40db-a584-5bdd7a9a06a6)

The results underscore a certain level of variability. Notably, a majority of village polygons were proficiently retrieved from the islands of Sumatra and Java. Conversely, a more limited representation is apparent in regions such as Kalimantan, Sulawesi, Nusa Tenggara, and Bali. Strikingly, a mere handful of village polygons are discernible on Papua island.

Some outcomes yield intriguing characteristics, as certain polygons extend beyond terrestrial boundaries, encompassing adjacent sea territories. A case in point is showcased by the North Sumatera province, as depicted below. The province's boundary is juxtaposed with the green-colored province boundary acquired from the GADM (Global Administrative Areas) website: https://gadm.org/.

![image](https://github.com/zakiulfahmijailani/IndoVilExiOW/assets/30364443/87a43bd4-175a-4da6-9a61-027b1a233dce)

The most peculiar one manifests in the village polygon retrieval process for the provinces of Maluku and North Maluku. Evidently, a substantial polygon extends to envelop both provinces and the maritime expanses surrounding them:

![image](https://github.com/zakiulfahmijailani/IndoVilExiOW/assets/30364443/8be035b7-4418-4169-8090-c30a8eb96dd2)

On the opposite spectrum, the village polygons within Jakarta, the capital city, are notably comprehensive. Only five villages exhibit an inability to be retrieved, as highlighted below: 

![image](https://github.com/zakiulfahmijailani/IndoVilExiOW/assets/30364443/5d3b43b3-f75a-40f2-a1e1-85feaf279318)

## Conclusion
IndoVilExiOW effectively employs Python as an automation conduit for the bulk retrieval of village polygons from OpenStreetMap. This is achieved through the matching of village names from Wikipedia with their counterparts in OpenStreetMap. The tool boasts substantial potential in automating the utilization of open-sourced spatial data from OpenStreetMap within the context of regional geography. Nonetheless, this method remains open to suggestions, corrections, and collaborations. Those interested in enhancing and refining this methodology are encouraged to reach out via email at zakiul.jailani@bakrie.ac.id.
