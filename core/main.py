from event_bus import EventBus
from ai_correlation_engine import AICorrelationEngine
from risk_engine import RiskEngine
from decision_core import DecisionCore
from soc.response_orchestrator import ResponseOrchestrator

bus = EventBus()
ai = AICorrelationEngine()
risk = RiskEngine()
decision = DecisionCore()
response = ResponseOrchestrator()

def handle(event):

    analysis = ai.analyze(event)
    level = risk.evaluate(analysis)
    action = decision.decide(level)

    response.execute(action)

    print("[SOC] cycle complete")

bus.subscribe(handle)

bus.start()

bus.publish({"type": "network_event", "payload": "suspicious_activity"})
