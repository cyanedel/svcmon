import os
import sqlite3
import time

class Repository:
  def __init__(self, db_name="data.db"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, db_name)
    self.conn = sqlite3.connect(db_path)
    self.cur = self.conn.cursor()

  def __enter__(self):
      return self

  def __exit__(self, exc_type, exc_value, traceback):
      self.conn.close()

  def save_memory_data(self, data: dict) -> None:
    self.cur.execute("INSERT INTO memory_log (memory_type, total, used, free, available, unix_created) VALUES (?, ?, ?, ?, ?, ?)", (data.get("type"), data.get("total", 0), data.get("used", 0), data.get("free", 0), data.get("available", 0), int(time.time())))
    self.conn.commit()

  def get_memory_log(self, memory_type):
    query = "SELECT memory_type, total, used, free, available, unix_created" \
      ", strftime('%Y', unix_created, 'unixepoch', 'localtime') AS year" \
      ", strftime('%m', unix_created, 'unixepoch', 'localtime') AS month" \
      ", strftime('%d', unix_created, 'unixepoch', 'localtime') AS day" \
      ", strftime('%H', unix_created, 'unixepoch', 'localtime') AS hour" \
      " FROM memory_log WHERE memory_type=?" \
      " AND unix_created >= strftime('%s', 'now', '-3 days')" \
      " ORDER BY unix_created DESC"
    self.cur.execute(query, (memory_type,))
    return self.cur.fetchall()