import subprocess
from dal.port_status_history_repository import Repository

class PortStatusService:
  def __init__(self):
    self.PortStatusDAO = Repository()
  
  def get_port_list(self):
    return self.PortStatusDAO.get_port_list()

  def check_port_list_status(self, ports):
    ss_result = subprocess.run(["ss", "-tulnp"], capture_output=True, text=True)
    result = []

    for port in ports:
      if f":{port} " in ss_result.stdout:
        result.append((port, True))
      else:
        result.append((port, False))

    return result
  
  def check_port_status(self, port):
    ss_result = subprocess.run(["ss", "-tulnp"], capture_output=True, text=True)
    result = []

    if f":{port} " in ss_result.stdout:
      result.append((port, True))
    else:
      result.append((port, False))

    return result
  
  def save_port_status(self, data):
    return self.PortStatusDAO.save_port_status(data)

if __name__ == "__main__":
    statusService = PortStatusService()
    ports = statusService.get_port_list()
    result = statusService.check_port_status(ports)
    print(result)