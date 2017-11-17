import requests
import platform
import datetime
from requests.exceptions import ConnectTimeout
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

REQUEST_TIMEOUT = 50

class AMEndpoints:
    software_update = '/maintenance/software_update'
    general_info = '/general_info'
    auth = '/auth'
    logs = '/settings/logs'
    get_logs = '/logs?type=debug&token='


class ApplianceManager:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    headers1 = {
        'Content-Type': 'application/zip',
        'Accept': 'application/json',
    }

    def __init__(self, ip_addr, username, password, request_timeout=REQUEST_TIMEOUT):
        self.base_url = 'https://{}/AppManager/api/v1'.format(ip_addr)
        self.token = None
        self.username = username
        self.password = password
        self.request_timeout = request_timeout

    def post(self, data, endpoint='/', headers={}):
        url = "{}{}".format(self.base_url, endpoint)
        req_headers = self.headers.copy()
        req_headers.update(headers)
        return requests.post(url, json=data, headers=req_headers, verify=False, timeout=self.request_timeout)

    def get(self, endpoint='/', headers={}):
        url = "{}{}".format(self.base_url, endpoint)
        req_headers = self.headers.copy()
        req_headers.update(headers)
        return requests.get(url, headers=req_headers, verify=False, timeout=self.request_timeout)

    def get_log_files_res(self, endpoint='/', headers={}):
        url = "{}{}".format(self.base_url, endpoint)
        req_headers = self.headers.copy()
        req_headers.update(headers)
        print("URL: " + url)
        res = requests.get(url, headers=req_headers, verify=False, timeout=self.request_timeout)
        get_content_info = res.headers.get('Content-Disposition')
        split_content_info = get_content_info.split("=")
        log_file = split_content_info[1].replace('"', '')
        file_name = log_file.replace('.zip', '')
        today = datetime.datetime.now()
        ctime = "{:%H%M%S}".format(today)
        cdate = "{:%Y%m%d}".format(today)
        file_name = "{}_{}_{}.zip".format(file_name, cdate, ctime)
        if 'Windows' in platform.system():
            path_file_name = "{}\{}".format("C:\TEMP\Logs", file_name)
        else:
            path_file_name = "{}/{}".format(".", file_name)
        with open(path_file_name, mode='wb') as localfile:
           localfile.write(res.content)
        return path_file_name

    def login(self):
        data = {
            'username': self.username,
            'password': self.password,
        }

        response = self.post(data, AMEndpoints.auth)
        json = response.json()
        data = json.get('data', {})
        token = data.get('access_token')
        self.token = token
        return token

    def call_software_update(self, su_filename):
        data = {'resumableFilename': su_filename}
        headers = {'Authorization': 'Bearer/{}'.format(self.token)}
        return self.post(data, AMEndpoints.software_update, headers)

    def get_general_info(self):
        self.login()
        headers = {'Authorization': 'Bearer/{}'.format(self.token)}
        data = self.get(AMEndpoints.general_info, headers=headers)
        return data.json().get('data')

    def get_serial_number(self):
        try:
            general_info = self.get_general_info()
        except (ValueError, ConnectTimeout):
            print("Unable to read Serial Number")
        else:
            return general_info.get('serial_number')

    def get_log_files(self):
        self.login()
        headers1 = {'Authorization': 'Bearer/{}'.format(self.token)}
        filename = self.get_log_files_res(AMEndpoints.get_logs + self.token, headers=headers1)
        return filename
