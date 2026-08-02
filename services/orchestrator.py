from packages.core import Engine
from packages.utils.logging import init_logger

class OrchestratorService:
  def __init__(self):
    self.logger = init_logger(__name__)
    self.engine = Engine(KnowledgeGraph())

  def register_agent(self, agent):
    self.engine.register_agent(agent)
    self.logger.info(f"Agent {agent.id} registered")

  def assign_task(self, task):
    self.engine.assign_task(task)
    self.logger.info(f"Task {task.id} assigned")

  def execute_tasks(self):
    self.engine.execute_tasks()

  def report_progress(self):
    self.engine.report_progress()