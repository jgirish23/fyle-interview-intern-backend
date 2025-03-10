import pytest
import json
from tests import app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def h_student_1():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }

    return headers


@pytest.fixture
def h_student_2():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }

    return headers

@pytest.fixture
def h_student_3():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 9,
            'user_id': 6
        })
    }

    return headers


@pytest.fixture
def h_teacher_1():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }

    return headers


@pytest.fixture
def h_teacher_2():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }

    return headers

@pytest.fixture
def h_teacher_3():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 3,
            'user_id': 7
        })
    }

    return headers

@pytest.fixture
def h_server_root():
    headers = {
        'X-Principal': json.dumps({
            
        })
    }

    return headers
