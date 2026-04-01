print("request_os_module.py")

import requests


response = requests.get('https://jsonplaceholder.typicode.com/posts/1', verify=False)
print(response.json())


import os
os.path.abspath(__file__) # absolute path