import unittest
from flask import Flask, json
from app import app


class TestHTTPMethods(unittest.TestCase):

    def test_HTTP_200_pass(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': '5', 'v': '2'})
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['answer'] == 10
            assert data['error'] == 'false'
            assert data['u'] == 5
            assert data['v'] == 2
            assert data['string'] == '5 * 2 = 10'

    def test_HTTP_200_multiply_zero_pass(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': '0', 'v': '1'})
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['answer'] == 0
            assert data['error'] == 'false'
            assert data['u'] == 0
            assert data['v'] == 1
            assert data['string'] == '0 * 1 = 0'

    def test_HTTP_status_code_400_invalid_int_pass_u(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': 'a', 'v': '3'})
            assert response.status_code == 400

    def test_HTTP_status_code_400_invalid_int_pass_v(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': '3', 'v': 'a'})
            assert response.status_code == 400

    def test_HTTP_status_code_400_no_parameter_pass(self):
        with app.test_client() as c:
            response = c.get('/', query_string={})
            assert response.status_code == 400

    @unittest.expectedFailure
    def test_HTTP_200_error_fail(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': '5', 'v': '2'})
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['answer'] == 10
            assert data['error'] == 'true'
            assert data['u'] == 5
            assert data['v'] == 2
            assert data['string'] == '5 * 2 = 10'

    @unittest.expectedFailure
    def test_HTTP_200_string_fail(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': '5', 'v': '2'})
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['answer'] == 10
            assert data['error'] == 'true'
            assert data['u'] == 5
            assert data['v'] == 2
            assert data['string'] == '5 + 2 = 1'


    @unittest.expectedFailure
    def test_HTTP_200_answer_fail(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': '5', 'v': '2'})
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['answer'] == 'k'
            assert data['error'] == 'true'
            assert data['u'] == 5
            assert data['v'] == 2
            assert data['string'] == '5 * 2 = 10'


    @unittest.expectedFailure
    def test_HTTP_200_u_Variable_fail(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': '5', 'v': '2'})
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['answer'] == 10
            assert data['error'] == 'true'
            assert data['u'] == 6
            assert data['v'] == 2
            assert data['string'] == '5 % 2 = 10'

    @unittest.expectedFailure
    def test_HTTP_200_v_Variable_fail(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': '5', 'v': '2'})
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['answer'] == 1
            assert data['error'] == 'true'
            assert data['u'] == 5
            assert data['v'] == 3
            assert data['string'] == '5 * 2 = 10'

    @unittest.expectedFailure
    def test_HTTP_status_code_200_fail(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': 'a', 'v': '2'})
            assert response.status_code == 250
            data = json.loads(response.get_data(as_text=True))
            assert data['answer'] == 10
            assert data['error'] == 'true'
            assert data['u'] == 5
            assert data['v'] == 2
            assert data['string'] == '5 * 2 = 10'

    @unittest.expectedFailure
    def test_HTTP_status_code_400_invalid_int_fail(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'u': 'a', 'v': '2'})
            assert response.status_code == 200

    @unittest.expectedFailure
    def test_HTTP_status_code_400_no_parameter_fail(self):
        with app.test_client() as c:
            response = c.get('/', query_string={})
            assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()