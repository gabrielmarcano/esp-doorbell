import network
import espnow
import esp
import binascii

# Replace this with the receiver MAC address
MAC_STRING = "AA:BB:CC:DD:EE:FF"

# The address must be in byte format, so turn the string into a byte sequence that looks like b"\xaa\xbb\xcc\xdd\xee\xff"
MAC_BYTES = bytes([int(p, 16) for p in MAC_STRING.split(":")])

# A WLAN interface must be active to send ESP-NOW messages
nic = network.WLAN(network.WLAN.IF_STA)
nic.active(True)
nic.disconnect()  # Because ESP8266 auto-connects to last Access Point
print("Network is active.")
mac_bytes = nic.config("mac")
mac_address_str = binascii.hexlify(mac_bytes, ":").decode().upper()
print(f"MAC address: {mac_address_str}")

e = espnow.ESPNow()
e.active(True)

# Add the receiver as a peer
try:
    e.add_peer(MAC_BYTES)
    print("Receiver peer added successfully.")
except OSError as e:
    print("Error adding peer:", e)

# This code runs only ONCE when the ESP8266 boots up.
print("Woke up. Sending doorbell signal...")

# Send a message to the receiver.
try:
    if e.send(MAC_BYTES, b"ring", True):
        print("Signal sent successfully!")
    else:
        print("Failed to send signal.")
except OSError as err:
    print("Error sending message:", err)

# After sending, go into deep sleep forever.
# It will only wake up when the RST pin is pulled to GND by the button press.
print("Going to deep sleep. Press the button to wake up.")
esp.deepsleep(0)
