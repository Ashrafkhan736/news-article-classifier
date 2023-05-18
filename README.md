# news-article-classifier

This application predicts the category of news article

## File structure

```
.
├── ai_model
│   ├── bbc-news-data.csv
│   ├── category_predictor.sav
│   └── news_category_classification.ipynb
├── app
│   ├── **init**.py
│   ├── stop_words.py
│   ├── templates
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── all_result.html
│   │   ├── base.html
│   │   ├── index.html
│   │   └── result.html
│   └── utils.py
├── README.md
├── requirements.txt
└── startup.py
```

`ai_model` repo store the model, data and .ipynb file to generating the ML model.

`app` repo store all the logic for server

`__init__.py` file store routes for application

`utils.py` file store spcraping, preprocessing and prediction logic

`startup` file give acess to flask `app` object in ropt repo.

## For cloud deployment

visit https://news-article-classifier-wiay.onrender.com/

---

## Deployment

`deployment` branch stroes file runing on cloud on `render` cloud platform

To deploy flask app on render create a free account

link the github repo on cloud platform

save MONGO_URI as enviroment variable on cloud platform

```
# provide this command  as excutable in cloud platform
gunicorn --bind=0.0.0.0 --timeout 600 startup:app
```

Then start the webserver

---

## For local run

### Go to `local_run` branch

## Create .env file in ./app/ repo

store following key value pair in .env file

MONGO_URI = < mongo database uri >

for either cloud database or local mongodb database

Example

```
MONGO_URI = "mongodb+...."
```

## Strat web server locally

give excutable acess to run.sh

```
chmod 700 run.sh
./run.sh
```

Run run.sh file
