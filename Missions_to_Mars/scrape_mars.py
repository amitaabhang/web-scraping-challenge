from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    
    mars_data = {}
    
    #NASA Mars News

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    mars_data['news_title'] = soup.find_all('div', class_='content_title')[0].text
    mars_data['news_p'] = soup.find_all('div', class_='article_teaser_body')[0].text
    
    #JPL Mars Space Images - Featured Image
    nasa_url = 'https://spaceimages-mars.com'
    browser.visit(nasa_url)
    nasa_html = browser.html
    nasa_soup=BeautifulSoup(nasa_html,'html.parser')
    
    nasa_div = nasa_soup.find('div', class_='floating_text_area')

    if('FEATURED IMAGE' in nasa_div.text):
        nasa_img = nasa_div.find('a')['href']
        featured_image_url = nasa_url +'/'+ nasa_img
        mars_data['featured_image_url'] = featured_image_url
    
    # Mars Facts
    mars_url = 'https://galaxyfacts-mars.com/'
    mars_facts = pd.read_html(mars_url)
    mars_df = mars_facts[0]
    mars_df.columns = ['Description','Mars','Earth']
    mars_df = mars_df[1:]
    mars_html = mars_df.to_html()
    mars_html = mars_html.replace("\n","")
    mars_html
    mars_data['mars_html']= mars_html
    
    # Mars Hemispheres
    hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(hemisphere_url)
    hemisphere_html = browser.html
    hemisphere_soup=BeautifulSoup(hemisphere_html,'html.parser')
    all_div = hemisphere_soup.find_all('div', class_='description')
    hemisphere_url_lst=[]
    hemisphere_titles_lst=[]

    for div in all_div:
        hemisphere_url_lst.append(hemisphere_url+div.find('a')['href'])
        hemisphere_titles_lst.append(div.find('a').text)
    hemisphere_img_lst=[]
    
    for url in hemisphere_url_lst:
        browser.visit(url)
        img_html = browser.html
        img_soup=BeautifulSoup(img_html,'html.parser')
        all_div = img_soup.find_all('div', class_='downloads')[0]
        hemisphere_img_lst.append(hemisphere_url+all_div.find('a')['href'])
    
    hemisphere_image_urls  = [{'Title':hemisphere_titles_lst[0],'Image URL': hemisphere_img_lst[0]},
            {'Title':hemisphere_titles_lst[1],'Image URL': hemisphere_img_lst[1]},
            {'Title':hemisphere_titles_lst[2],'Image URL': hemisphere_img_lst[2]},
            {'Title':hemisphere_titles_lst[3],'Image URL': hemisphere_img_lst[3]}]
    
    mars_data['hemisphere_List'] = hemisphere_image_urls
    
        
    return mars_data


print(scrape())