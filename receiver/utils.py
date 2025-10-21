def play_chime(buzzer_pin):
    """
    Plays a two-tone 'ding-dong' chime on the passive buzzer.
    """
    import machine
    import time
    
    buzzer = machine.PWM(buzzer_pin)
    
    # Set the duty cycle (volume). 512 is 50% (range 0-1023)
    buzzer.duty(512)
    
    # Play "Ding" (E5)
    buzzer.freq(659)
    time.sleep_ms(200)
    
    # Play "Dong" (C5)
    buzzer.freq(523)
    time.sleep_ms(300)
    
    buzzer.deinit()

def blink_internal_led(pin):
    """
    Manages the internal LED by turning it on and off in a specific pattern.
    """
    import time

    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.25)
    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.25)
    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.25)
    pin.on()
    time.sleep(0.5)
    pin.off()
