#!/usr/bin/env python

"""
This program will enable you to get the descriptions of up to 300 Twitter Users
per run. If the code runs correctly, a csv file named user_descriptions.csv
will store the Twitter account descriptions next to the usernames.  This program
will also format nicely with a .txt file as well.  Change the name to
user_descriptions.txt from user_descriptions.csv.

Due to limits in the Twitter API, an app is rate limited after 100 Twitter user information requests. Therefore, you will need to 
create 3 apps (and have 3 sets of credentials) to run this code properly.  

System requirements.  You must ahve the following downloaded and installed on
your computer: python3, json, codes, and twython.


"""

import sys, string, json, codecs
from twython import Twython



# Here we have a comma deliminated list usernames we wish to get the
#descritions for

#Copy and paste the user names you wish to fetch the twitter descriptions for.
#Don't worry about formatting, the code will automatically parse this variable
#properly.


## copy and paste the user IDs you want into this variable
usr_nm = """ """


users = list(usr_nm.split())
users1 = users[0:99]
users2 = users[100:199]
users3 = users[200:299]



#print('Can not get descriptions after user:  {0}'.format(users[299]))

description_file = "user_descriptions.csv"


#We input the Twitter credentials as the following for keys.  If you run this
#program, generate your own set of keys via apps.twitter.com .


#credentials for app gatekeep 1

ak1 = ''
ask1 = ''
at1 = ''
ats1 = ''


credentials= Twython(   app_key=ak1,
                        app_secret=ask1,
                        oauth_token=at1,
                        oauth_token_secret=ats1
            )


data = credentials.lookup_user(user_id = users1)

i = 0
while (i < len(data)):
    profile = data[i]
    handle = str(profile['id'])
    description = profile['description'].replace("\t", " ")

    with codecs.open(description_file, 'a', encoding='utf-8') as out:
        out.write(u''+ handle + '\t' +
            description + '\n')
                         
       
    i = i +1

out.close()

# access tokens for gatekeep 2
ak2 = ''
ask2 = ''
at2 = ''
ats2 = ''

credentials2= Twython(   app_key=ak2,
                        app_secret=ask2,
                        oauth_token=at2,
                        oauth_token_secret=ats2
            )

data = credentials2.lookup_user(user_id = users2)

i = 0
while (i < len(data)):
    profile = data[i]
    handle = str(profile['id'])
    description = profile['description'].replace("\t", " ")

    with codecs.open(description_file, 'a', encoding='utf-8') as out:
        out.write(u''+ handle + '\t' +
            description + '\n')
                         
       
    i = i +1

out.close()



#access tokens for gatekeep 3
ak3 = ''
ask3 = ''
at3 = ''
ats3 = ''


credentials3= Twython(   app_key=ak3,
                        app_secret=ask3,
                        oauth_token=at3,
                        oauth_token_secret=ats3
            )



data = credentials3.lookup_user(user_id = users3)

i = 0
while (i < len(data)):
    profile = data[i]
    handle = str(profile['id'])
    description = profile['description'].replace("\t", " ")

    with codecs.open(description_file, 'a', encoding='utf-8') as out:
        out.write(u''+ handle + '\t' +
            description + '\n')
                         
       
    i = i +1

out.close()




