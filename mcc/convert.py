import json

data = []

template = json.loads("""
{
    "title": "System Data API",
    "description": "A restful web service for a system's data set from 2012.",
    "resources": [
          { 
            "accessURL": "http://www.agency.gov/data/raw/system_2012.csv",
            "format": "csv",
            "size": "20kb"
          },
          { 
            "accessURL": "http://www.agency.gov/data/raw/system_2012.json",
            "format": "json",
            "size": "10kb"
          },
          { 
            "accessURL": "http://www.agency.gov/data/raw/system_2012.pdf",
            "format": "pdf",
            "size": "27kb"
          }
    ],
    "keyword": "keyword1, keyword2",
    "modified": "2012-03-01",
    "publisher": "Agency",
    "person": "Bill, Smith",
    "mbox": "bill.smith@agency.gov",
    "identifier": "3",
    "accessLevel": "public",
    "dataDictionary": "http://www.agency.gov/data/information/system_api",
    "webService": "http://www.agency.gov/data/raw/data_api.json",
    "license": "creative commons Cco",
    "spatial": "United States",
    "temporal": "2012",
    "issued": "2012-03-01",
    "accrualPeriodicity": "weekly",
    "granularity": "address",
    "dataQuality" : "true",
    "category": "health",
    "references": "http://www.agency.gov/data/information/locations/document.doc",
    "landingPage": "http://agency.gov/data/mydata.html",
    "feed": "http://agency/gov/data/system_2012.rss",
    "systemOfRecords": "http://agency.gov/data/systemofrecord.pdf"
}
""")

template["modified"] = "today" #timestamp this
template["publisher"] = "Millenium Challenge Corporation"
template["person"] = "Dmitry Kachaev"
template["mbox"] = "kachaevd@mcc.gov"
template["accessLevel"] = "public"
template["webService"] = ""
template["license"] = "MCC Terms of Use, http://data.mcc.gov/termsofuse.html"
template["spatial"] = "N/A, World"
template["issued"] = "today" #timestamp this
template["dataQuality"] = "true"
template["landingPage"] = "http://data.mcc.gov"
template["feed"] = "N/A"
template["systemOfRecords"] = "http://data.mcc.gov"


f = open ("index.json")

index = json.loads(f.read())

for group in index["categories"]:
	group_id = group["id"]

	#print "processing group: ", group_id
	#print group 

	if group["type"] == "documents":
		template["title"] = group["name"]
		template["description"] = group["description"]
		template["resources"] = []
		template["keyword"] = group["type"]+", human-readable"
		template["identifier"] = "group" + str(group["id"])
		template["dataDictionary"] = "N/A"
		template["temporal"] = "TBD"
		template["accrualPeriodicity"] = "TBD"
		template["granularity"] = "TBD"
		template["theme"] = group["name"]
		template["references"] = "TBD"

		for dataset in index["datasets"]:
			if dataset["group_id"] == group_id:
				#print dataset

				resource = {}
				resource["accessURL"] = "http://data.mcc.gov/raw" + group["location"] + dataset["location"]
				template["title"] = dataset["name"]					
				template["description"] = dataset["name"]					
				resource["format"] = dataset["formats"][1:]
				#resource[""]
				template["distribution"]=[]
				template["distribution"].append(resource)

				data.append(json.loads(json.dumps(template)))
			



print json.dumps(data, indent=True)

fo = file ("human-readable.json", "w")
fo.write(json.dumps(data, indent=True))
fo.close()

f.close()

