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

    print(f'Total Characters: {len(myhtml)}')

    # Checks odd and even rows for the 4th column which holds the number for the temp
    values = r'<td>(?P<Temp>\d+)</td>[\s\r\n]+<td>(?P<Dew>\d+)</td>[\s\r\n]+<td>(?P<Humidity>\d+)</td>[\s\r\n]+'
    matches = re.finditer(values, myhtml)

    data = []

    for match in matches:
        row = {
            "Temp": int(match.group("Temp")),
            "Dew": int(match.group("Dew")),
            "Humidity": int(match.group("Humidity"))
        }
        data.append(row)

    df = pd.DataFrame(data)

    print(df)

if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    main();

