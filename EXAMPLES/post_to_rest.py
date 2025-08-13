from datetime import datetime
import time
import requests

URL = 'http://httpbin.org/post'

for i in range(3):
    response = requests.post(  # POST data to server
        URL,
        data = {'date': datetime.now(),
                'label': 'test_' + str(i)
        },
        cookies={'python': 'testing'},
        headers={'X-Python': 'Guido van Rossum'},
    )
    print(response.status_code)
    print(response.text)
    print()
    time.sleep(2)

