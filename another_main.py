import requests  #will get the source code and store it as a string
import selectorlib   #extract info from all the code source, for exmp from html of a website
from datetime import datetime
import time

URL = "https://programmer100.pythonanywhere.com/"

def scrape(url): #this will bring us all the code from a certain url, from the html to be specific!
    """ scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml_another")
    value = extractor.extract(source)["tours"]
    return value

def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt_1","a") as file:
        line = f"{now},{extracted}\n"
        file.write(line)

if __name__ == "__main__":
    # while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
        # time.sleep(2)  # every 2 seconds the code will run