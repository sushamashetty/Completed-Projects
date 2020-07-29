#!/usr/bin/env python

import requests
import time
from pyfingerprint.pyfingerprint import PyFingerprint


## Tests Finger
##
URL = "http://192.168.0.101/attend/markAtten.php"
## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to verify finger
try:
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)

    ## Checks if finger is already enrolled
    result = f.searchTemplate()
    positionNumber = result[0]

    if ( positionNumber >= 0 ):
        PARAMS = {'studid':positionNumber}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        resp=data['indus'][0]['mesg']
        print("Response:"+resp)
        exit(0)

    

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
