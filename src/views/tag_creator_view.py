from src.views.http_types.http_requests import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
  '''
    responsability for interact with HTTP
  '''
  
  def validade_and_create(self, http_request: HttpRequest) -> HttpResponse:
    body = http_request.body
    product_code = body['product_code']
    print("mae, to na globo")
    return HttpResponse(status_code=200, body={"hello":"world"})