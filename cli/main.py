import argparse
import sys
from services.orchestrator import OrchestratorService

def main():
  parser = argparse.ArgumentParser(description="Distributed Agent Orchestrator")
  parser.add_argument("--register-agent", action="store_true", help="Register agent")
  parser.add_argument("--assign-task", action="store_true", help="Assign task")
  args = parser.parse_args()
  orchestrator = OrchestratorService()

  if args.register_agent:
    agent = Agent(id="agent-1", capabilities=["capability-1"])
    orchestrator.register_agent(agent)
  elif args.assign_task:
    task = Task(id="task-1", requirements="capability-1")
    orchestrator.assign_task(task)
    orchestrator.execute_tasks()
    orchestrator.report_progress()

if __name__ == "__main__":
  main()