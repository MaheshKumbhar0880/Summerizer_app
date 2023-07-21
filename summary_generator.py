import spacy
from heapq import nlargest
nlp = spacy.load('en_core_web_sm')

# Importing the stopwords
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# stopwords = list(STOP_WORDS)``

def summary_generator(text_document):
  stopwords = list(STOP_WORDS)
  doc = nlp(text_document)
  tokens = [token.text for token in doc]
  word_freq = {}

  for word in doc:
    if (word.text.lower()) not in stopwords and word.text.lower() not in punctuation:
      if word.text not in word_freq.keys():
        word_freq[word.text] = 1
      else:
        word_freq[word.text] += 1

  max_freq = max(word_freq.values())

  for word in word_freq.keys():
    word_freq[word] = word_freq[word] / max_freq

  sent_tokens = [sent for sent in doc.sents]
  sent_scores = {}

  for sent in sent_tokens:
    for word in sent:
      if word.text in word_freq.keys():
        if sent not in sent_scores.keys():
          sent_scores[sent] = word_freq[word.text]
        else:
          sent_scores[sent] += word_freq[word.text]

  summ_length = int(len(sent_tokens) * 0.40)
  summary = nlargest(summ_length, sent_tokens, key=sent_scores.get)

  final = [word.text for word in summary]
  summary_lines = "".join(final)

  return text_document, summary_lines, len(text_document.split(' ')), len(summary_lines.split(' '))

# summary_generator(text)

