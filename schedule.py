from service.service_status_history_service import ServiceStatusService
from service.port_status_history_service import PortStatusService
from dal.service_status_history_repository import Repository as ServiceStatusRepository

if __name__ == "__main__":
  ServiceStsDAO = ServiceStatusRepository()
  ServiceStsService = ServiceStatusService()
  PortStsService = PortStatusService()

  services = ServiceStsDAO.get_service_list()
  serviceCheckResult = []
  
  for service in services:
    result = ServiceStsService.check_service_status(service)
    serviceCheckResult.append(result)
    ServiceStsDAO.save_service_status(result)

  print(serviceCheckResult)

  PortStsService.check_port_multiple()