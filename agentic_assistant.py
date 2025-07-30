import os
from langgraph.agents import Agent, Task, Workflow, tool
from tools.flight import book_flight
from tools.hotel import book_hotel
from tools.calendar import create_calendar_event

# Example: Parse user request (stub for demo)
def parse_user_request(request: str):
    # In production, use LLM or NLU to extract these fields
    return {
        "origin": "JFK",
        "destination": "SFO",
        "depart_date": "2025-08-10",
        "return_date": "2025-08-15",
        "hotel_location": "Moscone Center, San Francisco"
    }

# Workflow graph
workflow = Workflow()

workflow.add_node("flight", Task(
    tool=book_flight,
    next="hotel"
))

workflow.add_node("hotel", Task(
    tool=book_hotel,
    next="calendar"
))

workflow.add_node("calendar", Task(
    tool=create_calendar_event
))

workflow.set_entrypoint("flight")

agent = Agent(workflow=workflow)

def handle_user_request(request):
    parsed = parse_user_request(request)
    result = agent.run(parsed)
    print("==== Final Result ====")
    print(result)

if __name__ == "__main__":
    print("Welcome to the Agentic AI Workflow Assistant!")
    user_request = input("Enter your travel/workflow request:\n")
    handle_user_request(user_request)
