class ActionExecutor:

    def execute(self, plan):

        print("Executing plan:", plan)

        for step in plan:
            print("Doing step:", step)
