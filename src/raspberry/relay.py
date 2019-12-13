from time import sleep

from gpiozero import LED

button = LED(7)


def power_on():
    button.on()
    sleep(500)
    button.off()


def power_off():
    button.on()
    sleep(3000)
    button.off()