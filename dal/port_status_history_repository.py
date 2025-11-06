import os
import sqlite3
import time

class Repository:
  def __init__(self, db_name="data.db"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, db_name)
    self.conn = sqlite3.connect(db_path)
    self.cur = self.conn.cursor()

  def save_status(self, port_data):
    self.cur.execute("INSERT INTO port_log (port, status, datetime) VALUES (?, ?, ?, ?)", (port_data.get("port"), port_data.get("state"), time.time()))
    self.conn.commit()

  def select_users(self, service_name, limit):
    self.cur.execute("SELECT name, status, datetime FROM port_log WHERE name=? LIMIT ?", (service_name, limit))
    return self.cur.fetchall()

  def close(self):
    self.conn.close()