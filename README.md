# Project Media Insights
Developed by Darren Colby and essup Jong

Get insights into your user inteaction on YouTube. This tool enables you to
quickly see trends in comments and sentiments in your videos. The time series 
predictions are powered by Prophet, a time series library developed at Facebook,
that separately models day, month, year, and autoregression components using 
Bayesian Markov Chain Monte Carlo. Sentiment classification is based on VADER
using preprocessed text. When conducting sentiment classification, the program 
removes emojis, newlines, tabs, carriage returns, punctuation, and numbers before
translating any foreign text to English and correcting misspelled words. Finally,
this program allows you to visualize the similarity of competitor videos by using
the cosine similarity of the GloVe embeddings of their transcripts.

## Features
-Automate video uploads
-Can be run by double clicking a single file
-Automatic translation of comments and transcripts to English
-Automatic spelling correction
-Cosine similarities calculated based on GloVe embeddings
-Change the forecast period with a slider
-Uploads secured by OAuth

## Usage
### Using the automate.sh script
```Python
cd media_insights
automate.sh
```
Alternatively run by double clicking on automate.sh

### Makefile
```Shell
cd media_insights
make
```

## Demo Version
In addition to running the program locally, you can interact with a live version at https://mediainsights.streamlit.app
