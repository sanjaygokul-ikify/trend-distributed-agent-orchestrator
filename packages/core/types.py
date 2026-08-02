from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Agent:
    id: str
    capabilities: List[str]

    def can_execute(self, task: 'Task') -> bool:
        return task.requirements in self.capabilities

    def assign_task(self, task: 'Task'):
        # Assign the task to the agent
        pass

    def execute_task(self, task: 'Task'):
        # Execute the task
        pass

    def get_knowledge(self) -> Dict:
        # Return the agent's knowledge
        return {}

    def get_task_status(self, task: 'Task') -> str:
        # Return the status of the task
        return "unknown"

@dataclass
class Task:
    id: str
    requirements: str
    agent_id: str = None
    status: str = "pending"

@dataclass
class KnowledgeGraph:
    def update(self, knowledge: Dict):
        # Update the knowledge graph with new information
        pass