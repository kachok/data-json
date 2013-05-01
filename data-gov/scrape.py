import requests
import json

#https://explore.data.gov/api/dcat.json?page=1
#https://explore.data.gov/api/views/ne3q-zie5.json

page=1
while True:
	r = requests.get('https://explore.data.gov/api/dcat.json?page=%s' % page)
	data = json.loads(r.text)

	f = open('data/page%s.json' % str(page).zfill(4), 'w')
	f.write(r.text.encode('utf8'))
	f.close()

	print "page ",page," ",len(data)
	page = page+1
	if len(data)==0:
		break
