import network
import espnow
import esp
import time

CHANNEL = 3 # Receiver's channel
MAC_STRING = "AA:BB:CC:DD:EE:FF" # Receiver's MAC 

# peer in byte format = b"\xaa\xbb\xcc\xdd\xee\xff"
peer = bytes([int(p, 16) for p in MAC_STRING.split(":")])

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
sta.config(channel=CHANNEL)

e = espnow.ESPNow()
e.active(True)
e.add_peer(peer)

# This code runs only ONCE when the ESP8266 boots up.
print("Sending doorbell signal...")

# Send a message to the receiver.
if e.send(peer, b"ring", True):
        print("Signal sent successfully!")
else:
    print("Failed to send signal.")

# After sending, go into deep sleep forever.
# It will only wake up when the RST pin is pulled to GND by the button press.
print("Going to deep sleep.")
e.active(False)
sta.active(False) 
time.sleep(1) # Give time to interrupt in case of trying to access to repl
esp.deepsleep(0)
