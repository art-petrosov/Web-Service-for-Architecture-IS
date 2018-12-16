# -*- coding: utf-8 -*-
# Module render_template for HTML-report
from flask import render_template
# Library requests to request data from an open data source site
from requests import *
# Library re for parsing data using regular expressions 
import re
# Import application
from app import app
# Decorator
@app.route('/')
# Decorator
@app.route('/index')
# Function with trigger parameters of weather temperature, wind speed and pressure
def index(temp_trig = -15, wind_speed_trig = 15, press_lower_trig = 998):

    # We have that list of stations (airports). Variant 11
    port_list = ['LICJ', 'LSZS', 'ESNZ', 'EGDR', 'KOKC', 'HTKA', 'KFXE', 'CYCP', 'GMFM', 'KCWA', 'KMCF', 'LTBS', 
                'MMUN', 'LFYR', 'KSNK', 'KORS', 'FAPN', 'CWII', 'NCMK', 'KDSV', 'KAGR', 'WBGG', 'EGKA', 'LEHC',
                'PAGH', 'PTSA', 'CYCD', 'CYYJ', 'K3AU', 'CWCJ']

    # Here we will store our reports for each station
    reports = []

    # Using cycle make a report for each station and add to list 'reports'
    for port in port_list:

        # Make an URL-address for station
        url = 'http://tgftp.nws.noaa.gov/data/observations/metar/decoded/' + port + '.TXT'

        # Get the data
        port_data = get(url).text.strip()

        # We bypass the exception when there is no data on temperature / wind speed / pressure
        try:
            # Using regular expessions find a temperature value of the station
            temp = re.search(r'[-]?(?:\d{1,2}|\d{1,2}\.\d) C', port_data).group(0)
            # Tranform value from string to number and match with trigger value
            if float(temp.split()[0]) < temp_trig:
                # Create the variable for report text
                output = 'Look out! temperature in airport {} area below {} C !\n'.format(port, temp_trig)
            else:
                output = 'Temperature in airport {} area is OK!\n'.format(port)
        except:
            output = 'Sorry, temperature data is not available from that source\n'
            
        try:
            wind_speed = re.search(r'(?:\d{1,2} MPH|Calm:0)', port_data).group(0)
            if wind_speed == 'Calm:0':
                output += 'Wind speed in airport {} area is OK!\n'.format(port)
            elif int(wind_speed.split()[0]) < wind_speed_trig:
                output += 'Wind speed in airport {} area is OK!\n'.format(port)
            else:
                output += 'Look out! Wind speed in airport {} area over {} MPH!\n'.format(port, wind_speed_trig)
        except:
            output += 'Sorry, wind speed data is not available from that source\n'
            
        try:
            press = re.search(r'\d{3,4} hPa', port_data).group(0)
            if int(press.split()[0]) < press_lower_trig:
                output += 'Look out! Pressure in airport {} area below {} hPa!\n'.format(port, press_lower_trig)
            else:
                output += 'Pressure in airport {} area is OK!\n'.format(port)
        except:
            output += 'Sorry, pressure data is not available from that source\n'.format(port)
        # Add report of each station to list 'reports' by the certain way
        reports += [{'airport': {'station': port}, 'text': output}]
    # Match element values with report template
    return render_template('index.html', reports=reports)

app.run('83.220.168.38', port=5028)
