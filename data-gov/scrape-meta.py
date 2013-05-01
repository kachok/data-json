import os
import json
import settings

import requests

count=0

path = 'data'

for filename in os.listdir(path):
    if not filename.endswith('.json'):
        continue
    filename = os.path.join(path, filename)
    #print filename

    with open(filename, 'r') as fh:
        data = json.loads(fh.read())

        for dataset in data:
            count=count+1
            identifier=dataset["identifier"]
            
            print identifier, count

            r = requests.get('https://explore.data.gov/api/views/%s.json?app_token=%s' % (identifier, settings.settings["app_token"])

            f = open('meta/%s.json' % identifier, 'w')
            f.write(r.text.encode('utf8'))
            f.close()

#f=open("data.json","w")
#f.write(json.dumps(data_json, indent=4))
#f.close()
