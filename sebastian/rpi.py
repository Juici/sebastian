try:
    import RPi.GPIO as GPIO
except RuntimeError:
    raise RuntimeError('Error importing RPi.GPIO. Superuser privileges may be required.')

LEFT_WHEEL = 12
RIGHT_WHEEL = 13

# LEFT_WHEEL = 32
# RIGHT_WHEEL = 33

CHANNELS = [LEFT_WHEEL, RIGHT_WHEEL]

FREQ = 500
DC = 100


class RPi:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)

        GPIO.setup(CHANNELS, GPIO.OUT)

        self._left = GPIO.PWM(LEFT_WHEEL, FREQ)
        self._right = GPIO.PWM(RIGHT_WHEEL, FREQ)

    def forward(self):
        self._left.start(DC)
        self._right.start(DC)

    def left(self):
        self._left.start(DC)
        self._right.stop()

    def right(self):
        self._right.start(DC)
        self._left.stop()

    def stop(self):
        self._left.stop()
        self._right.stop()

    def __del__(self):
        self._left.stop()
        self._right.stop()

        GPIO.cleanup(CHANNELS)
