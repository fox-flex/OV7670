# Camera OV7670 via arduino

## About
This project make photo using OV7670 model and send it into Serial port. </br>
It's possible to configurate image properties in file  `src/ExampleUart.cpp` </br>
To get images fill in the firmware into Arduino Uno and afterwards run `read_img_from_serial.py`

## Pinout
- Power supply
  - 3.3V -> 3.3V
  - GND -> GND
- Camera Control Bus (SCCB) - I2C interface
  - SIOC -> A5
  - SIOD -> A4
- 

## Images examples
![](./img/3/p2.jpg) </br>
![](./img/3/p3.jpg)

## Used sources
- [Tutorial](https://circuitjournal.com/arduino-OV7670-to-pc)
- [Git source](https://github.com/indrekluuk/LiveOV7670)