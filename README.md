# TwitterGatekeeping
Python code that cleans, collects, and prepares Twitter user data for Dr. Hazel Kwon's Audience Gatekeeping research project. 
The code is built upon the Twython package and uses scikit-learn for Machine Learning and the Natural Language Toolkit for 
its corpus on stop words and implementation of its Snowball word stemmer algorithim. 


A list of files and their functionalities:

1. getTwitterUserDescriptions.py : collect information on up to 300 Twitter User Descriptions outputed to a .csv file.
2. getUserInformation.py: General version of getTwitterUserDescriptions.py: collect more data than just descriptions and timezone information (which is the functionality of getTwitterUserDescriptions.py). 
3. [**** UNDER CONSTRUCTION ****] accountClassification.py: Classes and methods that will implement supervised machine learning protocols that classify Twitter profiles as a personal (or layman's) account or a nonpersonal (such as a business', public figure's, news reporter's) account.  
                          

