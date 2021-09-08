import json


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
  lemmas = json.load(open('app/static/data/json/dim/all/data_lemmas.json'))
  tokens = json.load(open('app/static/data/json/dim/all/data_tokens.json'))
  if id not in lemmas:
    return 'Document not part of this work.'
  return {
    'title': {
      'tokens': tokens[id]['title'], 'lemmas': lemmas[id]['title']
    },
    'abstract': {
      'tokens': tokens[id]['abstract'], 'lemmas': lemmas[id]['abstract']
    }
  }


def get_vocab_words(lemmas, vocab):
  """ Given a text, return a list of tuples where each tuple contains the 
  indexes of the words that compose that ngram, if it is present in the
  vocabulary. Check ngrams up to length 4. """
  res = []
  i = 0
  while i < len(lemmas):
    for j in range(i+4, i, -1):
      ngram = ' '.join(lemmas[i:j])
      if ngram in vocab:
        res.append(range(i, j))
        i = j
        break
      elif j == i + 1:
        i += 1
  return res


def format_text(tokens, indexes):
  """ Given a text and the indexes returned by get_vocab_words(), output a
  string that encloses each ngram present in 'indexes' with the <mark> tags. """
  if len(indexes) == 0:
    return ' '.join(tokens)
  res = ""
  ngram = indexes.pop(0)
  for idx, token in enumerate(tokens):
    if idx in ngram:
      token_inserted = False
      if ngram[0] == idx:
        res += f'<mark>{token} '
        token_inserted = True
      if ngram[-1] == idx:
        if not token_inserted:
          res += token
          token_inserted = True
        res += '</mark> '
        if len(indexes) > 0:
          ngram = indexes.pop(0)
        else:
          ngram = None
      if not token_inserted:
        res += token + ' '
    else:
      res += token + ' '
  return res[:-1]


if __name__ == '__main__':
  vocab = json.load(open('app/static/data/vocab/repo_vocab.json'))
  words = get_vocab_words('this is a text with singular value decomposition and visual cortex', vocab)
  print(words)
