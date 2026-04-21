"""
pandasHW.py
====================================
This is a web scraper that will return information from weather reports and format it using pandas

| Author: Abraham Fisher
| Date: 2026 April 18
"""
import requests
import regex as re
import re
import pandas as pd
import numpy as np

def main():

    response = requests.get("https://forecast.weather.gov/obslocal.php?warnzone=IAZ031&local_place=Sioux%20City%20IA&zoneid=CDT&offset=18000")
    response.raise_for_status() # check for errors
    myhtml = response.text;

    print(f'Total Characters: {len(myhtml)}')

    # Checks odd and even rows for the 4th column which holds the number for the temp
    odd_temps = re.findall(r'<tr class="odd">\s*<td class="obs-link">.*?</td><td class="time">.*?</td><td class="wx">.*?</td><td>(\d+)</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td></tr>', myhtml);
    even_temps = re.findall(r'<tr class="even">\s*<td class="obs-link">.*?</td><td class="time">.*?</td><td class="wx">.*?</td><td>(\d+)</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td></tr>', myhtml);
    #changes each value from a string to an int
    odd_temps = [int(t) for t in odd_temps]
    even_temps = [int(t) for t in even_temps]
    #combines the lists
    temps = odd_temps + even_temps;

    print(f'Total Temps: {temps}')

if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    main();

