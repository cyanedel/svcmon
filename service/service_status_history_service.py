import subprocess
from datetime import datetime
from dal.service_status_history_repository import Repository

class ServiceStatusService:
  def __init__(self):
    pass
  
  def get_service_list(self):
    with Repository() as ServiceStatusDAO:
      return ServiceStatusDAO.get_service_list()
    
  def subprocess_check_service(self, service_name):
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
      
    return {"service": service_name, "load": load, "state": state, "substate": sub, "last_active": last, "last_active_unix": unix_time}
  
  def subprocess_restart_service(self, service_name):
    services = self.get_service_list()
    if service_name in services:
      cmd = ["systemctl", "restart", service_name+".service"]
      subprocess.run(cmd)
      return True
    else:
      return False
  
  def save_service_status(self, data):
    with Repository() as ServiceStatusDAO:
      ServiceStatusDAO.save_service_status(data)
  
  def get_service_history(self, service_name):
    with Repository() as ServiceStatusDAO:
      return ServiceStatusDAO.get_history_minimum(service_name)
  
  def test_check_service_multiple(self):
    service_list = self.get_service_list()
    service_check_result = []
    for service_name in service_list:
      data = self.subprocess_check_service(service_name)
      service_check_result.append(data)
    return service_check_result

  def check_service_multiple(self):
    service_list = self.get_service_list()
    for service_name in service_list:
      data = self.subprocess_check_service(service_name)
      self.save_service_status(data)

if __name__ == "__main__":
    statusService = ServiceStatusService()
    # result = statusService.check_service_status("mariadb")
    result = statusService.get_service_history("webconsole")
    print(result)