from machine import Pin
import time

num_leds = 8


led_pins = [Pin(pin_num, Pin.OUT) for pin_num in [16, 17, 18, 19, 20, 21, 22, 26]]

def display_binary(number):
    
    for i in range(num_leds):
        
        if number & (1 << i):
            led_pins[i].on()
        else:
            led_pins[i].off()

def loop_through_numbers():
    while True:
        for number in range(256):  
            display_binary(number)
            time.sleep(0.5)  

loop_through_numbers()