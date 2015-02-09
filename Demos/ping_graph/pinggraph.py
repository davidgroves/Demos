#!/usr/bin/env python3

import subprocess
import datetime
import xlsxwriter

# Written for OSX, so assumes OSX like ping output.
# We cannot use native methods, as ping requires root or system
# capabilities to use. ping binary on most unixes is setuid root.

# Mostly designed to demo xlsxwriter and show how we can produce
# manager friendly excel documents without much effort.

target = '8.8.8.8'
time=[]
rtt=[]

repeatcount = 100

for r in range(0,repeatcount):
    response = subprocess.check_output('ping -c1 ' + target, shell=True)
    responsestring = response.decode('ASCII')
    responselines = responsestring.split('\n')

    for line in responselines:
        if "time=" in line:
            rtt.append(float(line.split('=')[3].split()[0]))
            time.append(datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S.%f'))

workbook = xlsxwriter.Workbook('ping.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_row('A1', ['Time', 'RTT'])
worksheet.write_column('A2', time)
worksheet.write_column('B2', rtt)

chart1 = workbook.add_chart({'type': 'line'})

# Configure the first series.
chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$' + str(len(time) + 2),
    'values':     '=Sheet1!$B$2:$B$' + str(len(time) + 2)
})

worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
workbook.close()