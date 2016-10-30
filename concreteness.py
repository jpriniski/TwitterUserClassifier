import csv, codecs

"""
concreteness.py 
Arizona State University
J. Hunter Priniski (john.priniski@asu.edu)
Hazel Kwon (hazel.kwon@asu.edu)


Concreteness.py will calculate the concreteness rating for english sentences.

Word ratings are taken from Marc Brysbaert, Warriner, Kuperman (http://crr.ugent.be/papers/Brysbaert_Warriner_Kuperman_BRM_Concreteness_ratings.pdf)



*** TO RUN THIS SCRIPT ***
Declare the directories to your tweets (or other data) and concreteness ratings in main().  Then just run the script.  
Your concreteness ratings will be saved in the same directory but with a _with_ratings.csv appended to the end.  
i.e., if your tweet file directory is desktop/tweets.csv, your tweet file with ratings directory will be saved at:
desktop/tweets_with_ratings.csv



"""
    

def load(dir_to_text, dir_to_ratings):

    with codecs.open(dir_to_text, 'r', encoding = 'utf-8', errors = 'ignore', ) as csvfile_text:
        text = [rows for rows in csv.reader(csvfile_text)]

    with codecs.open(dir_to_ratings,'r', encoding = 'utf-8', errors = 'ignore') as csvfile_concreteness:
        ratings = {rows[0]: rows[1] for rows in csv.reader(csvfile_concreteness)}

    return text, ratings


def concreteness(text, ratings):
    count = 0
    score_total = 0

    for word in text[0].split():
        if word in ratings:
            count +=1
            score_total += float(ratings[word])

    if count != 0:
        return (text, count, score_total/count)
    else:
        return(text, 0,0)
    

def write(dir_to_text, text_ratings):
    
    dir_to_output = dir_to_text[:-4] + "_with_ratings.csv"
    data = codecs.open(dir_to_output, 'w', encoding = 'utf-8', errors = 'ignore')
    writer = csv.writer(data)
    writer.writerows(text_ratings)
    data.close()

    print("Script Finished. Concreteness scores saved to: " + dir_to_text)
    
    
def main():
    #in these two variables, load in the directories.  Tweets should be loaded in a single column and in utf-8 format
    dir_to_tweets = ""
    #let this variable represent the directory to the concreteness ratings. See paper mentioned above for more information on this
    dir_to_concreteness = ""
    tweet_concreteness = []

    tweets, concreteness_ratings = load(dir_to_tweets, dir_to_concreteness)

    for tweet in tweets:
        tweet_concreteness.append(concreteness(tweet, concreteness_ratings))

    write(dir_to_tweets, tweet_concreteness)
     
 
main()
