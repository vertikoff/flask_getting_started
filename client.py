import requests
import sys

def make_requests():
    host = "http://vcm-3581.vm.duke.edu:5000"
    get_endpoints = ["/", "/name", "/name/coach_k"]
    for endpoint in get_endpoints:
        r = requests.get(host + endpoint)
        sys.stdout.write('endpoint: ' + endpoint + ' \nresponse: ' + r.text + ' \n\n')

    data = {"a": [1, 6], "b": [3, 9]}
    r = requests.post(host + '/distance', json=data)
    sys.stdout.write('endpoint: /distance \ninput: ' + str(data) + '\nresponse: ' + r.text + ' \n\n')

make_requests()
