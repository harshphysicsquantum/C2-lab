import database

database.init_db()

task_id = database.add_task("test_task")
print("Created task:", database.get_task_by_id(task_id))

print("\nTest 1: pending -> running")
database.update_task_status(task_id, "running")
print("Current task:", database.get_task_by_id(task_id))

print("\nTest 2: running -> completed")
database.update_task_status(task_id, "completed")
print("Current task:", database.get_task_by_id(task_id))

print("\nTest 3: completed -> running")
database.update_task_status(task_id, "running")
print("Current task:", database.get_task_by_id(task_id))

print("\nTest 4: nonexistent task")
database.update_task_status(999999, "running")


# Test 5: running -> failed
task_id = database.add_task("failure_test")
print("\nTest 5: running -> failed")
database.update_task_status(task_id, "running")
database.update_task_status(task_id, "failed")
print("Current task:", database.get_task_by_id(task_id))
