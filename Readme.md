# Trip advisor analisis, and naive Bayes implementation

This project is a practice from review extracted from tripadvisor.

The code for scrapping the review was provided by Pedro Aguilar as part of class material

To run the scrapping code (Pedro Instructions):

### Scrapy-tripadvisor-reviews
Using scrapy to scrape tripadvisor in order to get users' reviews.

The code in this repository was used to scrape and gather data from tripadvisor about some brazilian cities attractions. The data were used to train a sentiment analysis classifier used in https://github.com/igorbpf/Twitter-Sentiment (https://twisentiment.herokuapp.com/). 

### Usage
In the project's root folder type:

scrapy crawl tripadvisor -o tripadvisor_reviews.csv

the reviews will be stored in a csv file named tripadvisor_reviews

## Jupyter notebook

* To view the analysis, run your jupyter server, and make sure thar the file to load is called tripadvisor.csv and is in the same folder as Class TripAdvisor.ipynb

* open Class TripAdvisor.ipynb

	* everythings is conteined in the notebook.