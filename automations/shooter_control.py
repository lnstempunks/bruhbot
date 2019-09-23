from magicbot import StateMachine, state, timed_state
from components.shooter import Shooter


class ShooterAutomation(StateMachine):
    shooter: Shooter

    def __init__(self):
        super().__init__()
        self.state = False

    def start(self, state):
        self.state = state
        self.engage("prep_shooter")

    @state(first=True)
    def prep_shooter(self):
        if self.state:
            self.shooter.set_speed(0.6)
        else:
            self.shooter.set_speed(-1)
        self.next_state_now("running")

    @state(must_finish=True)
    def running(self):
        self.shooter.enable()
        self.state = False
