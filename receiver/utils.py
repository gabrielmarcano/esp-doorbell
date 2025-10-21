def ring_bell(buzzer):
    """
    Rings the buzzer for a short duration.
    """
    import time

    buzzer.on()
    time.sleep(0.5)
    buzzer.off()
    time.sleep(0.1)
    buzzer.on()
    time.sleep(0.5)
    buzzer.off()


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
    


def make_buzzer_sound(pin):
    """
    Makes a sound using a buzzer
    """
    from machine import PWM

    beeper = PWM(pin, freq=440, duty=512)
    beeper.deinit()


def play_melody(buzzer_pin):
    """
    Plays a melody using a buzzer
    """
    from machine import PWM
    import time

    tempo = 5
    tones = {
        "c": 262,
        "d": 294,
        "e": 330,
        "f": 349,
        "g": 392,
        "a": 440,
        "b": 494,
        "C": 523,
        " ": 0,
    }
    beeper = PWM(buzzer_pin, freq=440, duty=512)
    melody = "cdefgabC"
    rhythm = [8, 8, 8, 8, 8, 8, 8, 8]

    for tone, length in zip(melody, rhythm):
        beeper.freq(tones[tone])
        time.sleep(tempo / length)
    beeper.deinit()
