# Chatbox for website
import requests
import json
import os

openai_api_key = # put yout api key here
if openai_api_key is None:
    raise ValueError("OpenAI API key is not set in environment variables.")

