from xml.etree import ElementTree as ET
import json
import os


def get_doc(id):
  """ Return the title and abstract of the doc with the given DOI. """
  data = json.load(open(f'app/static/data/json/dim/all/relevant_data.json'))
  if id not in data:
    return 'Document not part of this work.'
  return data[id].values()
  