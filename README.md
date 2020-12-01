# Chat API

This chat API stores messages in MongoDB as well as extracting the sentiment from chat messages. The API has several endpoints which are the following:
1. Welcome endpoint
Welcome to the API. __welcome()__
2. User endpoints
To create and save a user into the database. __insert_u(username)__
3. Chat endpoints
- To create a chat with users and save it into the database. __insert_ch(chatname)__
- To add a new user  to an existing chat. __add_user(chat_id)__
4. Message endpoints
- To add a message to a conversation __insert_messa(chat_id, user_id, text)__
- To list all the messages from a chat __get_mess(chat_id)__

## Sentiment Analysis
From one chat takes all the messages and performs a sentiment analysis