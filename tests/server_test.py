def test_get_server_root(client, h_server_root):
    response = client.get(
        '/',
        headers=h_server_root
    )

    assert response.status_code == 200

    data = response.json
    assert data['status'] == 'ready'

def test_get_student(client, h_student_1):
    response = client.get(
        '/student/assignments',
        headers=h_student_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1


def test_get_teacher(client, h_teacher_1):
    response = client.get(
        '/teacher/assignments',
        headers=h_teacher_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1


def test_get_wrong_path(client, h_server_root):
    response = client.get(
        '/tech',
        headers=h_server_root
    )

    assert response.status_code == 404
    error_response = response.json
    assert error_response['error'] == 'NotFound'

