import subprocess
from dal.memory_history_repository import Repository

class MemoryHistoryService:
  def __init__(self):
    pass

  def subprocess_check_disk_space(self) -> list[dict[str,str]]:
    result_cmd = subprocess.run(["free", "-k"], capture_output=True, text=True)
    lines = result_cmd.stdout.strip().split("\n")

    # headers = lines[0].split()
    headers = ["type", "total", "used", "free", "available"]
    mem_values = lines[1].split()
    mem_values[0] = "memory"
    mem_info = dict(zip(headers, mem_values))

    if len(lines) > 2:
        swap_values = lines[2].split()
        swap_values[0] = "swap"
        swap_info = dict(zip(headers, swap_values))
    else:
        swap_info = {}


    return [mem_info, swap_info]
  
  def save_memory_data(self, data: dict):
    with Repository() as MemoryHistoryDAO:
       MemoryHistoryDAO.save_memory_data(data)
  
  def check_memory(self):
    memory_list = self.subprocess_check_disk_space()
    for data in memory_list:
       self.save_memory_data(data)
  
  def get_memory_log(self, memory_type: str) -> list:
    with Repository() as MemoryHistoryDAO:
      return MemoryHistoryDAO.get_memory_log(memory_type)