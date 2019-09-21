from wpilib import DigitalInput, Spark


class Shooter:
    limitSwitch: DigitalInput
    shooter: Spark

    def __init__(self):
        self.speed = 0
        self.switchState = False
        self.enabled = False

    def enable(self):
        self.enabled = True

    def is_pressed(self):
        self.switchState = self.limitSwitch.get()

    def set_speed(self, new_speed):
        self.speed = new_speed

    def execute(self):
        if self.enabled and self.switchIsOn:
            self.shooter.set(self.speed)
        else:
            self.shooter.set(0)
        self.enabled = False
        self.switchIsOn = False
