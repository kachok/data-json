import json
import csv

f1 = open("mcc.csv", "wb")
f2 = open("mcc-resources.csv", "wb")
f = csv.writer(f1 , delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
fr = csv.writer(f2 , delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

header = "title	description	keyword	modified	publisher	person	mbox	identifier	accessLevel	COMMON-EXPANDED	dataDictionary	accessURL	webService	format	license	spatial	temporal	EXPANDED	issued	accrualPeriodicity	language	granularity	dataQuality	theme	references	size	landingPage	feed	systemOfRecords"
header2 = "identifier	url	format"
f.writerow(header.split("	"))
fr.writerow(header2.split("	"))

data = {"datasets":[]}

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


indexjson = open ("index.json")

index = json.loads(indexjson.read())

indexjson.close()

for group in index["categories"]:
	group_id = group["id"]

	#print "processing group: ", group_id
	#print group 

	if group["type"] == "documents":
		template["title"] = group["name"]
		template["description"] = group["description"]
		template["resources"] = []
		template["keyword"] = group["type"]
		template["identifier"] = "group" + str(group["id"])
		template["dataDictionary"] = "N/A"
		template["temporal"] = "TBD"
		template["accrualPeriodicity"] = "TBD"
		template["granularity"] = "TBD"
		template["category"] = group["type"]
		template["references"] = "TBD"

		for dataset in index["datasets"]:
			if dataset["group_id"] == group_id:
				#print dataset

				resource = {}
				resource["accessURL"] = "http://data.mcc.gov/raw" + group["location"] + dataset["location"]
				resource["name"] = dataset["name"]					
				resource["format"] = dataset["formats"][1:]
				#resource[""]

				template["resources"].append(resource)

		data["datasets"].append(json.loads(json.dumps(template)))
			
	else:
		for dataset in index["datasets"]:
			if dataset["group_id"] == group_id:
				#print dataset

				title=dataset["name"]
				description=dataset["description"]
				keyword=""
				modified="2013-05-01 00:00:00"
				publisher="Millennium Challenge Corporation"
				person="Open Data Initiative"
				mbox="opendata@mcc.gov"
				identifier=dataset["group_location"][1:].replace("/","-")+"-"+dataset["location"][1:][:-4]
				accessLevel="Public"
				COMMONEXPANDED=""
				dataDictionary="http://data.mcc.gov"+dataset["group_location"]+dataset["metadatalocation"]
				accessURL=""
				webService=""
				format=""
				license="data.mcc.gov terms of use - http://data.mcc.gov/termsofuse.html"
				spatial=""
				temporal=""
				EXPANDED=""
				issued="2013-05-01 00:00:00"
				accrualPeriodicity=""
				language="English"
				granularity=""
				dataQuality="true"
				theme=group["description"]
				references=""
				size=""
				landingPage="http://data.mcc.gov"
				feed=""
				systemOfRecords=""

				#f.writerow(["title	description	keyword	modified	publisher	person	mbox	identifier	accessLevel	COMMON-EXPANDED	dataDictionary	accessURL	webService	format	license	spatial	temporal	EXPANDED	issued	accrualPeriodicity	language	granularity	dataQuality	theme	references	size	landingPage	feed	systemOfRecords"])
				f.writerow([title,description,keyword,modified,publisher,person,mbox,identifier,accessLevel,COMMONEXPANDED,dataDictionary,accessURL,webService,format,license,spatial,temporal,EXPANDED,issued,accrualPeriodicity,language,granularity,dataQuality,theme,references,size,landingPage,feed,systemOfRecords])
				fr.writerow([identifier, "http://data.mcc.gov/raw" + group["location"] + dataset["location"], dataset["formats"][1:]])
				
				data["datasets"].append(json.loads(json.dumps(template)))

				#print json.dumps(template, indent=True)


print json.dumps(data, indent=True)


f1.close()
f2.close()

