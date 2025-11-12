import subprocess
from dal.disk_history_repository import Repository

class DiskHistoryService:
  def __init__(self):
    pass

  def get_fs_list(self) -> tuple:
    with Repository() as DiskHistoryDAO:
      return DiskHistoryDAO.get_filesystem_list()

  def subprocess_check_disk_space(self) -> list[dict[str,str]]:
    result_df = subprocess.run(["df", "-k"], capture_output=True, text=True)
    lines = result_df.stdout.strip().split("\n")

    # header = lines[0].split()
    header = ["filesystem", "size", "used", "available", "mount_point"]
    data = [line.split() for line in lines[1:]]
    fs = self.get_fs_list()

    data_filter = [row for row in data if row[0] in fs]
    data_dict = [dict(zip(header, row)) for row in data_filter]

    return data_dict
  
  def save_disk_space_data(self, data: dict) -> bool:
    with Repository() as DiskHistoryDAO:
      DiskHistoryDAO.save_disk_space_data(data)
      return True

  def check_disk_space(self) -> None:
    disk_list = self.subprocess_check_disk_space()
    for data in disk_list:
      self.save_disk_space_data(data)
  
  def get_disk_log(self, disk_name: str) -> list:
    with Repository() as DiskHistoryDAO:
      return DiskHistoryDAO.get_disk_log(disk_name)