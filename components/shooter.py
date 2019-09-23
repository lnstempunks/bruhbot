from wpilib import DigitalInput, Spark


class Shooter:
    ls_shooter: DigitalInput
    m_shooter: Spark

    def __init__(self):
        self.speed = 0
        self.switchState = False
        self.enabled = False

    def enable(self):
        self.enabled = True

    def is_pressed(self):
        self.switchState = self.limitSwitch.get()
        return self.switchState

    def set_speed(self, new_speed):
        self.speed = new_speed

    def execute(self):
        if self.enabled and self.switchIsOn:
            self.m_shooter.set(self.speed)
        else:
            self.m_shooter.set(0)
        self.enabled = False
        self.switchIsOn = False
