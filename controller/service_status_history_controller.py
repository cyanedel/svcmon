from service.service_status_history_service import ServiceStatusService

class ServiceStatusController:
  def __init__(self):
    self.ServiceStatusService = ServiceStatusService()
  
  def get_service_list(self):
    return self.ServiceStatusService.get_service_list()
  
  def restart_service(self, service_name):
    return self.ServiceStatusService.subprocess_restart_service(service_name)

  def test_check_service_single(self, service_name):
    result = self.ServiceStatusService.subprocess_check_service(service_name)
    return result

  def test_check_service_multiple(self):
    result = self.ServiceStatusService.test_check_service_multiple()
    return result
  
  def get_service_history(self, service_name):
    return self.ServiceStatusService.get_service_history(service_name)
  
if __name__ == "__main__":
  SvcControl = ServiceStatusController()
  result = SvcControl.get_service_history("webconsole")
  print(result)