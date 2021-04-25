# web-scraping-challenge

Mission to mars project has three files:

1. mission_to_mars.ipynb : This file does the web scrapping on different websites to
   capture the  news on Mars, Mars facts, Images and other details

2. scrape_mars.py : This file has thescrape method which calls the same functions as called in the .ipynb.
   This scrape method will be called by the Flask application and the data will be fed to the index.html file.

3. app.py files, has the flask app. This will call the scrape method  of scrape_mars.py and populate data to index.html and will render the html page.

4. The index.html page displays the data that was scrapped from the different websites.