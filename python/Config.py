#!/usr/bin/env python

import configparser
import os
from datetime import datetime

#read config
config = configparser.ConfigParser()

def read():
    try:
        #read config
        config.read('tasmota-temp-switch.ini')

        values = {}

        #read config and default values
        values["mqtt_broker"] = config['MqttSection']['mqtt_broker']
        values["mqtt_port"] = int(config['MqttSection']['mqtt_port'])
        values["mqtt_user"] = config['MqttSection']['mqtt_user']
        values["mqtt_password"] = config['MqttSection']['mqtt_password']
        values["mqtt_name"] = config['MqttSection']['mqtt_name']
        if os.getenv('MQTT_BROKER','None') != 'None':
            values["mqtt_broker"] = os.getenv('MQTT_BROKER')
            #print ("using env: MQTT_BROKER")
        if os.getenv('MQTT_PORT','None') != 'None':
            values["mqtt_port"] = int(os.getenv('MQTT_PORT'))
            #print ("using env: MQTT_PORT")
        if os.getenv('MQTT_USER','None') != 'None':
            values["mqtt_user"] = os.getenv('MQTT_USER')
            #print ("using env: MQTT_USER")
        if os.getenv('MQTT_PASSWORD','None') != 'None':
            values["mqtt_password"] = os.getenv('MQTT_PASSWORD')
            #print ("using env: MQTT_PASSWORD")
        if os.getenv('MQTT_NAME','None') != 'None':
            values["mqtt_name"] = os.getenv('MQTT_NAME')
            #print ("using env: MQTT_NAME")
        
        values["temp_on"] = config['TempSection']['temp_on']
        values["temp_off"] = int(config['TempSection']['temp_off'])
        if os.getenv('TEMP_ON','None') != 'None':
            values["temp_on"] = os.getenv('TEMP_ON')
            #print ("using env: TEMP_ON")
        if os.getenv('TEMP_OFF','None') != 'None':
            values["temp_off"] = int(os.getenv('TEMP_OFF'))
            #print ("using env: TEMP_OFF")
        
        #print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " config: ", values)

        return values
    except Exception as ex:
        print ("ERROR Config: ", ex) 
