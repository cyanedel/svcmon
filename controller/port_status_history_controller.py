from service.port_status_history_service import PortStatusService

class PortStatusController:
  def __init__(self):
    self.PortStatusService = PortStatusService()
  
  def get_port_list(self):
    return self.PortStatusService.get_port_list()
  
  def test_check_port_multiple(self):
    port_list = self.get_port_list()
    result = self.PortStatusService.subprocess_check_port_multiple(port_list)
    return result
  
  def test_check_port_single(self, port_no):
    result = self.PortStatusService.subprocess_check_port_single(port_no)
    return result
  
  def perform_check_port_multiple(self):
    self.PortStatusService.check_port_multiple()

  def get_port_history(self, port_no):
    result = self.PortStatusService.get_port_history(port_no)
    return result