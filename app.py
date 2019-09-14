import pandas as pd
import numpy as np
# from itertools import islice
from flask import Flask, render_template, request
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json

from emoji_sentiment_analysis import get_keywords

app = Flask(__name__)

url = ''

@app.route("/", methods=["GET"])
def hello():
  return "Hello World"

@app.route("/form", methods=["POST"])
def bye():
  return "Bye World!"

# @app.route("/", methods=["GET"])
# def get_form():
#     return render_template("form.html")

# @app.route("/form", methods=["POST"])
# def post_form():
# 	return render_template("result.html")


if __name__ == '__main__':
    app.run()