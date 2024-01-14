import json
import random
import string
import time
from datetime import datetime


def random_string_generator():
    """
    This method will generate random string that will be used for tasks content
    :return:
    random string for test template
    """
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str


def random_due_date_generator():
    """
    This method will generate random date string that will be used for tasks due_date value
    :return:
    date string
    """
    d = random.randint(1, int(time.time()))
    return datetime.fromtimestamp(d).strftime('%Y-%m-%d')


def save_task_id(file_destination: str, task_id: int):
    """
    This method will save the returned task id on given file destination path
    :param file_destination: json file path destination
    :param task_id: task id of the created task
    """
    task_id_data = {"task_id": task_id}
    json_object = json.dumps(task_id_data)
    try:
        with open(file_destination, "w") as file:
            file.write(json_object)
    except Exception as e:
        print(e)
        return e


def generate_task_body():
    """
    This method will generate new task request body for test scenarios
    :return:
    """
    task_title = random_string_generator()
    task_description = f"DO NOT FORGET TO {task_title} "
    task_due_date = random_due_date_generator()
    body = {
        'title': task_title,
        'description': task_description,
        "due_date": task_due_date
    }
    return body
