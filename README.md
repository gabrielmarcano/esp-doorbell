<h1 align="center">ESP Doorbell Project</h1>
<p align="center">
  A project to control a doorbell system using an ESP8266 and an ESP32
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

This project implements a doorbell system using both ESP8266 and ESP32 microcontrollers that communicate via the ESP-NOW protocol. The ESP8266 acts as the sender, powered by a battery and triggered by a button press. The ESP32 acts as the receiver and proxy, connected to a power source and a WiFi network. When the sender’s button is pressed, it transmits an ESP-NOW packet to the receiver, which then sends a POST request to a Home Assistant webhook. This setup simulates a doorbell ring, allowing Home Assistant to trigger any automation you configure.

## Deployment

The ESP8266 and ESP32 microcontrollers were programmed using MicroPython and deployed via the `mpremote` tool. To transfer the main script to the device, the following command was used, specifying the appropriate serial port for each board:

```bash
mpremote connect /dev/cu.usbserial-100 fs cp main.py :
```

Change the port to your specific device. See the list of connected devices with:

```bash
mpremote connect list
```

## Wiring

### Sender

| ESP8266 | BUTTON |
| ------- | ------ |
| RST     | +      |
| GND     | \-     |

## Resources

### MicroPython

Implementation of the Python 3 programming language optimised to run on microcontrollers.

https://docs.micropython.org/en/latest/

### ESP-NOW

MicroPython ESP-NOW protocol library for ESP devices.

https://docs.micropython.org/en/latest/library/espnow.html

### mpremote

MicroPython tool for remotely interact with devices over a serial connection.

https://docs.micropython.org/en/latest/reference/mpremote.html
