import binascii
import network

# Put the device in station mode and activate it.
nic = network.WLAN(network.WLAN.IF_STA)
if not nic.active():
    print("Activating network interface...")
    nic.active(True)
    nic.disconnect()  # Because ESP8266 auto-connects to last Access Point

print("Network is active.")
mac_bytes = nic.config("mac")
mac_address_str = binascii.hexlify(mac_bytes, ":").decode().upper()
print(f"MAC address: {mac_address_str}")
