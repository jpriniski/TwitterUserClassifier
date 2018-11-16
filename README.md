# Twitter User Classifier

The Twitter User Classifier is a set of scripts and methods that collect and analyze Twitter user data. This repository describes a Twitter user sampling method that filters institutional users (e.g., media and journalism professionals) from datasets of ordinary Twitter users. 

More details on the methods are found in:

K. Hazel Kwon, J. Hunter Priniski, & Monica Chadha (2018). Disentangling user samples: A machine learning approach to proxy-population mismatch in Twitter research. Communication Methods and Measures. Online before print:  http://www.tandfonline.com/doi/full/10.1080/19312458.2018.1430755 

CITATION: Please cite the journal publication above when using this repository.

Files: 
1. 18CMM: The method paper (published)
2. ManuallyLabeled_All.csv : The csv file includes 8945 user profile description that human coders labeled as either general public user profile (1) or not. The profile texts were collected using StreamAPI in the context of Mesa Shooting in Metro-Phoenix area (2015); Boston Bombing (2013); Bruessls Airport Bombing (2016); Quebect Mosque Shooting (2017); and the random sampling of profile texts in 2017. 

Dependencies:
1. Twython 
2. Scikit-learn : bag-of-words model, Random Forest Model.
3. Natural Language Toolkit: Snowball stemmer, English Stop-words dictionary


Scripts:

1. get_twitter_user_descriptions.py : collect information on up to 300 Twitter User Descriptions outputted to a .csv file.

2. get_user_information.py: General version of getTwitterUserDescriptions.py: collect more data than just descriptions and time zone information (which is the functionality of get_Twitter_User_Descriptions.py). 

3. account_classification.py: Classes and methods that implement supervised machine learning protocols that classify Twitter profiles as whether a profile is a general public user account or not (such as a business', public figure's, news reporter's, promotional accounts). For references on how to use this code, see below.  Also, references the example.txt document.   
                          
4.  concreteness.py. To understand the concreteness of a tweet (how concrete of language a user employs in their tweets gives us  a proximal coefficient, which informs us about how close the tweeter is to the event).  This function will calculate the average concreteness rating of a sentence (total concreteness score divided by the amount of concrete words). The concreteness ratings are taken from Marc Brysbaert, Amy Beth Warriner, and  Victor Kuperman's work (2014) found here (http://crr.ugent.be/papers/Brysbaert_Warriner_Kuperman_BRM_Concreteness_ratings.pdf)

Additional information:

To use account_classification.py, the data *must* be structured as bellow.

training data:

user_ID'\t'Description'\t'Personal
*some id*'\t'*some description*'\t'1
*some id*'\t'*some description*'\t'0
*some id*'\t'*some description*'\t'1
  ...
  
testing data:

user_ID'\t'Description         
*some id*'\t'*some description*   
*some id*'\t'*some description*   
*some id*'\t'*some description*  
  
Where 1 = general public users, 0 = others (mainly media professional, institutional, and promotional accounts).  user_ID can either be a string or an int data type. Furthermore, both the training and testing data should be saved as a .txt file with a tab ('\t') separator. 
**Make sure all data is saved in utf-8 format. To encode entire data frames we recommend using R. 
