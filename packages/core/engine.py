from typing import List, Dict
from logging import getLogger
from .types import Agent, Task, KnowledgeGraph
from .exceptions import OrchestrationError

logger = getLogger(__name__)


class Engine:
    def __init__(self, knowledge_graph: KnowledgeGraph):
        self.knowledge_graph = knowledge_graph
        self.agents: Dict[str, Agent] = {}
        self.tasks: List[Task] = []

    def register_agent(self, agent: Agent):
        self.agents[agent.id] = agent
        logger.info(f"Agent {agent.id} registered")

    def assign_task(self, task: Task):
        self.tasks.append(task)
        logger.info(f"Task {task.id} assigned")
        self._assign_task_to_agent(task)

    def _assign_task_to_agent(self, task: Task):
        # Find a suitable agent for the task
        for agent in self.agents.values():
            if agent.can_execute(task):
                agent.assign_task(task)
                logger.info(f"Task {task.id} assigned to agent {agent.id}")
                break
        else:
            logger.warning(f"No agent found for task {task.id}")

    def update_knowledge_graph(self):
        # Update the knowledge graph with new information
        for agent in self.agents.values():
            self.knowledge_graph.update(agent.get_knowledge())
        logger.info("Knowledge graph updated")

    def execute_tasks(self):
        # Execute all assigned tasks
        for task in self.tasks:
            agent = self.agents[task.agent_id]
            if agent:
                agent.execute_task(task)
            else:
                logger.error(f"Agent {task.agent_id} not found for task {task.id}")

    def report_progress(self):
        # Report progress of all tasks
        for task in self.tasks:
            agent = self.agents[task.agent_id]
            if agent:
                task.status = agent.get_task_status(task)
            else:
                task.status = "failed"
            logger.info(f"Task {task.id} status: {task.status}")