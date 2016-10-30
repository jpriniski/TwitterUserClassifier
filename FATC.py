import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import pandas as p
import re

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

from sklearn.ensemble import RandomForestClassifier

#FTAC stands for (Random) Forest Twitter Account Classification
class FTAC:
    train_dir = []
    test_dir = []
    train = []
    test = []
    subject = []
    clean_train_descriptions = []
    clean_test_descriptions = []
    train_data_features = []
    test_data_features = []
    v = CountVectorizer(analyzer="word",
                        tokenizer=None,
                        preprocessor=None,
                        stop_words=None,
                        #5000, 500
                        max_features=500)
    f = RandomForestClassifier(n_estimators=100)
    forest = ''
    result = ''

    stemmer = SnowballStemmer('english')

    def study(self, directory):
        self.train_dir = directory
        self.train = self.collect(self.train_dir)
        self.start(self.train, self.clean_train_descriptions)
        self.train_data_features = self.bag_it(self.clean_train_descriptions)
        self.learn()

    def collect(self, dir):

        return p.read_csv(dir, header = 0, sep = '\t', quoting=3)


    def start(self, descriptions, descriptions_array):

        num_descriptions = len(descriptions)

        for i in range(0,num_descriptions):#need to call the stem function here, remove it if you don't want it
            descriptions_array.append(self.clean(self.train["Description"][i]))


    def clean(self, raw):

        letters_only = re.sub("[^a-zA-Z#@]", " ", raw)

        words = letters_only.split()

        for i in range(0, len(words)):

            if "#" in words[i]:
                s = words[i].split('#')
                words[i] = '# '.join(s)
            if "@" in words[i]:
                s = words[i].split('@')
                words[i] = '@ '.join(s)
            if "http" in words[i]:
                s = words[i].split('http')
                words[i]= "http".join(s)


        total_stop_words = set(stopwords.words("english"))
        removed_stop_words = set(stopwords.words("english")[0:20])
        stop_words = total_stop_words - removed_stop_words
        content_words = [w for w in words if not w in stop_words]

        return " ".join(content_words)

    def stem(self, content_words):
        #take the content words and stem them
        words = content_words.split()
        roots = [self.stemmer.stem(word) for word in words]

        return " ".join(roots)

    def bag_it(self, descriptions):

        a = self.v.fit_transform(descriptions)
        a = a.toarray()
        return a

    def learn(self):
        self.personal = self.train['Personal']
        self.subject = np.array(self.personal).astype(int)
        self.forest = self.f.fit(self.train_data_features, self.subject)











