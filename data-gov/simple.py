import os
import json

data_json=[]

count=0

path = 'meta'
for filename in os.listdir(path):
    if not filename.endswith('.json'):
        continue
    filename = os.path.join(path, filename)
    print filename

    with open(filename, 'r') as fh:
        data = json.loads(fh.read())

        meta={}
        for dataset in data:
        	count=count+1
        	meta["title"]=dataset["title"]
        	try:
	        	#meta["description"]=dataset["description"]
	        	meta["identifier"]=dataset["identifier"]

	        	distribution=[]
	        	for dist in dataset["representations"]:
	        		print dist
	        		distribution.append({"accessURL":dist["accessUrl"],"format":dist["formats"][0]["label"]})
	        	meta["distribution"]=distribution
	        except:
	        	pass
        data_json.append(meta)

f=open("data.json","w")
f.write(json.dumps(data_json, indent=4))
f.close()


print "total num of datasets ",count
'''
#sample of new metadata in data.json
[
{
    "title": "White House Visitor Records Requests",
    "description": "A list of White House Visitor Record requests.",
    "distribution": [
          { 
            "accessURL": "https://explore.data.gov/api/views/644b-gaut/rows.csv?accessType=DOWNLOAD",
            "format": "csv"
          },
          { 
            "accessURL": "https://explore.data.gov/api/views/644b-gaut/rows.json?accessType=DOWNLOAD",
            "format": "json"
          },
          { 
            "accessURL": "https://explore.data.gov/api/views/644b-gaut/rows.xml?accessType=DOWNLOAD",
            "format": "xml"
          }
    ],
    "keyword": "visitor records, white house, transparency, government",
    "modified": "2013-04-26",
    "publisher": "Executive Office of the President",
    "person": "",
    "mbox": "",
    "identifier": "white-house-visitor-records",
    "accessLevel": "public",

    "license": "Data.gov license",
    
    "spatial": "Washington, DC",
    "temporal": "2010-01-01 12:00:00,2013-04-28 12:00:00",

    "issued": "2009-10-30",
    
    "accrualPeriodicity": "daily",
    "granularity": "person",
    "dataQuality" : "true",
    "category": "",
    "references": "https://explore.data.gov/dataset/White-House-Visitor-Records-Requests/644b-gaut",
    "landingPage": "https://explore.data.gov/dataset/White-House-Visitor-Records-Requests/644b-gaut",
    "systemOfRecords": "WAVES"
}
]


#sample of socrata simple metadata
{
  "created" : 1365539771,
  "description" : "Picture of Subsidized Households describes the nearly 5 million households living in HUD-subsidized housing in the United States for the year 2009. Picture 2009 provides characteristics of assisted housing units and residents, summarized at the national, state, public housing agency (PHA), project,census tract, county, Core-Based Statistical Area and city levels.",
  "identifier" : "6yrr-fxap",
  "lastModified" : 1366120221,
  "title" : "A Picture of Subsidized Households 2009",
  "keywords" : [ "Subsidized Households", "Section 8", "Multifamily assisted properties", "Section 236 Projects", "Public Housing", "Low housing income", "Housing Choice Vouchers", "FHA Insurance" ],
  "representations" : [ {
    "accessUrl" : "https://explore.data.gov/api/views/6yrr-fxap/rows.json?accessType=DOWNLOAD",
    "formats" : [ {
      "label" : "json",
      "value" : "application/json"
    } ]
  }, {
    "accessUrl" : "https://explore.data.gov/api/views/6yrr-fxap/rows.csv?accessType=DOWNLOAD",
    "formats" : [ {
      "label" : "csv",
      "value" : "text/csv"
    } ]
  }, {
    "accessUrl" : "https://explore.data.gov/api/views/6yrr-fxap/rows.xml?accessType=DOWNLOAD",
    "formats" : [ {
      "label" : "xml",
      "value" : "application/xml"
    } ]
  }, {
    "accessUrl" : "https://explore.data.gov/api/views/6yrr-fxap/rows.rdf?accessType=DOWNLOAD",
    "formats" : [ {
      "label" : "rdf",
      "value" : "application/xml+rdf"
    } ]
  }, {
    "accessUrl" : "https://explore.data.gov/api/views/6yrr-fxap/rows.xls?accessType=DOWNLOAD",
    "formats" : [ {
      "label" : "xls",
      "value" : "application/excel"
    } ]
  }, {
    "accessUrl" : "https://explore.data.gov/api/views/6yrr-fxap/rows.xlsx?accessType=DOWNLOAD",
    "formats" : [ {
      "label" : "xlsx",
      "value" : "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    } ]
  } ]
}
'''