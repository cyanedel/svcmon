from service.service_status_history_service import ServiceStatusService

class ServiceController:
  def __init__(self):
    self.ServiceStatusService = ServiceStatusService()

  def check_service(self, service_name):
    result = self.ServiceStatusService.check_service_status(service_name)
    self.ServiceStatusService.save_status(result)
    return result
  
  def get_history_minimum(self, service_name):
    return self.ServiceStatusService.get_history_minimum(service_name)
  
if __name__ == "__main__":
  SvcControl = ServiceController()
  result = SvcControl.get_history_minimum("webconsole")
  print(result)