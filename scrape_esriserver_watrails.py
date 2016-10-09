# Download polyline features from 
# http://wa-geoservices.maps.arcgis.com/apps/Viewer/index.html?appid=f7e9f357823a406abfc1ac89535c2470
# Note these data are now available for download in geodatabase format here
# http://rco.wa.gov/maps/Data.shtml

# July 15, 2016
# David Fisher


import json
# import pprint
import requests
from requests.exceptions import ConnectionError


## get all the object IDs from all the features in
## Layer 'WATrails_AggregatedMaster2015'

baseurl = 'http://services.arcgis.com/jsIt88o09Q0r1j8h/ArcGIS/rest/services/WATrails_AggregatedMaster2015/FeatureServer/0/query?'
q1 = 'where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&geohash=&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&outFields=&returnGeometry=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=true&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&quantizationParameters=&f=pjson&token='
qurl = baseurl + q1
 
req1 = requests.get(qurl)
req1_json = req1.json()

# pprint(jsntip)

oids = req1_json.values()[0]
print(len(oids))

## attribute fields to include
outfields='outFields=TR_NM%2C+TR_ALT_NM%2C+TR_NUM+%2CTR_SYS%2C+ATV%2C+BICYCLE%2C+DOG_SLED%2C+FOUR_WHEEL_DRIVE%2C+HIKER_PEDESTRIAN%2C+MOTORCYCLE%2C+PACK_AND_SADDLE%2C+SNOWMOBILE%2C+SNOWSHOE%2C+CROSS_COUNTRY_SKI%2C+TR_LENGTH%2C+TR_SURFC%2C+TR_STATUS%2C+NAT_TR_DES%2C+ACCESS_STA%2C+SPC_MGT_AR%2C+SPC_MGT_AR_COMMENTS%2C+PR_TR_MNTR%2C+PR_TR_MNTR_COMMENTS%2C+COUNTY%2C+AGENCY_DATA_SOURCE_GEO%2C+AGENCY_DATA_SOURCE_ATT%2C+REVIEW_FLAG%2C+OBJECTID'
q2 = 'returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&quantizationParameters=&f=pgeojson&token='

for i in range(len(oids)):
	if oids[i] % 100 == 0:
		print(oids[i])
	q3 = 'where=&objectIds=' + str(oids[i]) + '&time=&geometry=&geometryType=esriGeometryEnvelope&geohash=&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&'
	qurl2 = baseurl + q3 + outfields + q2
	req_geojson = requests.get(qurl2)
	geojson = req_geojson.json()
	with open('statewidetrail_' + str(oids[i]) + '.geojson', 'w') as outfile:
	    json.dump(geojson, outfile)

