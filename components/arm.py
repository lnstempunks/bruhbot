# SETUP
# DigitalInput(0) - Limit Switch
# Interrupts the shooter when pressed
# Spark(1) - Shooter
# DoubleSolenoid(2, 3) - Intake Solenoid

# WHAT DOES IT DO
from wpilib import DigitalInput, Spark, DoubleSolenoid


class Arm:
    intakeSolenoid: DoubleSolenoid

