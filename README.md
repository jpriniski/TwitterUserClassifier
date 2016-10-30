# TwitterClassification

TwitterClassification is a set of scripts and methods that collect and analyze Twitter user data.  It was created for Hazel Kwon's research in psychological concreteness. 


Dependicies:
1. Twython 
2. Scikit-learn : bag-of-words model, Random Forest Model.
3. Natural Language Toolkit: Snowball stemmer, English Stop-words dictionary


Scripts:

1. get_twitter_user_descriptions.py : collect information on up to 300 Twitter User Descriptions outputted to a .csv file.

2. get_user_information.py: General version of getTwitterUserDescriptions.py: collect more data than just descriptions and timezone information (which is the functionality of getTwitterUserDescriptions.py). 

3. account_classification.py: Classes and methods that implement supervised machine learning protocols that classify Twitter profiles as a personal (or layman's) account or a non-personal (such as a business', public figure's, news reporter's) account. For references on how to use this code, see below.  Also, references the example.txt document.   
                          
4.  concreteness.py. To understand the concreteness of a tweet (how concrete of language a user employs in their tweets gives us  a proximal coefficient, which informs us about how close the tweeter is to the event).  This function will calculate the average concreteness rating of a sentence (total concreteness score divided by the amount of concrete words). The concreteness ratings are taken from Marc Brysbaert, Amy Beth Warriner, and  Victor Kuperman's work found here (http://crr.ugent.be/papers/Brysbaert_Warriner_Kuperman_BRM_Concreteness_ratings.pdf)

Additional information:

To use account_classification.py, the data *must* be structured as bellow.
training data:
user_ID           Description         Personal
*some id*         *some description*   1
*some id*         *some description*   0
*some id*         *some description*   1
  ...
  
testing data:
user_ID           Description         
*some id*         *some description*   
*some id*         *some description*   
*some id*         *some description*  
  
Where 1 = personal, 0 = nonpersonal.  user_ID can either be a string or an int data type. Furthermore, both the training and testing data should be saved as a .txt file with a tab ('\t') separator. 
**Make sure all data is saved in utf-8 format. To encode entire data frames we recommend using R. 
 


  
  
