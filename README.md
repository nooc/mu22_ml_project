# Text sentiment vs stock market :expressionless:

A small ML school assignment.

## About

This is a rough idea for a service that predicts the next day outcome for a stoc based on previous days sentiment analysis of financial news texts.

The selected models were logistic regression for sentiment analysis and NN for the final prediction.

Some features:

* Test accuracy and training time for *LogisticRegression*, *LinearSVC* and neural net (*SentimentNN*).
* The ***sci-kit*** models are optimized and fitted using the experimental *HalvingGridSearchCV*.
* Use exported models in REST backend to produce predictions.

These classifier models were chosen based mostly on rule-of-thumb. These are generally used in classification, however trial and error will usually and eventually dictate what model is best for the actual data set.

## Data processing

Data resides in datasets folder.

### build_sentiment.ipynb

Uses data from:

* https://www.kaggle.com/datasets/ankurzing/aspect-based-sentiment-analysis-for-financial-news
* https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news
* https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis

These are text sentiment sources and are merged into one data-frame with features and score.

### render_index.ipynb

Reads in some selected NASDAQ stock from a kaggle dataset and fixes gaps in the data for continuous data. They are merged into one dataframe.

### train_sentiment.ipynb

Train, test accuracy and show training time for selected classifiers. Uses the output from build_sentiment.
Models are exported.

### render_news.ipynb

Compile a list of financial news for predictor training.

### train_predictor.ipynb

Train predictor using selected sentiment model, render_news output and render_index output.
Model is exported.

## REST servcie

### Framework

The servcie uses FastAPI and is deployed on Google App Engine Python environment.

This service is deployed at (with Swagger docs):

https://predictor.micro-services-378415.appspot.com
