from proteus_lab_assistant.tasks import available_tasks, get_task

def test_tasks_available():
    assert "task1_xnor" in available_tasks()

def test_task_has_components():
    assert get_task("task1_xnor")["components"]
