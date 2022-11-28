import requests
import json
import time
import codecs
import sys

json_start_mark = "<script>window.App="
json_end_mark = "</script><script nomodule="

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def print_yellow(text):
	print(color.YELLOW + text + color.END)

def print_cyan(text):
	print(color.CYAN + text + color.END)

def print_purple(text):
	print(color.PURPLE + text + color.END)

def parse_json(json_str):
	structure = json.loads(json_str)
	article_id = ""
	for k in structure['state']['articles']:
		article_id = k
		break
	
	items = structure['state']['articles'][article_id]["items"]
	for x in items["body"]:
		if (x["type"] == "paragraph"):
			print("\n")
			
			for e in x["items"]:
				if (e["type"] == "text"):
					print(e["text"])
				if (e["type"] == "bold" or e["type"] == "italic"):
					for n in e["items"]:
						if (n["type"] == "text"):
							if (e["type"] == "bold"):
								print_yellow(n["text"])
							else:
								print_purple(n["text"])
		if (x["type"] == "image"):
			print_cyan("\nIMAGE: " + x["urls"]["default"])

def load_url(url):
	req = requests.get(url)
	page_src = req.text
	json_start = page_src.split(json_start_mark,1)[1]
	json_str = json_start.split(json_end_mark,1)[0]
	final_json_str = json_str.replace("undefined", "null")
	return final_json_str

if (len(sys.argv) == 2):
	json_str = load_url(sys.argv[1])
	if (len(json_str) > 0):
		parse_json(json_str)




