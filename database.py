import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = self.con.cursor()
        self.create_task_table()

    # The task table
    def create_task_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT, task varchar(50) NOT NULL, due_date varchar(50), completed BOOLEAN NOT NULL CHECK (completed IN (0,1)))")
        self.con.commit()

    # The task
    def create_task(self, task, due_date=None):
        self.cursor.execute("INSERT INTO tasks(task, due_date, completed) VALUES(?,?,?)", (task, due_date, 0))
        self.con.commit()

        # Get the last entered item and add to task list
        created_task = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE task = ? and completed = 0", (task,)).fetchall()
        return created_task[-1]
    
    # Get the tasks
    def get_tasks(self):
        '''Getting all the tasks : completed and incompleted'''
        incompleted_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 0").fetchall()
        completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()
        return completed_tasks, incompleted_tasks
    

    # Update the tasks
    def mark_task_as_completed(self, taskid):
        '''Mark tasks as completed'''
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (taskid,))
        self.con.commit()

    def mark_task_as_incompleted(self, taskid):
        '''Mark tasks as incompleted'''
        self.cursor.execute("UPDATE tasks SET completed = 0 WHERE id = ?", (taskid,))
        self.con.commit()

        # Return the task text
        task_text = self.cursor.execute("SELECT task FROM tasks WHERE id = ?", (taskid,)).fetchall()
        return task_text[0][0]
    
    # Delete the task
    def delete_task(self, taskid):
        '''Delete a task'''
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (taskid,))
        self.con.commit()

    # Close the connection
    def close_db_connection(self):
        self.con.close()





