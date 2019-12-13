# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/on')
# def power_on():
#     return 'Power is on'
#
#
# @app.route('off')
# def power_off():
#     return 'Power is off'
#
# #
# if __name__ == '__main__':
#     app.run()

from time import sleep

from gpiozero import LED

button = LED(7)


def power_on():
    button.on()
    sleep(0.5)
    button.off()


def power_off():
    button.on()
    sleep(3)
    button.off()


power_on()
