""" Swap keys and values of the 'data_processed_pos.json' file. """


import json


old = json.load(open('app/static/data/json/dim/all/data_processed_pos.json'))
new = {}

for doc_id in old:
	new[doc_id] = {}
	for text in ('title', 'abstract'):
		if text not in old[doc_id]:
			new[doc_id][text] = None
		else:
			new[doc_id][text] = []
			for word, indexes in old[doc_id][text].items():
				for idx in indexes:
					while idx >= len(new[doc_id][text]):
						new[doc_id][text].append(None)
					new[doc_id][text][idx] = word

json.dump(new, open('app/static/data/json/dim/all/data_processed_arr.json', 'w'))