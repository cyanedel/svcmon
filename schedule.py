from service.service_status_history_service import ServiceStatusService
from dal.service_status_history_repository import Repository as ServiceStatusRepository

if __name__ == "__main__":
  services = ("safepc", "webconsole", "secuprint", "mariadb")
  serviceDAO = ServiceStatusRepository()
  for item in services:
    result = ServiceStatusService.get_service_status(item)
    serviceDAO.save_status(result)