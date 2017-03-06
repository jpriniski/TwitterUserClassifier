import sys, string, json, codecs
from twython import Twython

def readData(directory):
	with open(directory, 'r') as file:
		usr_nm= file.read().replace('\n', ' ')

	users = list(usr_nm.split())
	print(str(len(users)) + " users in list")

	return users


def getDescriptions(credentials_list, users_data, directory):
	
	if len(users_data) is 0:
		print('Complete')
		return 

	
	
	for credential in credentials_list:

		users = users_data[0:100]

		credentials = Twython(app_key=credential[0],
		    	app_secret=credential[1],
		    	oauth_token=credential[2],
		    	oauth_token_secret=credential[3], oauth_version=1)

		data = credentials.lookup_user(screen_name = users)

		for dat in data:
			profile = dat
			handle = str(profile['id'])
			time_zone = str(profile['time_zone'])
			screen_name = profile['screen_name']
	        #utc_offset = profile['utc_offset']
			description = profile['description'].replace("\t", " ")

			with codecs.open(directory[:-4] + "_IDs.csv", 'a', encoding='utf-8') as out:
				out.write(u''+ screen_name + '\t' + handle +'\n')



		users_data = users_data[101:]
		
	getDescriptions(credentials_list, users_data, directory)


def main():
	ak1, ask1, at1, ats1 = 
	ak2, ask2, at2, ats2 =
	ak3, ask3, at3, ats3 = 
    
	credentials_list = [ [ak1, ask1, at1, ats1], [ak2, ask2, at2, ats2], [ak3, ask3, at3, ats3] ]

	getDescriptions(credentials_list,readData("usernames.csv"), "usernames.csv")





main()



