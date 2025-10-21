import espnow
import machine
from utils import blink_internal_led, play_chime

BUZZER_PIN = 14
INTERNAL_LED_PIN = 2

e = espnow.ESPNow()
e.active(True)

buzzer = machine.Pin(BUZZER_PIN)

# ESP8266 has an active-low internal LED, so we use a Signal to manage the inverted state
led = machine.Signal(machine.Pin(INTERNAL_LED_PIN, machine.Pin.OUT, value=1), invert=True)

print("Receiver listening for signals...")

# Always listen for a "ring" sent within a ESP-NOW packet
while True:
    host, msg = e.recv()
    if msg == b"ring":
        print("Signal received! Ringing the bell...")
        play_chime(buzzer)
        blink_internal_led(led)
