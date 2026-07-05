class DecisionCore:
    def decide(self, risk_level):
        if risk_level == "CRITICAL":
            return "CONTAIN_IMMEDIATELY"
        elif risk_level == "HIGH":
            return "ISOLATE_AND_MONITOR"
        else:
            return "LOG_AND_LEARN"
