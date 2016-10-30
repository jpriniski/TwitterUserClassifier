#!/usr/bin/env python

"""
get_user_information.py
Arizona State University
J. Hunter Priniski
Hazel Kwon

A more generalized version of get_user_descriptions.py, such that it enables you to collect other data than just descriptions. 

"""


from twython import Twython
import sys, string, json, codecs

class Connection:
    """A connection object has the following properties:

    Attributes:
        Access tokens: ak, ask, at, ats.

        The set of credentials gained from apps.Twitter.com


    Functionalities: allow users to collect data on up to 100 different Twitter Users. In the near future, this program will
    allow users to collect Twitter data without witnessing any of the backend code. 
    
    """

    def __init__(self, ak1, ask1, at1, ats1):
        self.tokens = [ak1, ask1, at1, ats1]

    def connect_to_twitter(self):
        self.credentials = Twython(app_key=self.tokens[0],
                                  app_secret=self.tokens[1],
                                  oauth_token=self.tokens[2],
                                  oauth_token_secret=self.tokens[3]
                                  )
        print(self.credentials)

    def get_users(self, directory_to_users):
        self.directory_to_users = directory_to_users

        with open(self.directory_to_users, 'r') as file:
            self.users_raw = file.read().replace('\n', ' ')
        self.users = list(self.users_raw.split())

        self.users_list = [self.users[0:100], self.users[100:200], self.users[200:300]]


    def search_ids(self):
        self.data = self.credentials.lookup_user(user_id=self.users_list[1])

    def search_screen_names(self):
        self.data = []
        for i in range(0, 2):
            self.data[i] = self.credentials.lookup_user(screen_names=self.users_list[i])

    def write_to_file(self, directory_to_output):
        self.directory_to_users = directory_to_output

        j = 0
        while (j < len(self.data)):
            self.profile = self.data[j]

            self.contributors_enabled = str(self.profile['contributors_enabled'])
            self.created_at = self.profile['created_at']
            self.default_profile = str(self.profile['default_profile'])
            self.default_profile_image = str(self.profile['default_profile_image'])
            self.description = self.profile['description'].replace("\t", " ")
            self.entities = str(self.profile['entities'])
            self.favourites_count = str(self.profile['favourites_count'])
            self.following = str(self.profile['following'])
            self.followers_count = str(self.profile['followers_count'])
            self.friends_count = str(self.profile['friends_count'])
            self.geo_enabled = str(self.profile['geo_enabled'])
            self.id_str = str(self.profile['id_str'])
            self.is_translator = str(self.profile['is_translator'])
            self.lang = self.profile['lang']
            self.listed_count = str(self.profile['listed_count'])
            self.location = str(self.profile['location'])
            self.notifications = str(self.profile['notifications'])
            self.profile_background_color = self.profile['profile_background_color']
            self.profile_background_image_url = str(self.profile['profile_background_image_url'])
            self.profile_background_image_url_https = str(self.profile['profile_background_image_url_https'])
            self.profile_image_url = self.profile['profile_image_url']
            self.protected = str(self.profile['protected'])
            self.screen_name = self.profile['screen_name']
            self.statuses_count = str(self.profile['statuses_count'])
            self.time_zone = str(self.profile['time_zone'])
            self.url = str(self.profile['url'])
            self.utc_offset = str(self.profile['utc_offset'])
            self.verified = str(self.profile['verified'])


            with codecs.open(directory_to_output, 'a', encoding='utf-8') as out:
                out.write(u''
                          + self.id_str + '\t'
                          + self.screen_name + '\t'
                          + self.created_at + '\t'
                          + self.description + '\t'
                          + self.followers_count + '\t'
                          + self.time_zone + '\t'
                          + self.geo_enabled + '\t'
                          + self.utc_offset + '\t'
                          + self.location + '\t'
                          + self.url + '\t'
                          + self.statuses_count + '\t'
                          + self.favourites_count + '\t'
                          + self.entities + '\t'
                          + self.lang + '\t'
                          + self.profile_background_color + '\t'
                          + self.profile_background_image_url + '\t'
                          + self.profile_background_image_url_https + '\t'
                          + self.profile_image_url + '\t'
                          + self.protected + '\t'
                          + self.verified + '\t'
                          + self.contributors_enabled + '\t'
                          + self.default_profile + '\t'
                          + self.default_profile_image + '\t'
                          + self.following + '\t'
                          + self.friends_count + '\t'
                          + self.notifications + '\t'
                          + self.listed_count + '\t'
                          + self.is_translator + '\t'

                          )

            j = j + 1

        out.close()

                              """   INPUT YOUR SPECIFIC INFORMATION BELOW (STEPS 1-3)  """
"""     1.
Input your Keys and Access tokens respecticely: 
Consumer Key (API Key), Consumer Secret (API Secret), Access Token, Access Token Secret
"""

connection_object = Connection("", "", "", "")  
connection_object.connect_to_twitter()

"""     2.a
Input the complete directory to the file you wish to write the Twitter Information"""

connection_object.get_users("/Directory_to_file_containing_user_IDs_or_screen_names")

"""     2.b
If you have a list of Twitter user IDs, comment out the line connection_object.seach_screen_names(), and instead use the
line of code connection_object.search_ids().  If you have a list of Twitter Screen names in your user file, isntead comment 
out the line of code connection_object.search_ids(). """

connection_object.search_ids()
connection_object.search_screen_names()

"""     3.
Input the complete directory to the file you wish to write the Twitter Information"""

connection_object.write_to_file("") 
