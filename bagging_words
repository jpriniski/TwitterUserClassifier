#!/usr/bin/python
""" This module is still in drafting phases, and has some problems that need to be resolved.  However, here is the 
overall structure of program that will create a bag of words vectorization of term frequencies for our 
Twitter account descriptions.  

This will be the penultimate step in our ML process, with the final, of course, being implementation of a learning algorithim. 

"""

import codecs
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

descriptions ={}
descriptions_list = []

def collect_data(dir_to_data):

    """ Due to the variety of user descriptions (for example, the use of emojis and special characters),
    we must encode the description data using utf-8/unicode.  We import the codecs package to assist.

    We will collect the data from the .csv file.  Where the data is formatted as follows:
    ID \t description \n
    ID \t descriptions \n ...

    We will parse this, and then create a dictionary with the following form:
    {   'ID_1' : 'description_1'
        'ID_2' : 'description_2' ... }

    NOTE:   It is convenient to see the whole dictionary as our Boston Marathon Bombing corpus, while
            each description/string can be seen as the individual file/compoenent.
    """

    with codecs.open(dir_to_data, "r", encoding='utf-8', errors='ignore') as out:
        for user in out:
            (user_id, desc) = user.split("\t")
            user_id = user_id.replace('\"', "")
            desc = desc.replace('\"',"")
            descriptions[user_id] = desc

    return descriptions

def listify(descriptions):
    """We must turn the dictionary into a list so we can apply the scikit-learn methods to the
    descriptions.  This is also where we will employ our stemmer. To simplify the process, we only
    care in having the stems of words. Therefore, we will count derivatives of the same word as equivalent."""

    #iterate over each word and find the stem. write to the string
    stemmer = SnowballStemmer('english')

    for user_id, desc in descriptions.items():
        desc_word_list = desc.split()
        desc_stem_list = []

        for word in desc_word_list:
            stem = stemmer.stem(word)
            desc_stem_list.append(stem)

        desc_stem_string = ' '.join(desc_stem_list)
        user_id = desc_stem_string
        descriptions_list.append(user_id)
    return descriptions_list


def bag_it(list):

    """Words like I, me, we ... can help differentiate between personal and non-personal accounts.  So, for our purpose, we 
    removed words from the stop words list (ie. counted them in the term frequency) that may have helped in the suprivsed 
    classification"""
    
    stop_words = stopwords.words('english')
    stop_words = stop_words[100:127]

    v = CountVectorizer(stop_words=stop_words)
    bag_of_words = v.fit(list)
    bag_of_words = v.transform(list)
    print(bag_of_words)



def main():
    """Instructions:
        1. Set the directory to your user ID and user descriptions file
        2. Go through the collect_data method if interested
        3.Go through the listify data if interested
        3. We will print the bag of words for the text. However, some problems still need to be iorned out.
    """
    dir = ""
    data1 = collect_data(dir_to_data=dir)
    
    list1 = listify(data1)
    
    bag_it(list1)
   



main()

    
