# HATCH
# MADE OF MOTOR AND LIMIT SWITCH(?)
# WHAT DOES IT DO - It runs the motor in one direction or another depending on the joystick pressed.
# Control Methods - hatch_in hatch_out
# Execute Method - Run The Motor About Speed

from wpilib import Spark


class Hatch:
    m_hatch: Spark

    def setup(self):
        self.speed = 0
        self.enabled = False

    def enable(self):
        self.enabled = True

    def hatch_in(self):
        self.speed = -0.6

    def hatch_out(self):
        self.speed = 0.8

    def execute(self):
        if self.enabled:
            self.m_hatch.set(self.speed)
        else:
            self.m_hatch.set(0)

        self.speed = 0
        self.enabled = False
