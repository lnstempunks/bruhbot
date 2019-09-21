import wpilib
from wpilib.drive import MecanumDrive

from ctre import WPI_TalonSRX


class Drivetrain:
    # We also use injection here to access the l_motor and r_motor declared in BruhBot's
    # createObjects method.
    m_lfront: WPI_TalonSRX
    m_rfront: WPI_TalonSRX
    m_lback: WPI_TalonSRX
    m_rback: WPI_TalonSRX

    xSpeed = 0
    ySpeed = 0
    zRotation = 0
    gyroAngle = 0

    # Declare the basic drivetrain setup.
    def setup(self):
        self.mec_drive = MecanumDrive(
            self.m_lfront, self.m_lback, self.m_rfront, self.m_rback
        )
        self.mec_drive.setExpiration(0.1)
        self.mec_drive.setSafetyEnabled(True)

    # Change x and y variables for movement.
    def move(self, x, y, z, gyroAngle):
        self.xSpeed = x if abs(x) > 0.03 else 0
        self.ySpeed = y if abs(y) > 0.03 else 0
        self.zRotation = z
        self.gyroAngle = gyroAngle

    # Each time move is called, call arcadeDrive with supplied
    # x and y coordinates.
    def execute(self):
        self.mec_drive.driveCartesian(
            self.xSpeed, self.ySpeed, self.zRotation, self.gyroAngle
        )
