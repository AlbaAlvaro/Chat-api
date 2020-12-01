
from pymongo import MongoClient
from bson.objectid import ObjectId

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")

import regex as re

client = MongoClient()
db = client.get_database("api_chat")


# User
# Insert a user into the database users
def insert_user(username):
    curs=db.users.insert_one(username)
    return f"The user {curs.inserted_id} was added to users"


# Chat
# Insert new chat
def insert_chat(chatname):
    curs=db.chats.insert_one(chatname)
    return f"The chat {curs.inserted_id} was added to chats"


# Messages
# Add new message to a chat
def insert_message(chat_id, user_id, text):
    curs=db.messages.insert_one({"message":text, "chat_id": chat_id, "user_id":user_id})
    return {"_id": curs.inserted_id}

# Check if user is part of the chat before adding message
def insert_messag(chat_id, user_id, text):
    users=str(list(db.chats.find({"_id":ObjectId(chat_id)},{"list of users":1, "_id":0})))
    # use regex to see if the user is in the string
    pattern=user_id
    string=users       
    if re.search(pattern,string):
        curs=db.messages.insert_one({"message":text, "chat_id": chat_id, "user_id":user_id})
        return f"The messaje {text} was added to chat {curs.inserted_id}"
    else:
        return f"This user ({user_id}) is not in this chat ({chat_id})"

#  Get all messages from a chat
def get_message(chat_id, text):
    curs=db.messages.find({"chat_id":chat_id}, {"message.text" : 1})
    return list(curs)


# Sentiment analysis
sia=SentimentIntensityAnalyzer()
def sentiment(chat_id):
    curs=list(db.messages.find({"_id": ObjectId(chat_id)}, {"message.text": 1}))
    print(curs)
    # sia_chat=sia.polarity_scores(curs)
    # return list(sia_chat)