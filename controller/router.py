from controller.service_status_history_controller import ServiceController
from service.response_service import ResponseService as Response
from controller.error_controller import HTTPError

class APIGetRouter:
  def __init__(self):
    self.ServiceController = ServiceController()

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
      result = self.ServiceController.get_service_list()
      return result
    
    elif subpath == "service/check":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceController.check_service(service_name)
        return result
      else:
        raise HTTPError(400, Response.MSG_400)
      
    elif subpath == "service/history":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceController.get_history_minimum(service_name)
        print(result)
        return result
      else:
        raise HTTPError(400, Response.MSG_400)