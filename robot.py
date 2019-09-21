import wpilib
import wpilib.drive
import magicbot
import components.drivetrain

from ctre import WPI_TalonSRX


# Main class for the robot
class BruhBot(magicbot.MagicRobot):
    """
    The Bruh Bot. Perfect for next year's water game.
    """
    # Using a technique called injection, we can access the class
    # Drivetrain from components/drivetrain.py here.
    drive: components.drivetrain.Drivetrain

    # Creates all 'objects' used by the robot. Includes high level systems
    # (grabber, drivetrain, etc) and lower level things,
    # like motors or pnuematics
    def createObjects(self):
        # Motors
        self.m_lfront = WPI_TalonSRX(1)
        self.m_rfront = WPI_TalonSRX(2)
        self.m_lback = WPI_TalonSRX(3)
        self.m_rback = WPI_TalonSRX(4)

        # Joysticks (PS4 Controller, in our case)
        self.joystick = wpilib.Joystick(0)

    # Called when teleop period starts during a match
    def teleopInit(self):
        pass

    # Called each tick (every few miliseconds) during the teleop period
    def teleopPeriodic(self):
        self.drive.move(self.joystick.getX(), self.joystick.getY(), 0, 0)


# If being ran directly, create a new instance of the BruhBot class
if __name__ == "__main__":
    wpilib.run(BruhBot)
