import json
import requests
import logging

class APIConfig:
    """
    API config object will be used for api calls.
    Attributes:
        base_url : base url
        end_point : relative url
        content_type : content type in header
        accept_type : accept type in header
        headers : headers
        key: gemini key for the api
        secret_key : gemini secret Key
        auth : auth for HTTP calls
        params : params for API call
        time_out : configurable timeout for API call
    """

    def __init__(self):
        self.base_url = None
        self.end_point = None
        self.content_type = None
        self.accept_type = None
        self.headers = {'Content-Type': 'application/json'}
        self.key = None
        self.secret_key = None
        self.auth = None
        self.params = None
        self.time_out = 120


class RestClass:
    @staticmethod
    def post(config: APIConfig, data=None, json_data=None):
        """
        Makes a get HTTP POST call and returns APIResponse object.
        APIResponse object will be with data from POST call.
        :param config: APIConfig object
        :param data: message body
        :param json_data: message body
        :return: APIResponse response object with data from POST call
        """
        global response
        if data is None:
            data = {}
        url = config.base_url+config.end_point
        if 'json' in config.headers.get('Content-Type', []):
            try:
                json_string = json.dumps(data)
            except json.JSONDecodeError:
                raise Exception("Invalid JSON Format , Please check message body")
            payload = json_string
        else:
            payload = data
        try:
            response = None
            if data:
                response = requests.post(url=url, params=config.params,
                                         data=payload,
                                         headers=config.headers,
                                         timeout=config.time_out,
                                         auth=config.auth)
            elif json_data:
                response = requests.post(url=url, params=config.params,
                                         json=json_data,
                                         headers=config.headers,
                                         timeout=config.time_out,
                                         auth=config.auth)



        except requests.exceptions.RequestException as ex:
            logging.log("{err_name} on POST call for url: {url} \n {err_msg}"
                                            .format(err_name=ex.__class__.__name__, url=url,
                                                    err_msg="Error in the post request"))
        return response
