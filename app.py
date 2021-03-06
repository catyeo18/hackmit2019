import pandas as pd
import numpy as np
# from itertools import islice
from flask import Flask, render_template, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
from flask import send_from_directory
import os

from emoji_sentiment_analysis import get_emotion, get_keywords
from scrape_youtube_music import return_track 

app = Flask(__name__)
json = FlaskJSON(app)

# url = "https://youtube.com/playlist?list=RDCLAK5uy_kJWGcrtTC_zrbD6rKkBvOcht_vzijhX1A"

@app.route("/<emoji>")
def emoji_to_track(emoji):
	emotion = get_emotion(emoji)
	url = return_track(emotion)
	return json_response(url=url)
	# return render_template("results.html", emoji=emoji, url=url)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.route("/form", methods=["POST"])
# def post_form():
# 	return render_template("result.html")


if __name__ == '__main__':
    app.run()