import nltk
from nltk.corpus import stopwords
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
                        max_features=5000)
    f = RandomForestClassifier(n_estimators=100)
    forest = ''
    result = ''

    def study(self, directory):
        self.train_dir = directory
        self.train = self.collect(self.train_dir)
        self.start(self.train, self.clean_train_descriptions)
        self.train_data_features = self.bag_it(self.clean_train_descriptions)
        self.learn()

    def test(self, directory):
        self.test_dir = directory
        self.test = self.collect(self.test_dir)
        self.start(self.test, self.clean_test_descriptions)
        self.test_data_features = self.bag_it(self.clean_test_descriptions)
        self.testing()


    def collect(self, dir):

        return p.read_csv(dir, header = 0, delimiter = '\t', quoting=3)

    def remove_descriptions(self, file):



    def start(self, descriptions, descriptions_array):

        num_descriptions = len(descriptions)

        for i in range(0,num_descriptions):
            descriptions_array.append(self.clean(self.train["Description"][i]))


    def clean(self, raw):

        letters_only = re.sub("[^a-zA-Z]", " ", raw)
        words = letters_only.split()
        stop_words = set(stopwords.words("english"))
        content_words = [w for w in words if not w in stop_words]

        return " ".join(content_words)

    def bag_it(self, descriptions):

        a = self.v.fit_transform(descriptions)
        a = a.toarray()
        return a

    def learn(self):
        self.personal = self.train['Personal']
        self.subject = np.array(self.personal).astype(int)
        self.forest = self.f.fit(self.train_data_features, self.subject)

#We need to fix the dimensionality of this vector

    def testing(self):
        self.result = self.f.predict(self.test_data_features)
        output = p.DataFrame( data = {"id":self.test["UserID"],
                                           "Description":self.test["Description"],
                                           "Personal":self.test["Personal"]})
        output.to_csv("bag_of_words_model.csv", index=False, quoting = 3)








