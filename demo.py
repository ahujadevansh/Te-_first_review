import re
import nltk
import numpy as np
import pandas as pd
import string
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

with open('positive_reviews.json') as json_file:
    data = [json.loads(line) for line in json_file]
# with open('negative_reviews.json') as json_file:
#     data = [json.loads(line) for line in json_file]
# dataset = []
# for review in data:
#     try:
#        dataset.append(review['reviewText'])
#     except KeyError:
#         pass


corpus = []

for foo in data:
    review = foo['reviewText'].lower()

    exclude = set(string.punctuation)

    review = ''.join(ch for ch in review if ch not in exclude)

    # review = review.split()

    review = nltk.word_tokenize(review)# converts to list of words

    ps = PorterStemmer()

    review = [ps.stem(word) for word in review
    if not word in set(stopwords.words('english'))]

    review = ' '.join(review)

    corpus.append(review)

# print(corpus)
query=input("ask me as ques: ")
query = query.lower()
exclude = set(string.punctuation)
query = ''.join(ch for ch in query if ch not in exclude)
query = query.split()
ps = PorterStemmer()
query =[ps.stem(word) for word in query
if not word in set(stopwords.words('english'))]
query = ' '.join(query)

corpus.insert(0, query)
ans=[]
indexes=[]
corpus_new=tuple(corpus)
# print(corpus_new)
tfidf_v=TfidfVectorizer(norm="l2")
tfid_mat=tfidf_v.fit_transform(corpus_new)
# print(tfidf_v.vocabulary_)
# print (tfid_mat.shape)
# print(tfid_mat)
temp=cosine_similarity(tfid_mat[0], tfid_mat[1::])
for i in range(len(temp[0])):
    ans.append(temp[0][i])
for i in range(10):
    m = max(ans)
    indexes.append(ans.index(m))
    ans.remove(m)
for x in indexes:
    print(data[x])
# print(sorted(ans,reverse=True))
