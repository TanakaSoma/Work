import pandas as pd
import requests
import io

# URL
url = "https://heroku-copype.herokuapp.com/"
r = requests.get(url).content
print(r)
