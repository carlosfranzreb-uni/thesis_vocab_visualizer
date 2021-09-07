from xml.etree import ElementTree as ET
import json
import os


def get_vocab(vocab_name):
  if vocab_name == 'Unfiltered':
    return json.load(open('app/static/data/vocab/repo_vocab.json'))
  elif vocab_name == 'Step 1':
    return json.load(open('app/static/data/vocab/repo_vocab_step_1.json'))
  elif vocab_name == 'Step 2':
    return json.load(open('app/static/data/vocab/repo_vocab_step_2.json'))
  elif vocab_name == 'Step 4':
    return json.load(open('app/static/data/vocab/repo_vocab_step_4.json'))


def get_doc(id):
  """ Return the title and abstract of the doc with the given DOI. """
  data = json.load(open('app/static/data/json/dim/all/data_processed.json'))
  original_data = json.load(open('app/static/data/json/dim/all/relevant_data.json'))
  if id not in data:
    return 'Document not part of this work.'
  return {
    'title': {
      'original': original_data[id]['title'], 'processed': data[id]['title']
    },
    'abstract': {
      'original': original_data[id]['abstract'], 'processed': data[id]['abstract']
    }
  }


def get_vocab_words(processed, vocab):
  """ Given a text, return a list of tuples where each tuple contains the 
  indexes of the words that compose that ngram, if it is present in the
  vocabulary. Check ngrams up to length 4. """
  res = []
  i = 0
  while i < len(processed):
    for j in range(i+4, i, -1):
      ngram = ' '.join(processed[i:j])
      if ngram in vocab:
        res.append(range(i, j))
        i = j
        break
      elif j == i + 1:
        i += 1
  return res


def format_text(text, indexes):
  """ Given a text and the indexes returned by get_vocab_words(), output a
  string that encloses each ngram present in 'indexes' with the <mark> tags. """
  if len(indexes) == 0:
    return text
  res = ""
  ngram = indexes.pop(0)
  for idx, word in enumerate(text.split(' ')):
    if idx in ngram:
      word_inserted = False
      if ngram[0] == idx:
        res += f'<mark>{word} '
        word_inserted = True
      if ngram[-1] == idx:
        if not word_inserted:
          res += word
          word_inserted = True
        res += '</mark> '
        if len(indexes) > 0:
          ngram = indexes.pop(0)
        else:
          ngram = None
      if not word_inserted:
        res += word + ' '
    else:
      res += word + ' '
  return res[:-1]


if __name__ == '__main__':
  vocab = json.load(open('app/static/data/vocab/repo_vocab.json'))
  words = get_vocab_words('this is a text with singular value decomposition and visual cortex', vocab)
  print(words)
