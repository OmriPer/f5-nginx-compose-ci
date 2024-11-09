# test.py

import requests
from typing import Optional

def test_server(url: str, expected_status: int, expected_content: Optional[str]=None) -> bool: 
    with requests.get(url) as response:
        # check the response code
        if response.status_code == expected_status:
            print(f'server {url} responded with the correct status')
        else:
            print(f'server {url} responded with the wrong status')
            return False

        # check the response body if applicable
        if expected_content is not None:
            if response.text.splitlines() == expected_content.splitlines():
                print(f'server {url} responded with the correct content')
            else:
                print(f'server {url} responded with the wrong content')
                return False

        return True
    
if __name__ == '__main__':
    success: bool = True
    with open('expected.html', 'r') as expected_file:
        expected_html:str = expected_file.read()
    
    success = test_server('http://nginx:8080', 200, expected_html) and test_server('http://nginx:8081', 500)

    result_file_name = '/result/succeeded' if success else '/result/fail'

    with open(result_file_name, 'w') as result_file:
        result_file.write('')

    exit(0 if success else 1) # exit code 0 if test passed, 1 if failed
