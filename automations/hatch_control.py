from magicbot import StateMachine, state, timed_state
from components.hatch import Hatch


class HatchAutomation(StateMachine):
    hatch: Hatch

    def __init__(self):
        super().__init__()
        self.state = False

    def start(self, state):
        self.state = state
        self.engage("prep_hatch")

    @state(first=True)
    def prep_hatch(self):
        if self.state:
            self.hatch.hatch_in()
        else:
            self.hatch.hatch_out()
        self.state = False
        self.next_state_now("running")

    @timed_state(duration=1, must_finish=True)
    def running(self):
        self.hatch.enable()
