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

https://predictor-dot-micro-services-378415.appspot.com

### Example request

```
{
  "news": [
    "Equities Tech stock retreat leads Wall Street indices lower Bank stocks steady and bond markets calm Private credit Big debt investors dealt blow in mattress maker bankruptcy ruling Serta Simmons court decision is milestone in ‘creditor-on-creditor violence’ litigation FT live news Live news updates from March 28: Dimon to be deposed in Epstein lawsuits, Alibaba to split into six Apple Inc Apple launches ‘buy now, pay later’ service in the US Tech giant debuts rival to companies such as Klarna and Affirm after delays LexHigh yield bonds Junk bond market: securities market may replace bank lending, uneasily Premium content After a roaring start to the year, a downturn in March shows that risk appetites are clearly inhibited Liontrust Liontrust directors quit over chair’s 12-year tenure Corporate governance worries prompted two executives to leave the asset manager’s board",
	"Equities US equities rise as ‘fear trades’ fade in broad-based rally Wall Street joins global stock advance over waning concerns about banking turmoil FT live news Live news updates from March 29: UBS names Sergio Ermotti CEO, Pope Francis hospitalised LexFinancial services Jefferies: direct lenders chip away at investment bank franchise Premium content More companies are getting their loans from private credit funds The FT ViewThe editorial board How to avoid a developing world debt crisis Surge in China’s rescue lending shows need for co-operation on restructuring LexOil & Gas industry US natural gas prices: déjà vu all over again Premium content Investors should retain their scepticism instead of believing prophecies of secular tailwinds Digital currencies What NFT mania can tell us about market bubbles Extracting the fun from non-fungible Binance Binance hid extensive links to China for several years Company documents show crypto exchange relied on country long after it said it had left in 2017",
	"Wall Street stocks notch back-to-back gains boosted by tech Investors refocus on path for US rates after weeks of bank turmoil FT live news Live news updates from March 30: Donald Trump indicted, Finland cleared to join Nato US financial regulation Biden calls for tougher rules for large regional banks Push to unwind Trump-era rule changes comes as policymakers consider long-term response to recent crisis LexMSCI Inc MSCI/ESG ratings: grade deflation should pump box tickers’ profits Premium content The lack of universal standards is a problem, though Gillian Tett Prepare for a multipolar currency world The US dollar still dominates debt markets, but some niche-sounding data suggests things could be set to shift LexGilts UK government bonds: short end offers investors a gilty pleasure Premium content Chances are that UK interest rates have peaked"],
  "stock": [32.394, 32.717, 32.859]
}
```
