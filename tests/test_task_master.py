from utils.common import read_file, generate_task_id
from utils.data_helpers import save_task_id, generate_task_body
from utils.task_master_client import TaskMasterClient
from assertpy import assert_that
from configurations.config import ResponseCode, BASE_URL, TASK_ID_PATH

tm_client = TaskMasterClient()

# -------------------------------------------------POST--------------------------------------------------

def test_create_new_task():
    """
    Happy path - status code 201
    """
    task_content = generate_task_body()
    response = tm_client.create_new_task(base_url=BASE_URL, task_content=task_content)
    assert_that(response.status_code).is_equal_to(ResponseCode.Created.value)
    # assumption: the POST response will contain taskId for the new task
    # that will be store at the DB for GET and PUT request
    assert_that(response.json_obj.get('taskId')).is_not_none()
    task_id = response.json_obj.get("taskId")
    save_task_id(file_destination=TASK_ID_PATH, task_id=task_id)


def test_invalid_create_task_request():
    """
    Sad path - status code 404
    """
    invalid_url = fr"{BASE_URL}\fake\route"
    task_content = generate_task_body()
    response = tm_client.create_new_task(base_url=invalid_url, task_content=task_content)
    assert_that(response.status_code).is_equal_to(ResponseCode.StatusNotFound.value)


def test_create_task_external_error():
    """
    bad path status code 500
    :return:
    """
    invalid_url = r"http://fakeServer:3001/tasks"
    task_content = generate_task_body()
    response = tm_client.create_new_task(base_url=invalid_url, task_content=task_content)
    assert_that(response.status_code).is_equal_to(ResponseCode.ServerError.value)


# -------------------------------------------------GET--------------------------------------------------

def test_get_task_by_id():
    """
    happy path - status code 200
    """
    task_id_content = read_file(TASK_ID_PATH)
    task_id = task_id_content.get("task_id")
    response = tm_client.get_task_by_id(base_url=BASE_URL, task_id=task_id)
    assert_that(response.status_code).is_equal_to(ResponseCode.Ok.value)
    assert_that(response.json_obj.get('title')).is_not_none()
    assert_that(response.json_obj.get('description')).is_not_none()
    assert_that(response.json_obj.get('due_date')).is_not_none()


def test_get_task_by_fake_id():
    """
    sad path - status code 404
    """
    fake_task_id = generate_task_id()
    response = tm_client.get_task_by_id(base_url=BASE_URL, task_id=fake_task_id)
    assert_that(response.status_code).is_equal_to(ResponseCode.StatusNotFound.value)
    assert_that(response.json_obj.get('error')).is_not_none()
    assert_that(response.json_obj.get('message')).is_not_none()


def test_invalid_get_task_by_id():
    """
    bad oath - status code 500
    """
    invalid_url = r"http://fakeServer:3001/tasks"
    task_id_content = read_file(TASK_ID_PATH)
    task_id = task_id_content.get("task_id")
    response = tm_client.get_task_by_id(base_url=invalid_url, task_id=task_id)
    assert_that(response.status_code).is_equal_to(ResponseCode.ServerError.value)
    assert_that(response.json_obj.get('error')).is_not_none()
    assert_that(response.json_obj.get('message')).is_not_none()


# -------------------------------------------------PUT--------------------------------------------------

def test_update_task_content():
    """
    happy path - status code 200
    """
    task_id_content = read_file(TASK_ID_PATH)
    task_id = task_id_content.get("task_id")
    task_update = generate_task_body()
    response = tm_client.update_task_by_id(base_url=BASE_URL, task_id=task_id, task_update=task_update)
    assert_that(response.status_code).is_equal_to(ResponseCode.Ok.value)
    assert_that(response.json_obj.get('status')).contains("Updated")


def test_update_task_invalid_route():
    """
    sad path - status code 404
    """
    invalid_url = fr"{BASE_URL}\fake\route"
    task_update = generate_task_body()
    task_id_content = read_file(TASK_ID_PATH)
    task_id = task_id_content.get("task_id")
    response = tm_client.update_task_by_id(base_url=invalid_url, task_id=task_id, task_update=task_update)
    assert_that(response.status_code).is_equal_to(ResponseCode.StatusNotFound.value)
    assert_that(response.json_obj.get('message')).is_not_none()


def test_update_task_fake_id():
    """
    bad path - status code 500
    """
    invalid_url = r"http://fakeServer:3001/tasks"
    task_id_content = read_file(TASK_ID_PATH)
    task_id = task_id_content.get("task_id")
    task_update = generate_task_body()
    response = tm_client.update_task_by_id(base_url=invalid_url, task_id=task_id, task_update=task_update)
    assert_that(response.status_code).is_equal_to(ResponseCode.ServerError.value)
    assert_that(response.json_obj.get('message')).contains("Error")
