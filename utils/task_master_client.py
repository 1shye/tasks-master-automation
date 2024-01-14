from utils.requests_wrapper import RequestsHandler


class TaskMasterClient:
    """
    This class will be used to simulate task master client behaviour
    """
    def __init__(self):
        self.request = RequestsHandler()

    def create_new_task(self, base_url, task_content):
        return self.request.send_post_request(url=base_url, body=task_content)

    def get_task_by_id(self, base_url, task_id):
        url = f'{base_url}/{task_id}'
        print(url)
        return self.request.send_get_request(url)

    def update_task_by_id(self, base_url, task_id, task_update):
        url = f'{base_url}/{task_id}'
        return self.request.send_put_request(url=url, data=task_update)

    def delete_task(self, base_url, task_id):
        # for future feature
        url = f'{base_url}/{task_id}'
        return self.request.send_delete_request(url)
