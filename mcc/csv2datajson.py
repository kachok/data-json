import csv
import json

#read all resources in memory
resources={}
f=open('mcc-resources.csv', 'Urb')
listreader = csv.reader(f, delimiter=',', quotechar='"')
for i, row in enumerate(listreader):
	if i==0: pass
	else:
		id=row[0]
		url=row[1]
		format=row[2]
		if id in resources.keys():
			resources[id].append({"accessURL":url,"format":format})
		else:
			resources[id]=[]
			resources[id].append({"accessURL":url,"format":format})
f.close()

#read and dump all datasets metadata in output
f=open('mcc.csv', 'Urb')

header=""
datasets=[]

listreader = csv.reader(f, delimiter=',', quotechar='"')
for i, row in enumerate(listreader):
	dataset={}
	if i==0: header=row
	else:
		for j,item in enumerate(row):
			if item != "":
				#print header[j], item
				dataset[header[j]]=item
		#print "---"
		dataset["distribution"]=resources[dataset["identifier"]]
		datasets.append(dataset)


f.close()


f=open("external-catalog.json")
catalog=json.loads(f.read())
f.close()

for dataset in catalog:
	datasets.append(dataset)

f=open("api.json")
catalog=json.loads(f.read())
f.close()

for dataset in catalog:
	datasets.append(dataset)

f=open("human-readable.json")
catalog=json.loads(f.read())
f.close()

for dataset in catalog:
	datasets.append(dataset)
#dump datasets into data.json file
#print json.dumps(datasets, indent=4)

f=open("data.json","w")
f.write(json.dumps(datasets, indent=4))
f.close()
