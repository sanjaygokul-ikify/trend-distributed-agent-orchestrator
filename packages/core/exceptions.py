class OrchestrationError(Exception):
    pass

class AgentNotFoundError(OrchestrationError):
    def __init__(self, agent_id: str):
        super().__init__(f"Agent {agent_id} not found")

class TaskAssignmentError(OrchestrationError):
    def __init__(self, task_id: str):
        super().__init__(f"Failed to assign task {task_id}")