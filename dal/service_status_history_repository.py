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
    query = "INSERT INTO service_log (name, status, datetime, datetime_lastactive) VALUES (?, ?, ?, ?)"
    self.cur.execute(query, (
      service_data.get("service")
      , service_data.get("state")
      , time.time()
      , service_data.get("last")
    ))
    self.conn.commit()

  def get_history_by_limit(self, service_name, limit):
    query = "SELECT name, status, datetime FROM service_log WHERE name=? LIMIT ?"
    self.cur.execute(query, (service_name, limit))
    return self.cur.fetchall()

  def get_history_minimum(self, service_name):
    query = "SELECT name, status, datetime" \
    ", strftime('%Y', datetime, 'unixepoch') AS year" \
    ", strftime('%m', datetime, 'unixepoch') AS month" \
    ", strftime('%d', datetime, 'unixepoch') AS day" \
    ", strftime('%H', datetime, 'unixepoch') AS hour" \
    " FROM service_log WHERE name=? AND datetime >= strftime('%s', 'now', '-3 days')"
    self.cur.execute(query, (service_name,))
    return self.cur.fetchall()

  def close(self):
    self.conn.close()
  
if __name__ == "__main__":
  ServiceRepository = Repository()
  result = ServiceRepository.get_history_minimum(service_name="webconsole")
  print(result)