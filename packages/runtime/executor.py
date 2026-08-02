from typing import List
from logging import getLogger
from ..core.engine import Engine
from ..core.types import Agent, Task

logger = getLogger(__name__)


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, task_list: List[Task]):
        for task in task_list:
            try:
                self.engine.execute_tasks()
                logger.info(f"Task {task.id} executed")
            except Exception as e:
                logger.error(f"Error executing task {task.id}: {str(e)}")
                raise OrchestrationError(f"Error executing task {task.id}: {str(e)}")

    def report_progress(self, task_list: List[Task]):
        for task in task_list:
            try:
                self.engine.report_progress()
                logger.info(f"Task {task.id} progress reported")
            except Exception as e:
                logger.error(f"Error reporting progress of task {task.id}: {str(e)}")
                raise OrchestrationError(f"Error reporting progress of task {task.id}: {str(e)}")