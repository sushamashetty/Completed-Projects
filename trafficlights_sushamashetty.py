#Embedded Systems Project(2020)
#LED controlled with PCA
import time
import busio
import board
import adafruit_pca9685
def SS_phase_1():
#setting red LED on
pca9685.channels[SS_trafficLight_0].duty_cycle = SS_onLED
print("Red LED is ON")
#setting green LED on
pca9685.channels[SS_trafficLight_5].duty_cycle = SS_onLED
print("green LED is on")
time.sleep(3) # 3 seconds
#setting red LED off
pca9685.channels[SS_trafficLight_0].duty_cycle = SS_offLED
#setting green LED off
pca9685.channels[SS_trafficLight_5].duty_cycle = SS_offLED
return
def SS_phase_2():
#setting red LED and amber LED on
pca9685.channels[SS_trafficLight_0].duty_cycle = SS_onLED
pca9685.channels[SS_trafficLight_1].duty_cycle = SS_onLED
print("red and amber LEDs are on")
# setting Amber LED on
pca9685.channels[SS_trafficLight_4].duty_cycle = SS_onLED
print("Amber LED is on")
time.sleep(3) # 3 seconds
pca9685.channels[SS_trafficLight_0].duty_cycle = SS_offLED
pca9685.channels[SS_trafficLight_1].duty_cycle = SS_offLED
pca9685.channels[SS_trafficLight_4].duty_cycle = SS_offLED
return
def SS_phase_3():
#setting green LED on
pca9685.channels[SS_trafficLight_2].duty_cycle = SS_onLED
print("green LED is on")
#setting red LED on
pca9685.channels[SS_trafficLight_3].duty_cycle = SS_onLED
print("Red LED is ON")
time.sleep(3) # 3 seconds
#setting green LED off
pca9685.channels[SS_trafficLight_2].duty_cycle = SS_offLED
#setting red LED off
pca9685.channels[SS_trafficLight_3].duty_cycle = SS_offLED
return
def SS_phase_4():
pca9685.channels[SS_trafficLight_1].duty_cycle = SS_onLED
print("Amber LED is on")
#setting red LED and amber LED on
pca9685.channels[SS_trafficLight_3].duty_cycle = SS_onLED
pca9685.channels[SS_trafficLight_4].duty_cycle = SS_onLED
time.sleep(3) # 3 seconds
pca9685.channels[SS_trafficLight_1].duty_cycle = SS_offLED
pca9685.channels[SS_trafficLight_3].duty_cycle = SS_offLED
pca9685.channels[SS_trafficLight_4].duty_cycle = SS_offLED
return
def SS_allLEDsOff():
#setting all the LEDs off
for trafficLightNr in range(6):
pca9685.channels[trafficLightNr].duty_cycle = SS_offLED
return
#Creating the I2C bus instance
i2c_bus = busio.I2C (board.SCL, board.SDA)
# Creating a PCA instance
pca9685 = adafruit_pca9685.PCA9685(i2c_bus)
#Setting the PWM frequency to 60Hz
pca9685.frequency = 60
#per 1 of the 60 Hz there are
#65536 duty cycles-values
SS_onLED = 65535 # PWM duty cycle 100%
SS_offLED = 0 # PWM duty cylce 0%
#SS_ledNr = 0 # index of LED port = 0
SS_trafficLight_0 = 0 # red light
SS_trafficLight_1 = 1 # amber light
SS_trafficLight_2 = 2 # green light
SS_trafficLight_3 = 3 # red light
SS_trafficLight_4 = 4 # amber light
SS_trafficLight_5 = 5 # green light
SS_allLEDsOff()
print("To finish press Ctrl + C")
try:
while True:
print()
SS_phase_1()
SS_phase_2()
SS_phase_3()
SS_phase_4()
except KeyboardInterrupt:
print("finish")
SS_allLEDsOff()
print("The End")
