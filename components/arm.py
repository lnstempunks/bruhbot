# SETUP
# DigitalInput(0) - Limit Switch
# Interrupts the shooter when pressed
# Spark(1) - Shooter
# DoubleSolenoid(2, 3) - Intake Solenoid

# WHAT DOES IT DO
from wpilib import DigitalInput, Spark, DoubleSolenoid
from components.shooter import Shooter


class Arm:
    s_intake: DoubleSolenoid

    def setup(self):
        self.arm_state = DoubleSolenoid.Value.kOff

    def toggle_arm(self):
        if self.arm_state == DoubleSolenoid.Value.kForward:
            self.arm_state = DoubleSolenoid.Value.kReverse
        else:
            self.arm_state = DoubleSolenoid.Value.kForward

    def execute(self):
        self.s_intake.set(self.arm_state)
        self.arm_state = DoubleSolenoid.Value.kOff
