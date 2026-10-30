# Wire all four agents together into a executable graph pipeline
from typing import TypedDict
from agents.planner_agent import planner_agent
from agents.retrieval_agent import retrieval_agent
from agents.reasoning_agent import reasoning_agent
from agents.validation_agent import validation_agent
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    question: str
    plan: str
    context: str
    answer: str
    validation: str

def plan_node(state):
    state["plan"] = planner_agent(
        state["question"]
    )
    return state

def retrieve_node(state):
    state["context"] = retrieval_agent(
        state["question"]
    )
    return state

def reason_node(state):
    state["answer"] = reasoning_agent(
        state["question"],
        state["context"]
    )
    return state

def validate_node(state):
    state["validation"] = validation_agent(
        state["question"],
        state["context"],
        state["answer"]
    )
    return state

graph = StateGraph(AgentState)

graph.add_node("planner", plan_node)
graph.add_node("retrieve", retrieve_node)
graph.add_node("reason", reason_node)
graph.add_node("validate", validate_node)

graph.set_entry_point("planner")
graph.add_edge("planner", "retrieve")
graph.add_edge("retrieve", "reason")
graph.add_edge("reason", "validate")
graph.set_finish_point("validate")

workflow = graph.compile()