from requests import Response

from rest import RestClient


class ScyllaRestClient(RestClient):
    def __init__(self, host: str = "localhost", port: str = "10000"):
        super().__init__(host=host, port=port)

    def get_raw_api_json(self, resource_path: str = ""):
        if api := self.get(f"/api-doc{resource_path}"):
            return api.json()
        return None

    def get(self, resource_path: str, query_params: dict = None):
        return super().get(resource_path=resource_path, query_params=query_params)

    def post(self, resource_path: str, query_params: dict = None, json: dict = None):
        return super().post(resource_path=resource_path, query_params=query_params, json=json)

    def delete(self, resource_path: str, query_params: dict = None):
        return super().delete(resource_path=resource_path, query_params=query_params)

    def dispatch_rest_method(self, rest_method_kind: str, **kwargs) -> Response:
        method_to_call_dict = {
            "GET": self.get,
            "POST": self.post,
            "DELETE": self.delete
        }

        return method_to_call_dict[rest_method_kind](**kwargs)


