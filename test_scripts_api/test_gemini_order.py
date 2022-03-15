import unittest
import time
from pytest import mark
from common_methods import assert_test, log_info
from constants import STATUS_CREATED, STATUS_BAD_REQUEST, STATUS_NOT_FOUND, STATUS_BAD_GATEWAY, STATUS_OK
from workflows_api.order_workflow import new_order_gemini


class Test_Gemini_Order_All_Cases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        log_info("****Executing the test cases in Test_Gemini_Order_All_Cases****")

    def setUp(self) -> None:
        log_info(f'####Executiong the test case##  : {self._testMethodName}')

    def tearDown(self) -> None:
        log_info("Executed test case")
    @classmethod
    def tearDownClass(cls) -> None:
        log_info("*****Execution Completed****")

    @mark.positive_case
    def test_order_gemini_post_validate_200_status_code(self):
        """
        validate 201 status code for the new order api
        """
        order_response, _ = new_order_gemini()
        if order_response.status_code == STATUS_OK:
            result_str = "Received the required status code as expected"
        else:
            result_str = f"Received incorrect status code as {order_response.status_code} instead of {STATUS_CREATED}"
        assert_test(order_response.status_code == STATUS_OK, result_str=result_str,
                    status_code=order_response.status_code)

    @mark.positive_case
    def test_order_validate_amount_executeamount_remainingamount(self):
        """
        validate the sum of (executed amount + remaining amount = amount)
        """
        order_response, payload = new_order_gemini()
        if order_response.status_code == STATUS_OK:
            get_executed_amt = float(order_response.executed_amount)
            get_remain_amt = float(order_response.remaining_amount)
            payload_amount = float(payload['amount'])
            if payload_amount == get_remain_amt + get_executed_amt:
                result_str = "payload amount is equal to remaining amount and executed amount"
                bool_result = True
            else:
                result_str = "payload amount is not equal to remaining amount and executed amount"
                bool_result = False
        else:
            result_str = "payload amount is not equal to remaining amount and executed amount"
            bool_result = False

        assert_test(bool_result, result_str=result_str,
                    status_code=order_response.status_code)

    @mark.positive_case
    def test_order_gemini_post_validate_200_price_in_request_response(self):
        """
        validate the price value in the request and response
        """
        order_response, payload = new_order_gemini()
        if order_response.status_code == STATUS_OK and order_response.price == payload['price'] :
            result_str = "The price in request and response match as expected"
        else:
            result_str = f"Price mismatch between the request price and response price."
        assert_test(order_response.status_code == STATUS_OK, result_str=result_str,
                    status_code=order_response.status_code)

    @mark.positive_case
    def test_order_gemini_post_validate_200_symbol_in_request_response(self):
        """
        validate the price value in the request and response
        """
        order_response, payload = new_order_gemini()
        if order_response.status_code == STATUS_OK and order_response.symbol == payload['symbol']:
            result_str = "The symbol value in request and response match as expected"
            bool_result = True
        else:
            bool_result = False
            result_str = f"symbol mismatch in the request and response"
        assert_test(bool_result, result_str=result_str,
                    status_code=order_response.status_code)

    @mark.positive_case
    def test_order_gemini_post_validate_200_type_in_request_response(self):
        """
        validate the price value in the request and response
        """
        order_response, payload = new_order_gemini()
        if order_response.status_code == STATUS_OK and order_response.type == payload['type']:
            result_str = "The type in request and response match as expected"
        else:
            result_str = f"Type mismatch between the request and response ."
        assert_test(order_response.status_code == STATUS_OK, result_str=result_str,
                    status_code=order_response.status_code)


    @mark.negative_case
    @mark.client_side_validation
    def test_order_gemini_post_validate_invalid_400_signature(self):
        """
        validate 400 status code for the new order api
        """
        order_response, _ = new_order_gemini(bool_invalid_signature=True)
        if order_response.status_code == STATUS_BAD_REQUEST:
            result_str = "Negative Scenario Passed : Received the required status code 400 as expected"
        else:
            result_str = "Negative Scenario Failed : Received incorrect status code"
        assert_test(order_response.status_code == STATUS_BAD_REQUEST, result_str=result_str,
                    status_code=order_response.status_code)

    @mark.negative_case
    @mark.client_side_validation
    def test_order_gemini_post_validate_status_404_invalid_endpoint(self):
        """
        validate 404 status code for the new order api
        """
        order_response, _ = new_order_gemini(end_point='/v1/order/ne')
        if order_response.status_code == STATUS_NOT_FOUND and order_response.reason == 'EndpointNotFound':
            result_str = "Negative Scenario Passed : Received the required status code 404 as expected"
        else:
            result_str = "Negative Scenario Failed : Received incorrect status code"
        assert_test(order_response.status_code == STATUS_NOT_FOUND, result_str=result_str,
                    status_code=order_response.status_code)

    @mark.negative_case
    @mark.server_side_validation
    def test_order_gemini_post_validate_502_status_code(self):
        """
        validate 502 server side error.
        This test case should be validated during the server down time.
        """
        order_response, _ = new_order_gemini()
        if order_response.status_code == STATUS_BAD_GATEWAY:
            result_str = "Negative Scenario Passed for 502 error code : Received the required status code 502 as expected"
        else:
            result_str = "Negative Scenario Failed for 502 error code : Received incorrect status code"
        print(order_response.status_code)
        assert_test(order_response.status_code == STATUS_BAD_GATEWAY, result_str=result_str,
                    status_code=order_response.status_code)


if __name__ == '__main__':
    unittest.main()
