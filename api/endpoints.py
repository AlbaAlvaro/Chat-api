from api.app import app
from flask import request, send_from_directory
from helpers.mongoConnection import insert_user, insert_chat, insert_message, insert_messag, get_message, sentiment
from bson import json_util
import os
from bson.objectid import ObjectId

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.get_database("api_chat")

# API endpoints
@app.route("/")
def welcome():
    return {"welcome": "Welcome to my API"}


# User endpoints
# Insert a user into the collection users
@app.route("/user/create/<username>")
def insert_u(username):
    return json_util.dumps(insert_user(dict(request.args)))


# Chat endpoints
# Insert a new chat into the collection chats
@app.route("/chat/create/<chatname>")
def insert_ch(chatname):
    users = request.args.getlist("user_id")
    result = {"chat name":chatname, "list of users":users}
    return json_util.dumps(insert_chat(result))

# Insert a new user to a chat
@app.route ("/chat/adduser/<chat_id>")
def add_user(chat_id):
    chat_id = ObjectId(chat_id)
    new_user = ObjectId(request.args.get("user_id"))
    db.chats.update({"_id":chat_id},{"$push":{"list of users": new_user}})
    return f"The user {new_user} was added to chat {chat_id}"


# Messages endpoints
# Add new message to a chat
@app.route("/messages/create/<chat_id>/<user_id>/<text>")
def insert_mess(chat_id, user_id, text):
    return json_util.dumps(insert_message(chat_id, user_id, dict(request.args)))

# Check if the user is in the chat before adding the message
@app.route("/messages/create/ifuser/<chat_id>/<user_id>/<text>")
def insert_messa(chat_id, user_id, text):
    return json_util.dumps(insert_messag(chat_id, user_id, dict(request.args)))

# Get all messages from a chat
@app.route("/chat/list/<chat_id>")
def get_mess(chat_id):
    return json_util.dumps(get_message(chat_id, dict(request.args)))


# Sentiment analysis
@app.route("/chat/sentiment/<chat_id>")
def sentiment_a(chat_id):
    return json_util.dumps(sentiment(dict(request.args)))