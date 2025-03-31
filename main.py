#----------------------------------------------
# A SIMPLE SINE WAVE GENERATOR 
# WITH TO POTS FOR AMPLITUDE AND FREQUENCY MANIPIULATING
# ARDUINO ACTS AS AN ADC AND CONVERTS THE POTS ANALOG SIGNALS
# TO THE RASPBERRY PI
#----------------------------------------------
from pyo import Server, Sine
import time

SAMPLE_RATE = 44100
CHANNELS = 2
BUFFER_SIZE = 256
DUPLEX = 0

# Initialize Pyo audio server
s = Server(sr=SAMPLE_RATE, nchnls=CHANNELS, buffersize=BUFFER_SIZE, duplex=DUPLEX).boot()
s.start()

sine_wave_left = Sine(freq=440, mul=0.5)
sine_wave_right = Sine(freq=440, mul=0.5)
sine_wave_left.out(chnl=0)
sine_wave_right.out(chnl=0)

try:
    print("Press Ctrl+C to stop the program.")
    while True:
        time.sleep(1)  # Keep the program running efficiently
except KeyboardInterrupt:
    print("Shutting down...")
    s.stop()
    s.shutdown()