<h1 align="center">ESP Doorbell Project</h1>
<p align="center">
  A project to control a doorbell system using two ESP8266
</p>

<div align="center">

<!-- [![Build](https://img.shields.io/github/actions/workflow/status/gabrielmarcano/esp32-roaster/build.yml?logo=github)](https://github.com/gabrielmarcano/esp32-roaster/blob/master/.github/workflows/build.yml) -->
<!-- [![OTA Update](https://img.shields.io/github/actions/workflow/status/gabrielmarcano/esp32-roaster/ota-update.yml?logo=github&label=OTA)](https://github.com/gabrielmarcano/esp32-roaster/blob/master/.github/workflows/ota-update.yml) -->
<!-- [![GitHub release](https://img.shields.io/github/v/release/gabrielmarcano/esp32-roaster?filter=*alpha&logo=github)](https://github.com/gabrielmarcano/esp32-roaster/releases) -->

[![python](https://img.shields.io/badge/Python-3.13-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![micropython](https://img.shields.io/badge/built%20for-MicroPython-3776AB?logo=micropython)](https://micropython.org/)

</div>

## Contents

- [Summary](#summary)
- [Deployment](#Deployment)
- [Wiring](#wiring)
- [Resources](#resources)

## Summary

This project implements a doorbell system using two ESP8266 microcontrollers communicating via the ESP-NOW protocol. One ESP8266 acts as a sender, powered by a battery and triggered by a button press. The other ESP8266 acts as a receiver, plugged into a power source and connected to a buzzer. When the sender's button is pressed, it transmits a signal to the receiver, which then activates the buzzer for a short duration, simulating a doorbell ring.

## Deployment

Use `build.py` to **automate the process of preparing, compiling, and deploying your MicroPython code** to an ESP board.

This interactive script streamlines the workflow by guiding you through the following steps:

1.  **Project Selection:** It first prompts you to choose whether you want to build the `sender` or the `receiver` code.
2.  **Code Compilation:** It asks if you want to compile your `.py` files into `.mpy` bytecode using `mpy-cross`. This makes the code run faster and use less memory on the device.
3.  **Device Upload:** Finally, it asks if you want to upload the prepared files directly to the root directory of your connected ESP board using `mpremote`.

## Wiring

### Sender

| ESP8266 | BUTTON |
| ------- | ------ |
| RST     | +      |
| GND     | \-     |

### Receiver

| ESP8266 | BUZZER |
| ------- | ------ |
| GPIO14  | +      |
| GND     | \-     |

## Resources

### ESP-NOW

MicroPython ESP-NOW protocol library for ESP devices.

https://docs.micropython.org/en/latest/library/espnow.html

### mpy-cross

MicroPython cross compiler utility, used to pre-compile python files into [mpy files](https://docs.micropython.org/en/latest/reference/mpyfiles.html).

https://pypi.org/project/mpy-cross/

### mpremote

MicroPython tool for remotely interact with devices over a serial connection.

https://docs.micropython.org/en/latest/reference/mpremote.html
