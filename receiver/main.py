import espnow
import machine
from utils import ring_bell

# --- Pin ---
BUZZER_PIN = 14

e = espnow.ESPNow()
e.active(True)

buzzer = machine.Pin(BUZZER_PIN, machine.Pin.OUT, value=0)

print("Receiver listening for signals...")

while True:
    host, msg = e.recv()
    if msg == b"ring":
        print("Signal received! Ringing the bell...")
        ring_bell(buzzer)
