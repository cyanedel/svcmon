from controller.service_status_history_controller import ServiceStatusController
from controller.port_status_history_controller import PortStatusController
from controller.disk_history_controller import DiskStatusController
from controller.memory_history_controller import MemoryStatusController
from service.response_service import ResponseService as Response
from controller.error_controller import HTTPError

class APIGetRouter:
  def __init__(self):
    self.ServiceStatusController = ServiceStatusController()
    self.PortStatusController = PortStatusController()
    self.DiskStatusController = DiskStatusController()
    self.MemoryStatusController = MemoryStatusController()

  def get_handler(self, subpath, params):
    if subpath == "ping":
      return {"status": Response.MSG_200}
    
    elif subpath == "service/list":
      result = self.ServiceStatusController.get_service_list()
      return result
    
    elif subpath == "service/restart":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceStatusController.restart_service(service_name)
        if result is True:
          return {"status": Response.MSG_200}
        else:
          raise HTTPError(403, Response.MSG_403)
      else:
        raise HTTPError(400, Response.MSG_400)
    
    elif subpath == "service/check":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceStatusController.test_check_service_single(service_name)
        return result
      else:
        raise HTTPError(400, Response.MSG_400)
      
    elif subpath == "service/history":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceStatusController.get_service_history(service_name)
        return result
      else:
        raise HTTPError(400, Response.MSG_400)
    
    elif subpath == "port/list":
      result = self.PortStatusController.get_port_list()
      return result
    
    elif subpath == "port/check":
      port_no = params.get("port_number", [None])[0]
      if port_no is not None:
        result = self.PortStatusController.test_check_port_single(port_no)
        return result
      else:    
        raise HTTPError(400, Response.MSG_400)
    
    elif subpath == "port-list/check":
      result = self.PortStatusController.test_check_port_multiple()
      return result
    
    elif subpath == "port/history":
      port_number = params.get("port_number", [None])[0]
      if port_number is not None:
        result = self.PortStatusController.get_port_history(port_number)
        return result
      else:    
        raise HTTPError(400, Response.MSG_400)
    
    elif subpath == "disk/list":
      result = self.DiskStatusController.get_fs_list()
      return result
    
    elif subpath == "disk/check":
      result = self.DiskStatusController.test_check_disk_space()
      return result
    
    elif subpath == "disk/history":
      disk_name = params.get("disk_name", [None])[0]
      if disk_name is not None:
        result = self.DiskStatusController.get_disk_log(disk_name)
        return result
      else:    
        raise HTTPError(400, Response.MSG_400)
    
    # elif subpath == "disk/check-save":
    #   self.DiskStatusController.check_disk_space()
    #   return {"status": Response.MSG_200}
    
    elif subpath == "memory/check":
      result = self.MemoryStatusController.test_check_memory()
      return result
    
    # elif subpath == "memory/check-save":
    #   self.MemoryStatusController.check_memory()
    #   return {"status": Response.MSG_200}
    
    elif subpath == "memory/history":
      memory_type = params.get("memory_type", [None])[0]
      if memory_type is not None:
        result = self.MemoryStatusController.get_memory_log(memory_type)
        return result
      else:    
        raise HTTPError(400, Response.MSG_400)
    
class APIPostRouter:
  def __init__(self):
    self.ServiceStatusController = ServiceStatusController()
  
  def post_handler(self, subpath, body):
    if subpath == "ping":
      return {"status": Response.MSG_200}
    
    # elif subpath == "service/restart":
    #   service_name = params.get("service_name", [None])[0]
    #   if service_name is not None:
    #     result = self.ServiceStatusController.restart_service(service_name)
    #     if result is True:
    #       return {"status": Response.MSG_200}
    #     else:
    #       raise HTTPError(403, Response.MSG_403)
    #   else:
    #     raise HTTPError(400, Response.MSG_400)
