from nltk.corpus import shakespeare
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np

DRIVER_PATH = '/Users/stephenhage/Downloads/chromedriver.exe'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://shakespeare.mit.edu/')


nltk.download('shakespeare')
shakespeare.xml('dream.xml')