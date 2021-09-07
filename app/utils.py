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
  data = json.load(open('app/static/data/json/dim/all/relevant_data.json'))
  if id not in data:
    return 'Document not part of this work.'
  return data[id].values()


def get_vocab_words(text, vocab):
  """ Given a text, return a dictionary where each word of the text is a key
  and its value is a boolean indicating if the word is in the vocabulary. 
  Check also for n-grams up to length 4. Each a word is part of an n-gram, 
  output it only there and not individually. """
  res = dict()
  words = text.split(' ')
  i = 0
  while i < len(words):
    for j in range(i+4, i, -1):
      ngram = ' '.join(words[i:j])
      if ngram in vocab:
        res[ngram] = True
        i = j
        break
      elif j == i + 1:
        res[ngram] = False
        i += 1
  return res


def format_text(words):
  """ Given a dict with words as returned by get_vocab_words(), output a string
  that encloses each word whose value is True with the <mark> tags. """
  res = ""
  for word in words:
    if words[word] is True:
      res += f'<mark>{word}</mark> '
    else:
      res += word + ' '
  return res[:-1]


if __name__ == '__main__':
  vocab = json.load(open('app/static/data/vocab/repo_vocab.json'))
  words = get_vocab_words('this is a text with singular value decomposition and visual cortex', vocab)
  print(words)
