from service.port_status_history_service import PortStatusService

class PortStatusController:
  def __init__(self):
    self.PortStatusService = PortStatusService()
  
  def get_port_list(self):
    return self.PortStatusService.get_port_list()
  
  def check_port(self, port_no):
    result = self.PortStatusService.check_port_status(port_no)
    return result
  
  def check_port_list(self):
    port_list = self.get_port_list()
    result = self.PortStatusService.check_port_list_status(port_list)
    return result