"""
pandasHW.py
====================================
This is a web scraper that will return information from weather reports and format it using pandas

| Author: Abraham Fisher
| Date: 2026 April 18
"""
import requests
import re
import pandas as pd
import numpy as np

def main():

    response = requests.get("https://forecast.weather.gov/obslocal.php?warnzone=IAZ031&local_place=Sioux%20City%20IA&zoneid=CDT&offset=18000")
    response.raise_for_status() # check for errors
    myhtml = response.text;

if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    main();

