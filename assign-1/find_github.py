# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def main():
    # Get paper title
    if len(sys.argv)!=2:
        print("Usage: py main.py paper_title")
        sys.exit(1)
    paperTitle = sys.argv[1]

    # Initilize Chrome Driver
    # driver = uc.Chrome(headless=True,use_subprocess=False)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')        #remove this for easy debbuing on your laptop /pc
    chrome_options.add_argument('--no-sandbox')                             
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10) # seconds

    # Fetch bing.com page
    driver.get('https://bing.com')

    # Find the seach box
    search_box = driver.find_element(By.NAME, "q")
    # print(search_box.get_attribute('outerHTML'))

    # Add the title into the textarea
    search_box.clear()
    search_box.send_keys(paperTitle + " github") # enter your name in the search box
    # print(search_box.get_attribute('value'))

    # Send search request
    search_box.submit() # submit the search

    # with open("index.html",'w', encoding='utf-8') as f:
    #     f.write(driver.page_source)
    # resultNum = driver.find_elements(By.XPATH, "//*[@id='b_tween']/span")
    # print(resultNum[0].text)
    try:
        firstResult = driver.find_element(By.XPATH,"//h2//a")
        link = firstResult.get_attribute('href')
        if ("github" in link) and (~("topics" in link)):
            print("Github repo of this paper is: "+link)
        else:
            print("Not found the github repo for this paper")
    except NoSuchElementException:
        print("Not found the github repo for this paper")

    driver.quit()

if __name__ == '__main__':
    main()