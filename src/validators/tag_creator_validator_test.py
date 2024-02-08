from .tag_creator_validator import tag_creator_validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    req = MockRequest(json={"product_code": "12345"})
    response = tag_creator_validator(req)
    
def test_tag_creator_validator_with_error():
    req = MockRequest(json={"product_code": 12345})
    try:
        response = tag_creator_validator(req)
    except Exception as exception:
        assert isinstance(exception,HttpUnprocessableEntityError)