import pandas as pd
import os
from urllib.request import urlopen, Request
import time
from tld import get_tld, get_fld


df = pd.read_csv("domains.csv")

# # print(df)

if not os.path.exists("domain_html"):
	os.mkdir("domain_html")

for link in df['domain_name']:
	# print("original: " +  link )
	# print(get_fld('http://' + link))
# 	# print("hello")
	f = open("domain_html/" + link, "wb")
	try:
		print("downloading(1st):" + link)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		fld_link = get_fld('http://' + link)
		request_link = "https://www." + fld_link
		req = Request(url = request_link, headers = headers)
		# f = open("domain_html/" + link, "wb")
		response = urlopen(req)
		html = response.read()
		f.write(html)
	except:
		print("downloading(2nd):" + link)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		fld_link = get_fld('http://' + link)
		request_link = "https://" + fld_link
		req = Request(url = request_link, headers = headers)
		# f = open("domain_html/" + link, "wb")
		response = urlopen(req)
		html = response.read()
		f.write(html)
	f.close()
	time.sleep(5)