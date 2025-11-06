import os
import sqlite3
import time
from datetime import datetime

class Repository:
  def __init__(self, db_name="data.db"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, db_name)
    self.conn = sqlite3.connect(db_path)
    self.cur = self.conn.cursor()

  def save_status(self, service_data):
    query = "INSERT INTO service_log (name, load, status, substate, unix_created, unix_last_active) VALUES (?, ?, ?, ?, ?, ?)"
    self.cur.execute(query, (
      service_data.get("service")
      , service_data.get("load")
      , service_data.get("state")
      , service_data.get("substate")
      , int(time.time())
      , service_data.get("last_active_unix")
    ))
    self.conn.commit()

  def get_history_by_limit(self, service_name, limit):
    query = "SELECT name, status, unix_created FROM service_log WHERE name=? LIMIT ?"
    self.cur.execute(query, (service_name, limit))
    return self.cur.fetchall()

  def get_history_minimum(self, service_name):
    query = "SELECT name, load, status, substate, unix_created" \
      ", strftime('%Y', unix_created, 'unixepoch') AS year" \
      ", strftime('%m', unix_created, 'unixepoch') AS month" \
      ", strftime('%d', unix_created, 'unixepoch') AS day" \
      ", strftime('%H', unix_created, 'unixepoch') AS hour" \
      " FROM service_log WHERE name=? AND unix_created >= strftime('%s', 'now', '-3 days')"
    self.cur.execute(query, (service_name,))
    return self.cur.fetchall()

  def close(self):
    self.conn.close()
  
if __name__ == "__main__":
  ServiceRepository = Repository()
  result = ServiceRepository.get_history_minimum(service_name="webconsole")
  print(result)