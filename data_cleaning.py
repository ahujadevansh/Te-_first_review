import re
import nltk
import numpy as np
import pandas as pd
import string
import json

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


file_read = 'dataset/negative_reviews.json'
file_write = 'dataset/negative_reviews_token.json'
with open(file_read) as json_file:
            data = [json.loads(line) for line in json_file]
extreme = open(file_write, 'w')
for row in data:
    review = row['reviewText'].lower()

    review = ''.join(ch for ch in review if ch not in set(string.punctuation))

    review = nltk.word_tokenize(review)# converts to list of words

    ps = PorterStemmer()

    review = [ps.stem(word) for word in review
    if not word in set(stopwords.words('english'))]

    review = ' '.join(review)
    row['token'] = review
    
    extreme.write(json.dumps(row))
    extreme.write('\n')
