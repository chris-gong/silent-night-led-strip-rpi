import time
import pygame
from rpi_ws281x import *
import random

LED_PIN = 18
LED_COUNT = 300
LED_FREQ_HZ = 800000
LED_BRIGHTNESS = 255

notes= [[('c', 'l', 3,1 ), ('g', 'r', 1.5,1)], [('a', 'r', .5, 1)], [('g', 'r', 1, 1)], [('c', 'l', 3, 1) , ('e', 'r', 3, 1)], [('c', 'l', 3,1), ('g','r', 1.5, 1)], [('a', 'r', .5, 1)], [('g', 'r', 1, 1)],
        [('c', 'l', 1, 1), ('e', 'r', 3, 1)], [('b', 'l', 1,1)], [('a', 'l', 1,1)],[('g', 'l', 3, 1), ('d', 'r', 2, 2)], [('d', 'r', 1, 2)], [('g', 'l', 2, 1), ('b', 'r', 3,1)], [('g', 'l', 1,1)],
        [('c', 'l' ,3 ,1), ('c','r', 2,2  )], [('c', 'r', 1, 2)], [('c', 'l', 3 ,1), ('g', 'r', 3, 1)], [('f', 'l', 3, 1), ('a', 'r', 2, 1)],[('a', 'r', 1,1)], [('f', 'l', 3, 1), ('c', 'r', 1.5, 2)],
        [('b', 'r', .5, 1)], [('a', 'r', 1,1)], [('c', 'l', 3, 1), ('g', 'r', 1.5,1)], [('a', 'r', .5, 1)], [('g', 'r', 1,1)],
 [('c', 'l', 3, 1), ('e', 'r', 3,1)], [('f', 'l',3,1), ('a', 'r', 2, 1)], [('a', 'r', 1,1)], [('f', 'l', 3, 1), ('c', 'r', 1.5, 2)],
        [('b', 'r', .5, 1)], [('a', 'r', 1,1)], [('c', 'l', 3, 1), ('g', 'r', 1.5, 1)],
 [('a', 'r', .5,1)], [('g', 'r', 1,1)], [('c', 'l', 1,1), ('e', 'r', 3,1)], [('b', 'l', 1,1)],
        [('a', 'l', 1,1)], [('g', 'l', 3,1), ('d', 'r', 2,2)], [('d', 'r', 1,2)], [('g', 'l', 3, 1), ('f', 'r', 1, 2)], [('d', 'r', 1, 2)],
 [('b', 'r', 1,1)], [('c', 'l', 3, 1), ('c', 'r', 3, 2)], [('c', 'l', 3,1), ('e', 'r', 3,2)], [('c', 'l', 3, 1), ('c', 'r', 1, 2)],
        [('g', 'r', 1,1)], [('e', 'r', 1,1)], [('g', 'l', 3, 1), ('g', 'r', 1.5, 1)], [('f', 'r', .5, 1)],
 [('d', 'r', 1, 1)], [('c', 'l', 3,1), ('c', 'r', 3, 1)]] 

if __name__ == '__main__':
    pygame.init()
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,10,False,255,0)
    strip.begin()
    for x in range(0,300):
        strip.setPixelColor(x,Color(0,0,0))
    strip.show()
    pygame.mixer.music.load("silent_night.mp3")
    pygame.mixer.music.play()
    time.sleep(1)
    for x in range(0,len(notes)):
        smallestDuration = 100

        for y in range(0, len(notes[x])):
        
            note = notes[x][y][0]
            hand = notes[x][y][1]
            duration = notes[x][y][2]
            octave = notes[x][y][3]

            if(duration < smallestDuration):
                smallestDuration = duration
                
            for z in range(0,10):
                if hand == 'r':
                    strip.setPixelColor(150 + (z * 2) + int(ord(note)/2) * int(octave/2),Color(255,0,0))
                if hand == 'l':
                    strip.setPixelColor(150 - (z * 2) - int(ord(note)/2) * int(octave/2),Color(255,0,0))
            
            strip.show()
        time.sleep(smallestDuration/1.78)     
        for x in range(0,300):
            strip.setPixelColor(x,Color(0,0,0))
        strip.show()
        
    for x in range(0,300):
        strip.setPixelColor(x,Color(0,0,0))
        strip.show()
    
