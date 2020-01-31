import tkinter as tk
from collections import OrderedDict

import re
import nltk
import numpy as np
import pandas as pd
import string
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from basic import *

class InputPage(Basic):
    def __init__(self, root):
        super().__init__(root)
        self.add_widgets()
        self.positive_data = []
        self.negative_data = []
        self.positive_corpus = []
        self.negative_corpus = []

        with open('dataset/positive_reviews_token.json') as json_file:
            for line in json_file:
                js = json.loads(line)
                self.positive_data.append(js)
                self.positive_corpus.append(js['token'])
        
        with open('dataset/negative_reviews_token.json') as json_file:
            for line in json_file:
                js = json.loads(line)
                self.negative_data.append(js)
                self.negative_corpus.append(js['token'])
        
    
    def add_widgets(self):

        l1=tk.Label(self.f, bg="BLACK", fg="WHITE", text="Ask me: ", padx=1, pady=5, font="Times 25 bold")
        l1.place(x=100, y=200)
        self.e1=tk.Text(self.f,  width=60, height=3,  bg="WHITE",  fg="BLACK", font="Times 17")
        self.e1.place(x=250, y=205)
        
        self.sbimg=ImageTk.PhotoImage(Image.open("images/submit.jpg"))
        self.submit_button=tk.Button(self.panel, image=self.sbimg, command=self.OutputPage)
        self.submit_button.place(x=270, y=320)

    def OutputPage(self):

        query = self.e1.get('1.0', tk.END)
        query = query.lower()
        exclude = set(string.punctuation)
        query = ''.join(ch for ch in query if ch not in exclude)
        query = query.split()
        ps = PorterStemmer()
        query =[ps.stem(word) for word in query
        if not word in set(stopwords.words('english'))]
        query = ' '.join(query)

        self.positive_corpus.insert(0,  query)
        ans=[]
        positive_indexes=[]
        corpus_new=tuple(self.positive_corpus)
        tfidf_v=TfidfVectorizer(norm="l2")
        tfid_mat=tfidf_v.fit_transform(corpus_new)
        temp=cosine_similarity(tfid_mat[0],  tfid_mat[1::])
        for i in range(len(temp[0])):
            ans.append(temp[0][i])
        for i in range(10):
            m = max(ans)
            positive_indexes.append(ans.index(m))
            ans.remove(m)

        self.negative_corpus.insert(0,  query)
        ans=[]
        negative_indexes=[]
        corpus_new=tuple(self.negative_corpus)
        tfidf_v=TfidfVectorizer(norm="l2")
        tfid_mat=tfidf_v.fit_transform(corpus_new)
        temp=cosine_similarity(tfid_mat[0],  tfid_mat[1::])
        for i in range(len(temp[0])):
            ans.append(temp[0][i])
        for i in range(10):
            m = max(ans)
            negative_indexes.append(ans.index(m))
            ans.remove(m)
        # for x in indexes:
        #     print(self.data[x])

        self.f.destroy()
        super().__init__(self.root)

        self.f2=tk.Frame(self.root, height=950, width=1688)
        self.f2.place(x=35, y=100)
        temp_dict = dict()
        ro = 0
        for j in range(len(positive_indexes)):
            title = self.positive_data[positive_indexes[j]]['title']
            review = f"{self.positive_data[positive_indexes[j]]['reviewText']}"
            if title not in temp_dict:
                z1=tk.Label(self.f2, text=title, bg="WHITE", fg="BLACK", width=100, relief=tk.SOLID, borderwidth=1,  wraplength=650, justify=tk.LEFT)
                temp_dict[title] = None
                z1.grid(row=ro, column=0)
                ro = ro + 1
            z2=tk.Label(self.f2, text=review, bg="GREEN", fg="WHITE", width=100, relief=tk.SOLID, borderwidth=1,  wraplength=650, justify=tk.LEFT)
            z2.grid(row=ro, column=0)
            ro = ro + 1
        
        ro = 0
        for j in range(len(negative_indexes)):
            title = self.negative_data[negative_indexes[j]]['title']
            review = f"{self.negative_data[negative_indexes[j]]['reviewText']}"
            if title not in temp_dict:
                z1=tk.Label(self.f2, text=title, bg="WHITE", fg="BLACK", padx=1, width=100, relief=tk.SOLID, borderwidth=1,  wraplength=650, justify=tk.LEFT)
                temp_dict[title] = None
                z1.grid(row=ro, column=1)
                ro = ro + 1
            z2=tk.Label(self.f2, text=review, bg="RED", fg="WHITE", padx=1, width=100, relief=tk.SOLID, borderwidth=1,  wraplength=650, justify=tk.LEFT)
            z2.grid(row=ro, column=1)
            ro = ro + 1
