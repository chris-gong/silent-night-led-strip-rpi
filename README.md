# Playing Silent Night while lighting up a WS2812B LED strip
(Made by Chris Gong and Ryan Thomas)

## Materials and setup
For this project you will need a WS2812B LED strip and a Raspberry Pi. The 5V pad on the LED strip has to be connected to one of the 5V pins on the pi, the DI pad on the strip has to be connected to pin 18 on the pi, and the GND pad on the strip has to be connected to one of the ground pins on the pi.

## Running the program
This project is dependent on a couple of packages. We suggest pip installing these packages (note that we are using python 3).

```
sudo pip3 install rpi_ws281x
sudo pip3 install pygame
```

Then, after installing these packages, simply run the program like so,
```
sudo python3 christmas.py
```

## Variables that could change
A couple things should be mentioned that could require changes in the code. One, if you decide not to use pin 18 on the pi, then set the value appropriately in the variable `LED_PIN` to the pin you do decide to use. Second, our LED strip had 300 LEDs, but if your's does not then set the value appropriately in the variable `LED_COUNT` to the number of LEDs you do decide to use.

Note that you may have to tinker with numbers in lines 46-50 to make it light up to your liking. These lines determine which LEDs light up at each note, so you can experiment and create different and more colorful patterns!

## Implementation Video
https://www.youtube.com/watch?v=CZVQ-xg_SeI
