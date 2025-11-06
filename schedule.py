from service.service_status_history_service import ServiceStatusService
from dal.service_status_history_repository import Repository as ServiceStatusRepository

if __name__ == "__main__":
  services = ("safepc", "webconsole", "secuprint", "mariadb")
  serviceDAO = ServiceStatusRepository()
  serviceStsService = ServiceStatusService()
  for service in services:
    result = serviceStsService.check_service_status(service)
    serviceDAO.save_status(result)