from service.service_status_history_service import ServiceStatusService

class ServiceStatusController:
  def __init__(self):
    self.ServiceStatusService = ServiceStatusService()
  
  def get_service_list(self):
    return self.ServiceStatusService.get_service_list()

  def test_check_service_multiple(self):
    result = self.ServiceStatusService.test_check_service_multiple()
    return result
  
  def get_history_minimum(self, service_name):
    return self.ServiceStatusService.get_history_minimum(service_name)
  
if __name__ == "__main__":
  SvcControl = ServiceStatusController()
  result = SvcControl.get_history_minimum("webconsole")
  print(result)