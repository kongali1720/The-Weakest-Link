class ResponseOrchestrator:

    def execute(self, action):
        if action == "CONTAIN_IMMEDIATELY":
            self.contain()
        elif action == "ISOLATE_AND_MONITOR":
            self.isolate()
        else:
            self.log()

    def contain(self):
        print("[AUTO SOC] System containment executed")

    def isolate(self):
        print("[AUTO SOC] Node isolated")

    def log(self):
        print("[AUTO SOC] Event logged for learning")
