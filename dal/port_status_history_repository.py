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

  def get_port_list(self):
    query = "SELECT port FROM port WHERE enabled=?"
    self.cur.execute(query, (1,))
    rows = self.cur.fetchall()
    return tuple(zip(*rows))[0] if rows else ()

  def save_port_status(self, port_data):
    self.cur.execute("INSERT INTO port_log (port, state, unix_created) VALUES (?, ?, ?)", (port_data.get("port"), port_data.get("state"), int(time.time())))
    self.conn.commit()

  def get_history_minimum(self, port_no):
    query = "SELECT port, state, unix_created" \
      ", strftime('%Y', unix_created, 'unixepoch', 'localtime') AS year" \
      ", strftime('%m', unix_created, 'unixepoch', 'localtime') AS month" \
      ", strftime('%d', unix_created, 'unixepoch', 'localtime') AS day" \
      ", strftime('%H', unix_created, 'unixepoch', 'localtime') AS hour" \
      " FROM port_log WHERE port=?" \
      " AND unix_created >= strftime('%s', 'now', '-3 days')" \
      " ORDER BY unix_created DESC"
    self.cur.execute(query, (port_no,))
    return self.cur.fetchall()

if __name__ == "__main__":
  PortRepository = Repository()
  result = PortRepository.get_port_list()
  print(result)