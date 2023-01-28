#!/usr/bin/env python

from datetime import datetime

import Tasmota
import Config

if __name__ == "__main__":  
    #print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " START #####")
    try:
        conf = Config.read()
        tempon = int(conf["temp_on"])
        tempoff = int(conf["temp_off"])
        
        #connect interfaces
        Tasmota.connect(conf["mqtt_broker"], conf["mqtt_port"], conf["mqtt_user"], conf["mqtt_password"])

        #read Tasmota
        result = Tasmota.get(conf["mqtt_name"], "8", ["StatusSNS_SI7021_Temperature"])
        actualtemp = int(result["StatusSNS_SI7021_Temperature"])
        
        if actualtemp >= tempon:
            Tasmota.on(conf["mqtt_name"])
        if actualtemp <= tempoff:
            Tasmota.off(conf["mqtt_name"])

        print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " actualtemp: " + str(actualtemp))  

        #print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " END #####")
        
    except Exception as ex:
        print ("ERROR: ", ex) 
