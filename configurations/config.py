import enum
from utils.common import get_environment_variable
import json

CONF_FILE = get_environment_variable("CONF_FILE", None)
if not CONF_FILE:
    raise EnvironmentError("Should provide path for CONF_FILE")
try:
    with open(CONF_FILE, "r", encoding="utf-8") as fp:
        conf = json.load(fp)
except Exception as e:
    raise EnvironmentError("Failed to load JSON for configuration") from e

CERT_DIR = conf.get("CERT_DIR", None)

BASE_URL = conf.get("BASE_URL")

HEADERS = conf.get("HEADERS", {'Content-Type': 'application/json'})

TASK_ID_PATH = conf.get("TASK_ID_PATH")


class ResponseCode(enum.Enum):
    """
    Types of server responses
    """

    Ok = 200  # server return ok status
    Created = 201  # server was return ok for changing
    NoJob = 204  # successful request with no content
    ValidationErrors = 400  # bad request
    StatusNotFound = 404  # not found
    DuplicatedError = 409  # conflict
    GetwayTimeOut = 504  # some server didn't respond on time
    ServerError = 500  # internal server error
