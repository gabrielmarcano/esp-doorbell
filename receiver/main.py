import time
import binascii

import espnow
import network
import urequests

WEBHOOK_URL = "http://homeassistant:8123/api/webhook/doorbell"
WIFI_SSID = "SSID"
WIFI_PASSWORD = "PASSWORD"

def wifi_reset():   # Reset wifi to AP_IF off, STA_IF on and disconnected
  sta = network.WLAN(network.WLAN.IF_STA); sta.active(False)
  ap = network.WLAN(network.WLAN.IF_AP); ap.active(False)
  sta.active(True)
  while not sta.active():
      time.sleep(0.1)
  sta.disconnect()   # For ESP8266
  while sta.isconnected():
      time.sleep(0.1)
  return sta, ap

sta, ap = wifi_reset()

sta.connect(WIFI_SSID, WIFI_PASSWORD)
while not sta.isconnected():  # Wait until connected...
    time.sleep(0.1)
sta.config(pm=sta.PM_NONE)  # ..then disable power saving

print("Proxy running on channel:", sta.config("channel"))

ap.active(True) # ESP8266 peers must send messages to this AP_IF interface

mac_address_str = binascii.hexlify(ap.config("mac"), ":").decode().upper()
print("MAC address:", mac_address_str)

e = espnow.ESPNow()
e.active(True)

print("Listening for ESP-NOW messages...")

# Always listen for a "ring" sent within a ESP-NOW packet
while True:
    host, msg = e.recv()
    if msg == b"ring":
        print("Doorbell signal received! Sending webhook...")
        
        try:
            r = urequests.post(WEBHOOK_URL)
            print("Webhook sent! Response:", r.status_code)
            r.close()
        except Exception as ex:
            print(f"HTTP error:", ex)