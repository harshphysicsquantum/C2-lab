import sqlite3


def get_db_resource():
    conn = get_connection()
    cursor = conn.cursor()
    return conn, cursor


def add_task(task_type):
    conn, cursor = get_db_resource()
    cursor.execute(
    "INSERT INTO tasks (task_type) VALUES (?)",
    (task_type, )
    )
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id


def update_task_status(task_id, new_status):
    conn, cursor = get_db_resource()
    status = ["pending", "completed", "running"]
    if new_status in status:
        cursor.execute("""UPDATE tasks SET status = ? WHERE task_id = ?""", (new_status, task_id))
        conn.commit()
        if cursor.rowcount == 0:
            print("Task not found")
        else:
            print("Task updated successfully")
        conn.close()
    else:
        print("Invalid status")
        conn.close()

def get_pending_tasks():
    conn, cursor = get_db_resource()
    cursor.execute("SELECT * FROM tasks WHERE status = 'pending'")
    pending = cursor.fetchall()
    conn.close()
    return pending

def get_next_pending_task():
    conn, cursor = get_db_resource()
    cursor.execute("SELECT * FROM tasks WHERE status = 'pending' ORDER BY task_id ASC LIMIT 1")
    pending = cursor.fetchone()
    conn.close()
    return pending 

def get_connection():
    connection = sqlite3.connect("c2_lab.db")
    return connection


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY,
        task_type TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def get_task_by_id(task_id):
    conn, cursor = get_db_resource()
    cursor.execute('''SELECT * FROM tasks WHERE task_id = ?''', (task_id, ))
    find_task = cursor.fetchone()
    conn.close()
    return find_task
