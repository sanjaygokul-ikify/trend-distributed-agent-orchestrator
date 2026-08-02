import unittest
from packages.core import Agent, Task, Engine

class TestCore(unittest.TestCase):
  def test_agent_registration(self):
    engine = Engine(KnowledgeGraph())
    agent = Agent(id="agent-1", capabilities=["capability-1"])
    engine.register_agent(agent)
    self.assertIn(agent.id, engine.agents)

  def test_task_assignment(self):
    engine = Engine(KnowledgeGraph())
    task = Task(id="task-1", requirements="capability-1")
    engine.assign_task(task)
    self.assertIn(task, engine.tasks)

  def test_task_execution(self):
    engine = Engine(KnowledgeGraph())
    task = Task(id="task-1", requirements="capability-1")
    agent = Agent(id="agent-1", capabilities=["capability-1"])
    engine.register_agent(agent)
    engine.assign_task(task)
    engine.execute_tasks()
    self.assertEqual(task.status, "pending")