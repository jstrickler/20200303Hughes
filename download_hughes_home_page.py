#!/usr/bin/env python
import requests
from subprocess import run

HUGHES_URL = 'https://www.hughes.com'

try:
    response = requests.get(HUGHES_URL)
except requests.HTTPError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:
        print(response.content.decode())

PDF_URL = "https://www.hughes.com/signage/sites/hughes.com/files/2020-03/Hughes%209502%20External%20Antenna.pdf"


try:
    response = requests.get(PDF_URL)
except requests.HTTPError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:
        pdf_name = 'hughes.pdf'
        pdf_content = response.content
        with open(pdf_name, 'wb') as hughes_out:
            hughes_out.write(pdf_content)
        run([pdf_name], shell=True)
