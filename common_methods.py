import logging
import os
import json

logging.basicConfig(level=logging.INFO,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def read_json(file_path):
    BASE_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(BASE_DIR_PATH, file_path), 'r') as f:
        json_data = json.load(f)
    return json_data


def assert_pass(test_str="status code obtained as expected", status_code=None):
    logging.log(f'{test_str}:{status_code}')
    assert True


def assert_fail(str_val="Test case is failes", status_code=None):
    logging.log(f'{str_val}:{status_code}')
    assert False

def log_info(message=""):
    logging.info(message)

def assert_test(bool_result=None, result_str="Test Case is working as expected", status_code=None):
    if bool_result:
        logging.info(
            f'Test case is working as expected, test case output : {result_str} , and status code :{status_code}')
        assert True
    else:
        logging.info(
            f'Test case is not working as expected, test case output : {result_str} , and status code :{status_code}')
        assert False


class CheckNonce:
    check_lst = []




