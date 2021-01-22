import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import re
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter URL: ')
    #if len(address) < 1: break

    parms = dict()
   # parms['address'] = address
 
    url = address + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('.//count')
    print('The amount of count tags', len(results))

    break

