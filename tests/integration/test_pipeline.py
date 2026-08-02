import unittest
from cli.main import main
from packages.core import Agent, Task

class TestPipeline(unittest.TestCase):
  def test_full_pipeline(self):
    # Register agent
    parser = unittest.mock.Mock()
    parser.register_agent = True
    main()

    # Assign task
    parser.register_agent = False
    parser.assign_task = True
    main()

    # Check task status
    task = Task(id="task-1", requirements="capability-1")
    self.assertEqual(task.status, "pending")