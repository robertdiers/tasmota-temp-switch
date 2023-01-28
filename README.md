# tasmota-temp-switch
Tasmota turns on power at a defined temperature

### Defaults
plaese check properties in tasmota-temp-switch.ini file, could be overridden by Docker env variables

### Docker usage

environment variables:

MQTT_BROKER (default: 192.168.1.7)

MQTT_PORT (default: 1883)

MQTT_USER (default: admin)

MQTT_PASSWORD (default: password)

MQTT_NAME (default: tasmota_serverraum)

TEMP_ON (default: 33)

TEMP_OFF (default: 30)

docker run -d --restart always -e MQTT_PASSWORD=password --name tasmotatempswitch ghcr.io/robertdiers/tasmota-temp-switch:1.0

### create Docker image for your architecture
./image.sh


