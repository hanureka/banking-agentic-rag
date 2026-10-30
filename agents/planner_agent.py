from typing import Dict

def planner_agent(question: str):
    task_plan = {
        "query": question,
        "steps": [
            "retrieve",
            "reason",
            "validate"
        ]
    }
    return task_plan