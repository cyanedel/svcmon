import subprocess
from datetime import datetime
from dal.service_status_history_repository import Repository as ServiceStatusRepository

class ServiceStatusService:
  def __init__(self):
    self.serviceStatusDAO = ServiceStatusRepository()
  
  def check_service_status(self, service_name):
    props = ["LoadState", "ActiveState", "SubState", "ActiveEnterTimestamp"]
    cmd = ["systemctl", "show", service_name, "--property=" + ",".join(props)]

    output    = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip().splitlines()
    data      = dict(line.split("=", 1) for line in output if "=" in line)
    load      = data.get("LoadState", "unknown")
    state     = data.get("ActiveState", "unknown")
    sub       = data.get("SubState", "unknown")
    last      = data.get("ActiveEnterTimestamp", None)
    unix_time = 0
    
    if len(last) > 0:
      dt = datetime.strptime(last, "%a %Y-%m-%d %H:%M:%S %Z")
      unix_time = int(dt.timestamp())
      print(service_name, last, unix_time )
      
    return {"service": service_name, "load": load, "state": state, "substate": sub, "last_active": last, "last_active_unix": unix_time}
  
  def save_status(self, result):
    self.serviceStatusDAO.save_status(result)
  
  def get_history_minimum(self, service_name):
    return self.serviceStatusDAO.get_history_minimum(service_name)

if __name__ == "__main__":
    service_name = "crond"  # example
    historyService = ServiceStatusService()
    result = historyService.check_service_status(service_name)
    print(f"Service: {result['service']}")
    print(f"Status: {result['status']}")
    print(f"Last active: {result['last_active']}")