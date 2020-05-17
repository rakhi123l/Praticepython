# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:14:26 2020

@author: admin
"""
from collections import defaultdict
from collections import Counter

users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []
    
for i, j in friendships:
# this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i
    
def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"]) # length of friend_ids list
    total_connections = sum(number_of_friends(user) for user in users) 

def friends_of_friend_ids_bad(user):
# "foaf" is short for "friend of a friend"
    return [foaf["id"]
    for friend in user["friends"] # for each of user's friends
    for foaf in friend["friends"]] 
    
print (friends_of_friend_ids_bad(users[0]))


def data_scientists_who_like(target_interest):
    return [user_id for user_id, user_interest in interests if user_interest == target_interest]

print(data_scientists_who_like("Big Data"))


user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
#def most_common_interests_with(user):
#    return Counter(interested_user_id for interest in interests_by_user_id[user["id"]]
#                   for interested_user_id in user_ids_by_interest[interest]
#                   if interested_user_id != user["id"])
#    
#print(most_common_interests_with(users))



tweet	=	{"user"	:	"joelgrus",	
			"text"	:	"Data	Science	is	Awesome",
			"retweet_count"	:	100,
			"hashtags"	:["#data",	"#science",	"#datascience",	"#awesome",	"#yolo"] }
tweet_keys			=	tweet.keys()		
print(tweet.keys())
print(tweet.values())
print(tweet.items())

with open('testfile.txt','r') as myfile: 
    print(myfile)
    
    d= {}
        
    for	line in	myfile:			
            
        myfile=myfile.strip()
        myfile=myfile.lower()
            
        words=myfile.split(" ")
            
        for word in d:                        
            try:								
                d[word]	+=	1				
            except	KeyError:								
                d[word]	=	1
            
            
print(d[word])

with open('grading problem-hackker rank.txt','r') as myfile:
     
    d={}
    
    for line in myfile:
        line=line.strip()
        line=line.lower()
        words=line.split(" ")
        
        for word in words:
            try:								
                d[word]	+=	1				
            except	KeyError:								
                d[word]	=	1
print(d[word])
for key in list(d.keys()): 
    print(key, ":", d[key]) 