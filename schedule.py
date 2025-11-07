from service.service_status_history_service import ServiceStatusService
from service.port_status_history_service import PortStatusService

if __name__ == "__main__":
  ServiceStsService = ServiceStatusService()
  PortStsService = PortStatusService()

  ServiceStsService.check_service_multiple()
  PortStsService.check_port_multiple()