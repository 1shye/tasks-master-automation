import requests
import json
from dataclasses import dataclass

from configurations import config


@dataclass
class Response:
    status_code: int
    text: str
    json_obj: object
    headers: dict


class RequestsHandler:
    """
    this class will be used on the automation execution layer
    """

    def send_get_request(self, url, params=None, header=None):
        """
        send http get request by providing url
        :return: http response data as Response object
        """

        if header is None:
            header = {"content-type": "application/json"}
        try:
            if not config.CERT_DIR:
                resp = requests.get(url, params, headers=header)
            else:
                resp = requests.get(
                    url, params, verify=config.CERT_DIR, timeout=120, headers=header
                )

        except Exception:
            resp = Response(500, "Internal server error", {}, {})
            return resp

        return self.__get_response_obj(resp)

    def send_put_request(self, url, data, header=None):
        """
        send http put request by providing put url + body
        :return: http response data as Response object
        """
        try:
            if not header:
                header = {"content-type": "application/json", "accept": "*/*"}

            if not config.CERT_DIR:
                resp = requests.put(url, data=data, headers=header, timeout=120)
            else:
                resp = requests.put(
                    url, data=data, headers=header, verify=config.CERT_DIR, timeout=120
                )
        except Exception:
            resp = Response(500, "Internal server error", {}, {})
            return resp

        return self.__get_response_obj(resp)

    def send_post_request(self, url, body, header=None, params=None):
        """
        send http post request by providing url, body , header and params
        :return:
        resp : http response data as Response object
        """

        if not header:
            header = {"content-type": "application/json", "accept": "*/*"}
        try:
            if not config.CERT_DIR:
                resp = requests.post(
                    url=url, data=json.dumps(body), headers=header, params=params
                )
            else:
                resp = requests.post(
                    url=url,
                    data=json.dumps(body),
                    headers=header,
                    verify=config.CERT_DIR,
                    params=params,
                )

        except Exception:
            resp = Response(500, "Internal server error", {}, {})
            return resp

        return self.__get_response_obj(resp)

    def send_delete_request(self, url, params=None):
        """
        send http delete request by providing delete url + query parameters
        :return: http response data as Response object
        """
        try:

            if not config.CERT_DIR:
                resp = requests.delete(url, data=params, timeout=120)
            else:
                resp = requests.delete(
                    url, data=params, verify=config.CERT_DIR, timeout=120
                )

        except Exception:
            resp = Response(500, "Internal server error", {}, {})
            return resp

        return self.__get_response_obj(resp)

    def __get_response_obj(self, response):
        status_code = response.status_code
        text = response.text

        try:
            json_obj = response.json()
        except Exception:
            json_obj = {}

        headers = response.headers

        return Response(
            status_code, text, json_obj, headers
        )
