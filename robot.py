import wpilib
import wpilib.drive
import magicbot
import components.drivetrain

from ctre import WPI_TalonSRX
from components.hatch import Hatch
from automations.hatch_control import HatchAutomation
from automations.shooter_control import ShooterAutomation
from automations.arm_control import ArmAutomation
from components.shooter import Shooter
from components.arm import Arm


# Main class for the robot
class BruhBot(magicbot.MagicRobot):
    """
    The Bruh Bot. Perfect for next year's water game.
    """
    hatch_control: HatchAutomation
    shooter_control: ShooterAutomation
    arm_control: ArmAutomation
    # Using a technique called injection, we can access the class
    # Drivetrain from components/drivetrain.py here.
    drive: components.drivetrain.Drivetrain
    hatch: Hatch
    shooter: Shooter
    arm: Arm

    # Creates all 'objects' used by the robot. Includes high level systems
    # (grabber, drivetrain, etc) and lower level things,
    # like motors or pnuematics
    def createObjects(self):
        # Motors
        self.m_lfront = WPI_TalonSRX(1)
        self.m_rfront = WPI_TalonSRX(2)
        self.m_lback = WPI_TalonSRX(3)
        self.m_rback = WPI_TalonSRX(4)

        self.m_hatch = wpilib.Spark(0)
        self.m_shooter = wpilib.Spark(1)
        self.ls_shooter = wpilib.DigitalInput(0)
        self.s_intake = wpilib.DoubleSolenoid(2, 3)
        # Joysticks (PS4 Controller, in our case)
        self.joystick = wpilib.Joystick(0)

    # Called when teleop period starts during a match
    def teleopInit(self):
        pass

    # Called each tick (every few miliseconds) during the teleop period
    def teleopPeriodic(self):
        self.drive.move(self.joystick.getX(), self.joystick.getY(), 0, 0)
        if self.joystick.getRawButton(5):
            self.hatch_control.start(False)

        if self.joystick.getRawButton(6):
            self.hatch_control.start(True)

        if self.joystick.getRawButton(7):
            self.shooter_control.start(True)

        if self.joystick.getRawButton(8):
            self.shooter_control.start(False)

        if self.joystick.getRawButton(1):
            self.arm_control.start()


# If being ran directly, create a new instance of the BruhBot class
if __name__ == "__main__":
    wpilib.run(BruhBot)
