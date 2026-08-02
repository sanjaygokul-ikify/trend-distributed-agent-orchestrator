import unittest
from services.orchestrator import OrchestratorService

class TestRuntime(unittest.TestCase):
  def test_register_agent(self):
    orchestrator = OrchestratorService()
    agent = Agent(id="agent-1", capabilities=["capability-1"])
    orchestrator.register_agent(agent)
    self.assertEqual(orchestrator.engine.agents[agent.id], agent)

  def test_assign_task(self):
    orchestrator = OrchestratorService()
    task = Task(id="task-1", requirements="capability-1")
    orchestrator.assign_task(task)
    self.assertIn(task, orchestrator.engine.tasks)