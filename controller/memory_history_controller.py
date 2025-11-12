from service.memory_history_service import MemoryHistoryService

class MemoryStatusController:
  def __init__(self):
    self.MemoryHistoryService = MemoryHistoryService()
  
  def get_memory_log(self, memory_type: str) -> list:
    return self.MemoryHistoryService.get_memory_log(memory_type)
  
  def check_memory(self):
    self.MemoryHistoryService.check_memory()
    return True
  
  def test_check_memory(self):
    result = self.MemoryHistoryService.subprocess_check_disk_space()
    return result