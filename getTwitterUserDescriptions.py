#!/usr/bin/env python

"""
This program will enable you to get the descriptions of up to 300 Twitter Users
per run. If the code runs correctly, a text file named user_descriptions.txt
will store the Twitter account descriptions next to the usernames.  This program
will also format nicely with a .csv file as well.  Change the name of
user_descriptions.txt to user_descriptions.csv.

NOTE: to collect the 300 Twitter User Descriptions per run, you must create 3 seperate sets of access tokens.  

System requirements.  You must ahve the following downloaded and installed on
your computer: python3, json, codes, and twython.


"""

import sys, string, json, codecs
from twython import Twython

"""Create a .txt file with the user IDs listed.  Insert the full path to the file in the string variable dirToFile """
dirToFile = ""

with open(dirToFile, 'r') as file:
    usr_nm= file.read().replace('\n', ' ')

users = list(usr_nm.split())

description_file = "user_timezones_new.csv"

""" Assign the following values with the proper access tokens. In order to collect information on 300 users, you must create 
three seperate apps.  Where ak1 is the access key (public) for the first app, ask1 is the acess key (secret) for the first app,
etc., and ak2 is the access key (pulic) for the second app, etc. 

All app credentials can be gathered at apps.Twitter.com, and an active Twitter account is required to create the apps."""

ak1, ask1, at1, ats1 = 
ak2, ask2, at2, ats2 = 
ak3, ask3, at3, ats3 = 

credentials_list = [ [ak1, ask1, at1, ats1],
                [ak2, ask2, at2, ats2],
                [ak3, ask3, at3, ats3] ]


users1, users2, users3 = users[0:100], users[100:200], users[200:300]

users_list = [users1, users2, users3]

for i in range(0,3):
    
    credentials =   Twython(    app_key=credentials_list[i][0],
                                app_secret=credentials_list[i][1],
                                oauth_token=credentials_list[i][2],
                                oauth_token_secret=credentials_list[i][3]
                            )
    data = credentials.lookup_user(user_id = users_list[i])

    j = 0
    while (j < len(data)):
        profile = data[j]
        handle = str(profile['id'])
        time_zone = str(profile['time_zone'])
        #screen_name = profile['screen_name']
        #utc_offset = profile['utc_offset']
        description = profile['description'].replace("\t", " ")
        

        with codecs.open(description_file, 'a', encoding='utf-8') as out:
            out.write(u''+ handle + '\t' + time_zone +'\n')                        
           
        j = j +1

out.close()



