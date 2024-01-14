import json
import os
import uuid


def read_file(file_location: str):
    """
    This method will read file content from given filepath
    :param file_location: path to the selected file to be read
    :return:
    file content
    """
    try:
        with open(file_location, 'r') as f:
            return json.load(f)
    except Exception as e:
        return e


def to_bool(string, default):
    # (str- bool) -> (bool)
    """
    This method convert string to bool - "True, "Yes", "1" are considered True
    """
    if string and string.strip():
        return string.strip()[0].lower() in ["1", "t", "y"]
    return default


def get_environment_variable(name: str, default_val):
    # (str, object) -> object
    """
    Returns an environment variable in the type set by the default value.
    If environment variable is empty or cannot be converted to default_val type, function returns default_val
    Note that for boolean value either 'True' 'Yes' '1', regardless of case sensitivity are considered as True.
    """
    value = os.environ.get(name)
    if value:
        if isinstance(default_val, bool):
            value = to_bool(value, default_val)
        elif default_val is not None:
            try:
                value = type(default_val)(value)
            except ValueError:
                value = default_val

    else:
        value = default_val
    return value


def generate_task_id():
    """
    This method will generate random task id for 404 scenarios
    :return:
    """
    random_task_id = str(uuid.uuid4())
    return random_task_id
