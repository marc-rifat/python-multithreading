import logging
import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def open_url(url):
    options = ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('window-size=2560x1440')
    browser = webdriver.Chrome(options=options)

    browser.get(url)
    logging.info(f'opening {browser.current_url}')
    browser.quit()


urls = [
    'https://www.google.com/',
    'https://www.youtube.com/',
    'https://www.amazon.com/',
    'https://www.udemy.com/',
    'https://github.com/',
    'https://www.monster.com/',
    'https://www.careerbuilder.com/',
    'https://www.dice.com/',
    'https://www.cnbc.com/'
]

threads = [threading.Thread(target=open_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
