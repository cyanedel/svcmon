import subprocess
from dal.port_status_history_repository import Repository

class PortStatusService:
  def __init__(self):
    pass
  
  def get_port_list(self):
    with Repository() as PortStatusDAO:
      return PortStatusDAO.get_port_list()

  def subprocess_check_port_multiple(self, ports):
    result_ss = subprocess.run(["ss", "-tulnp"], capture_output=True, text=True)
    result = []

    for port in ports:
      if f":{port} " in result_ss.stdout:
        result.append((port, True))
      else:
        result.append((port, False))

    return result
  
  def subprocess_check_port_single(self, port):
    result_ss = subprocess.run(["ss", "-tulnp"], capture_output=True, text=True)
    result = []

    if f":{port} " in result_ss.stdout:
      result.append((port, True))
    else:
      result.append((port, False))

    return result
  
  def save_port_status(self, data):
    with Repository() as PortStatusDAO:
      PortStatusDAO.save_port_status(data)
      return True
  
  def check_port_multiple(self):
    port_list = self.get_port_list()
    result = self.subprocess_check_port_multiple(port_list)
    for item in result:
      data = {"port": item[0], "state": item[1]}
      self.save_port_status(data)
  
  def get_port_history(self, port_no):
    with Repository() as PortStatusDAO:
      result = PortStatusDAO.get_history_minimum(port_no)
      return result

if __name__ == "__main__":
    statusService = PortStatusService()
    ports = statusService.get_port_list()
    result = statusService.subprocess_check_port_multiple(ports)
    print(result)