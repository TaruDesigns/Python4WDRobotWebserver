# Rover Control
This is a project to control a rover/robot through an ESP8266/ESP32 running webserver on MicroPython

# The Robot
The robot is one of these standard 4WD robot kits you can get on AliExpress. There are many sellers and variations on the same chassis
![4wdcar](images/car_example.JPG "Car Example")
The construction is very simple: Two plexiglass sheets, four (geared) motors attached to one of them, and plenty of space and holes for electronics

# Table of Contents
- [Rover Control](#rover-control)
- [The Robot](#the-robot)
- [Table of Contents](#table-of-contents)
- [BOM](#bom)
- [Power Supply Considerations](#power-supply-considerations)
- [Controlling Servo Motors](#controlling-servo-motors)
- [Quick installation and usage guide:](#quick-installation-and-usage-guide)
- [Feature List](#feature-list)

# BOM
List of components used:
* ESP8266: WEMOS D1 Mini
* ESP32CAM: Used as a simple and cheap IP Webcam.
* L9110 H Bridge: I am using a premade board with 4 of the ICs in them, but a similar H Bridge board would suffice.
* Power Bank: USB Power Bank
* HMC5883L: Used as a compass/heading indicator.
* 9G Servos: ![pantilt](images/9gservo.JPG "9G Servo")
* Pan/Tilt servo brackets ![pantilt](images/pantilt_bracket.JPG "PanTilt Bracket"): Used to mount the camera. They are cheap but 3D Printed altenatives should be just as good!

# Power Supply Considerations

The basic system (ESP8266+Motors) will use about 700mA@5V when running on high speed (depending on total weight), however, you can expect current spikes of about 1.5A@5V when the motors are starting. Make sure your power supply can keep a steady supply on those spikes and/or add aditional decoupling otherwise you might run into glitches with either of the ESPs rebooting.

# Controlling Servo Motors

I am using PWM outputs on the ESP8266 to control the servos directly, as well as the motors. Note that this isn't ideal, and an external PWM board (such as the PCA9685) would be preferred.

# Quick installation and usage guide:

* Make sure your ESP is running micropython firmware
* Adjust the settings.json file to enable/disable modules as well as set your preferred GPIO
* Change the wlan_settings.py file (your SSID settings are stored there)
* Upload every file to your ESP (I like using Ampy but WebREPL works fine as well)
  
# Feature List
* Control a 4WD rover, changing direction and speed (two selectable speeds) through HTML page: **DONE**
* Move the bracket the cam is sitting on: **DONE**
* Show real time heading: Sensor configured, pending to include in control panel
* Show real time cam: Sensor (ESP32CAM) configured, pending to include in control panel
* Infinitely adjustable speed and direction (Joystick Control): PENDING

