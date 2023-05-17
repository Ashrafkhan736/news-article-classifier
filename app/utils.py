import joblib
import requests
import pandas as pd
from sklearn.pipeline import Pipeline
import warnings
from bs4 import BeautifulSoup
from lxml import html
import re
from string import punctuation
from .stop_words import stop_words

punctuation = punctuation + "\n" + "—" + "“" + "," + "”" + "‘" + "-" + "’"
warnings.filterwarnings("ignore")

model: Pipeline = joblib.load("./ai_model/category_predictor.sav")


def predict(text):
    y_pred = model.predict(pd.Series(text))[0]
    return y_pred


def preprocessing(text):
    # removing non alphanumeric characters
    text = re.sub(r"[^A-Z a-z 0-9]", "", text)

    # removing punctuations
    text = "".join(char for char in text if char not in punctuation)

    # removing trailing whitespaces again
    text = re.sub(r" +", " ", text)

    # removing the stopword
    text = " ".join(word for word in text.split() if word not in stop_words)

    return text.lower()


def scrap_url(url):
    response = requests.get(url=url)
    # soup = BeautifulSoup(html,'lxml')
    if response.status_code == 200:
        tree = html.fromstring(response.content)
        elements = tree.xpath("//p//text()")
        text = " ".join(elements)
        if text != "":
            return predict(preprocessing(text)), text
    raise Exception
