# Finland-spesific notes

## Computing environment 

**Computing environment set up for running the analysis in Finland:**

- Launched an Ubuntu 20.04 instance, 3xlarge volume (Size: 80 GB, RAM: 62.5 GB, VCPUs: 8) via [CSC pouta service](https://research.csc.fi/-/cpouta)
- Installed docker following these instructions: https://docs.docker.com/engine/install/ubuntu/ --> install using the repository
- To use docker without sudo; add user 'ubuntu' to user group 'docker': https://docs.docker.com/engine/install/linux-postinstall/ (then log out, log in)
- Verify that docker is installed correctly: 

```$ sudo docker run hello-world```



## Data downloads (todo: update conf-details)
1.  Download /prepare raw data and update the configuration files with correct filenames and paths:
	- **Study area boundaries** (store data in `./data` and update details in `pre_process/_project_configuration.xls`, sheet: `datasets`)
	- **GHS population data** (store data in `./data/GHS/WGS84`, check details in `pre_process/_project_configuration.xls`, sheet: `datasets`)
	- **GHS urban region data** (store data in `./data/GHS`, check details in `pre_process/_project_configuration.xls`, sheet: `datasets`)
	- **OpenStreetMap data** (store data in `./data`,  check details in `pre_process/_project_configuration.xls`, sheet: `project_settings`). Double check that OSM date settings are up-to-date in `process/setup_config.py`.
	- **GTFS data** (store GTFS data in `./data/GTFS`, and update details in `data/GTFS/gtfs_config.py`). See [pre_process/12_all_cities_gtfs_analysis_readme.md](./pre_process/12_all_cities_gtfs_analysis_readme.md) for detailed instructions.
	

## GTFS spesifics

GTFS route types in Helsinki region, according to [transitfeeds.com](https://transitfeeds.com/p/helsinki-regional-transport/735/latest/routes). Codes for Extended route types from [Google transit API docs](https://developers.google.com/transit/gtfs/reference/extended-route-types).

			- 0 Tram / Streetcar / Light Rail
			- 1 Subway / Metro
			- 4 Ferry
			- 109 Suburban Railway (Extended)
			- 700 Bus (Extended)
			- 701 Regional Bus (Extended)
			- 702 Express Bus (Extended)
			- 704 Local Bus (Extended)
