import time
from pynput.mouse import Button, Controller
mouse = Controller()

min = 30


for i in range(min):
    print ('\r'+str(i)+' min van ' + str(min) + ' voorbij')
    mouse.scroll(0,1000)
    time.sleep(60)  # aantal seconden delay