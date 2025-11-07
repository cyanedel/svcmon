from service.service_status_history_service import ServiceStatusService
from dal.service_status_history_repository import Repository as ServiceStatusRepository

if __name__ == "__main__":
  serviceDAO = ServiceStatusRepository()
  serviceStsService = ServiceStatusService()

  services = serviceDAO.get_service_list()
  serviceCheckResult = []
  
  for service in services:
    result = serviceStsService.check_service_status(service)
    serviceCheckResult.append(result)
    serviceDAO.save_service_status(result)

  print(serviceCheckResult)