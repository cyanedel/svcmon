from service.disk_history_service import DiskHistoryService

class DiskStatusController:
  def __init__(self):
    self.DiskHistoryService = DiskHistoryService()
  
  def get_fs_list(self):
    return self.DiskHistoryService.get_fs_list()
  
  def check_disk_space(self):
    self.DiskHistoryService.check_disk_space()
    return True
  
  def test_check_disk_space(self):
    result = self.DiskHistoryService.subprocess_check_disk_space()
    return result