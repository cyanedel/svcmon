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

  def get_filesystem_list(self):
    query = "SELECT filesystem FROM disk"
    self.cur.execute(query)
    rows = self.cur.fetchall()
    return tuple(zip(*rows))[0] if rows else ()

  def save_disk_space_data(self, data):
    self.cur.execute("INSERT INTO disk_log (filesystem, size, used, avail, unix_created) VALUES (?, ?, ?, ?, ?)", (data.get("filesystem"), data.get("size"), data.get("used"), data.get("available"), int(time.time())))
    self.conn.commit()

if __name__ == "__main__":
  DiskRepository = Repository()
  result = DiskRepository.get_filesystem_list()
  print(result)