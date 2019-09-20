import wpilib
import wpilib.drive


class Drivetrain:
    # We also use injection here to access the l_motor and r_motor declared in BruhBot's
    # createObjects method.
    l_motor: wpilib.Talon
    r_motor: wpilib.Talon

    # Declare the basic drivetrain setup.
    def setup(self):
        self.dif_drive = wpilib.drive.DifferentialDrive(self.l_motor, self.r_motor)

    # Change x and y variables for movement.
    def move(self, x, y):
        self.x = x
        self.y = y
    
    # Each time move is called, call arcadeDrive with supplied x and y coordinates.
    def execute(self):
        self.dif_drive.arcadeDrive(self.x, self.y)
