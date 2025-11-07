from controller.service_status_history_controller import ServiceStatusController
from controller.port_status_history_controller import PortStatusController
from service.response_service import ResponseService as Response
from controller.error_controller import HTTPError

class APIGetRouter:
  def __init__(self):
    self.ServiceStatusController = ServiceStatusController()
    self.PortStatusController = PortStatusController()

  def get_handler(self, subpath, params):
    # parts = [p for p in subpath.split("/") if p]
    # if not parts:
    #     self._json_response({"error": "Invalid API path"}, 404)
    #     return

    # print("subpath: "+subpath)
    # print("params:")
    # print(params)

    if subpath == "ping":
      return {"status": Response.MSG_200}
    
    elif subpath == "service/list":
      result = self.ServiceStatusController.get_service_list()
      return result
    
    elif subpath == "service/check":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceStatusController.check_service(service_name)
        return result
      else:
        raise HTTPError(400, Response.MSG_400)
      
    elif subpath == "service/history":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceStatusController.get_history_minimum(service_name)
        return result
      else:
        raise HTTPError(400, Response.MSG_400)
    
    elif subpath == "port/check":
      port_no = params.get("port_number", [None])[0]
      if port_no is not None:
        result = self.PortStatusController.check_port(port_no)
        return result
      else:    
        raise HTTPError(400, Response.MSG_400)
    
    elif subpath == "port-list/check":
      result = self.PortStatusController.check_port_list()
      return result