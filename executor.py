def execute_task(task_type):
    if task_type == 'system_info':
        return "Simulated system information"

    elif task_type == 'health_check':
        return "Agent simulation is healthy"

    else:
        return None