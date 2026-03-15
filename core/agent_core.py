from perception.screen_capture import ScreenCapture
from reasoning.llm_brain import LLMBrain
from planning.task_planner import TaskPlanner
from executor.action_executor import ActionExecutor

class AgentCore:

    def __init__(self):

        self.vision = ScreenCapture()
        self.brain = LLMBrain()
        self.planner = TaskPlanner()
        self.executor = ActionExecutor()

    def run(self):

        while True:

            observation = self.vision.capture()

            thought = self.brain.think(observation)

            plan = self.planner.create_plan(thought)

            self.executor.execute(plan)
