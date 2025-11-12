from datetime import datetime
from service.service_status_history_service import ServiceStatusService
from service.port_status_history_service import PortStatusService
from service.disk_history_service import DiskHistoryService
from service.memory_history_service import MemoryHistoryService

if __name__ == "__main__":
  now = datetime.now()
  ServiceStsService = ServiceStatusService()
  PortStsService = PortStatusService()
  DiskService = DiskHistoryService()
  MemoryService = MemoryHistoryService()

  ServiceStsService.check_service_multiple()
  PortStsService.check_port_multiple()
  MemoryService.check_memory()
  if now.weekday() == 4 and now.hour() >= 23 and now.minute <= 5:
    DiskService.check_disk_space()