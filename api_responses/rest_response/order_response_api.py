import jsonpath

class OrderResponse:
    """
    Order response object.
    """

    def __init__(self, response):
        """
        :type response: object
        """
        response_json = response.json()
        print(response_json)
        self.status_code = response.status_code
        if int(self.status_code) == 200 or int(self.status_code) == 201:
            self.order_id = jsonpath.jsonpath(response_json, 'order_id')[0]
            self.id = jsonpath.jsonpath(response_json, 'id')[0]
            self.symbol = jsonpath.jsonpath(response_json, 'symbol')[0]
            self.exchange = jsonpath.jsonpath(response_json, 'exchange')[0]
            self.price = jsonpath.jsonpath(response_json, 'price')[0]
            self.executed_amount = jsonpath.jsonpath(response_json, 'executed_amount')[0]
            self.original_amount = jsonpath.jsonpath(response_json, 'original_amount')[0]
            self.remaining_amount = jsonpath.jsonpath(response_json, 'remaining_amount')[0]
            self.type = jsonpath.jsonpath(response_json, 'type')[0]
            self.reason = None
        else:
            self.result = jsonpath.jsonpath(response_json, 'result')[0]
            self.reason = jsonpath.jsonpath(response_json, 'reason')[0]
            self.message = jsonpath.jsonpath(response_json, 'message')[0]
            self.order_id = None
            self.id = None
            self.symbol = None
            self.exchange = None
            self.price = None
            self.original_amount = None
            self.remaining_amount = None
            self.remaining_amount = None
            self.type = None

