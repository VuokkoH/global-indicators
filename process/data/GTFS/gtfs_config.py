################################################################################
# Script: gtfs_config.py

# Description: This script contain GTFS parameters defined for each study regions
# for importing to conduct stop frequency analysis

# Note: most cities' parameters are based upon the stardard GTFS format
# however, this may not be the case for every study regions
# therefore, further research may be needed to define correct agency and route types
#
################################################################################

# set up study region GTFS config
analysis_period = ['07:00:00', '19:00:00']
headway_intervals = [20,30] # not implemented
dissolve_cities = ['hanoi'] # aggregate mean of headways by stop_id; does not retain mode
GTFS = {'helsinki':[{'gtfs_filename': 'gtfs_helsinki/gtfs_helsinki_hsl_20210927',
                    'gtfs_provider' : 'https://www.hsl.fi/',
                    'gtfs_year' : '2021',
                    'start_date_mmdd' : '20210927',
                    'end_date_mmdd' : '20211003',
                     'bbox' : (24.5001693455642986,60.0626721895615034, 25.2544954744790004,60.4012548634648994), # THIS IS NOW HMA BBOX
                     'crs':'epsg:32635',
                    'validation': False,
                    'modes' : {
                        # as per https://developers.google.com/transit/gtfs/reference#routestxt
                        'Tram'        : {'route_types': [ 0],'agency_id': None},
                        'Metro'       : {'route_types': [ 1],'agency_id': None},
                        'Rail'        : {'route_types': [ 109],'agency_id': None},
                        'Bus'         : {'route_types': [ 700, 701, 702, 704],'agency_id': None},
                        'Ferry'       : {'route_types': [ 4],'agency_id': None},
                        'Cable tram'  : {'route_types': [ 5],'agency_id': None},
                        'Aerial lift' : {'route_types': [ 6],'agency_id': None},
                        'Funicular'   : {'route_types': [ 7],'agency_id': None},
                        'Trolleybus'  : {'route_types': [11],'agency_id': None},
                        'Monorail'    : {'route_types': [12],'agency_id': None},
                    }
                   }],
                   
            'helsinkihma':[{'gtfs_filename': 'gtfs_helsinki/gtfs_helsinki_hsl_20210927',
                    'gtfs_provider' : 'https://www.hsl.fi/',
                    'gtfs_year' : '2021',
                    'start_date_mmdd' : '20210927',
                    'end_date_mmdd' : '20211003',
                     'bbox' : (24.5001693455642986,60.0626721895615034, 25.2544954744790004,60.4012548634648994),  # THIS IS NOW HMA BBOX
                     'crs':'epsg:32635',
                    'validation': False,
                    'modes' : {
                        # as per https://developers.google.com/transit/gtfs/reference#routestxt
                        'Tram'        : {'route_types': [ 0],'agency_id': None},
                        'Metro'       : {'route_types': [ 1],'agency_id': None},
                        'Rail'        : {'route_types': [ 109],'agency_id': None},
                        'Bus'         : {'route_types': [ 700, 701, 702, 704],'agency_id': None},
                        'Ferry'       : {'route_types': [ 4],'agency_id': None},
                        'Cable tram'  : {'route_types': [ 5],'agency_id': None},
                        'Aerial lift' : {'route_types': [ 6],'agency_id': None},
                        'Funicular'   : {'route_types': [ 7],'agency_id': None},
                        'Trolleybus'  : {'route_types': [11],'agency_id': None},
                        'Monorail'    : {'route_types': [12],'agency_id': None},
                    }
                   }],
                }
		