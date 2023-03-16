#Author: William Bukowski

import nltk

text = "Paperspace is built for the future where hardware and software are linked, a lot more"
text = text.lower()

word_tokens = nltk.word_tokenize(text)
print(word_tokens)