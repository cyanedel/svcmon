from controller.service_status_history_controller import ServiceController
from service.response_service import ResponseService as Response

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
      return {"status": Response.MSG_200, "status_code": Response.CODE_200}
    
    elif subpath == "service/check":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceController.check_service(service_name)
        return {"status": Response.MSG_200, "status_code": Response.CODE_200, "data": result}
      else:
        return {"status": Response.MSG_403, "status_code": Response.CODE_403}
      
    elif subpath == "service/history":
      service_name = params.get("service_name", [None])[0]
      if service_name is not None:
        result = self.ServiceController.get_history_minimum(service_name)
        print(result)
        return {"status": Response.MSG_200, "status_code": Response.CODE_200, "data": result}
      else:
        return {"status": Response.MSG_403, "status_code": Response.CODE_403}