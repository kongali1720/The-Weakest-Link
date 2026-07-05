class RiskEngine:
    def evaluate(self, analysis):
        score = analysis["risk_score"]

        if score > 0.8:
            return "CRITICAL"
        elif score > 0.5:
            return "HIGH"
        return "LOW"
