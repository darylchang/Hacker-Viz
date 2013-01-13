from flask import Flask, render_template
import requests
import json
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
	r = requests.get("http://api.ihackernews.com/page")
	if (r):
		r = r.json()
		hacker_news_dict = {'name': 'hackernews', 'children':[]}
		num = 0

		for item in r["items"]:
			if num>10:
				break
			else:
				hacker_news_dict['children'].append({'points':item["points"],'link':item["url"], 'name':item["title"], 'comments':item["commentCount"]})
	 			num = num+1

		r = json.dumps(hacker_news_dict)
		print hacker_news_dict, r

		with open ('%s/static/flare.json' % os.path.abspath(os.path.dirname(__file__)),'w') as handle:
			handle.write(r)

	return render_template("index.html")
		

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
