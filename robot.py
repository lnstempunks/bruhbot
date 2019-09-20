import wpilib
import wpilib.drive
import magicbot
import components.drivetrain

# Main class for the robot
class BruhBot(magicbot.MagicRobot):
    """
    The Bruh Bot. Perfect for next year's water game.
    """
    # Using a technique called injection, we can access the class 
    # Drivetrain from components/drivetrain.py here.
    drive: components.drivetrain.Drivetrain

    # Creates all 'objects' used by the robot. Includes high level systems (grabber, drivetrain, etc)
    # and lower level things, like motors or pnuematics
    def createObjects(self):
        # Motors
        self.l_motor = wpilib.Talon(1)
        self.r_motor = wpilib.Talon(2)

        # Joysticks (PS4 Controller, in our case)
        self.joystick = wpilib.Joystick(0)

    # Called when teleop period starts during a match
    def teleopInit(self):
        pass

    # Called each tick (every few miliseconds) during the teleop period
    def teleopPeriodic(self):
        self.drive.move(self.joystick.getX(), self.joystick.getY())


# If being ran directly, create a new instance of the BruhBot class
if __name__ == "__main__":
    wpilib.run(BruhBot)
