from magicbot import StateMachine, state, timed_state
from components.arm import Arm


class ArmAutomation(StateMachine):
    arm: Arm

    def __init__(self):
        super().__init__()

    def start(self):
        self.engage()

    @state(first=True)
    def prep_hatch(self):
        self.arm.toggle_arm()

    @state(must_finish=True)
    def running(self):
        self.arm.enable()
