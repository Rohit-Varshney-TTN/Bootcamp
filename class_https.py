import requests
from requests.auth import HTTPBasicAuth

class InvalidURL(Exception):
    pass

class MyHTTPS:
    def __init__(self,url,username,token,timeout=0.5):
        self.url=url
        self.auth=HTTPBasicAuth(username, token)
        self.timeout=timeout

    def user_req(self):
        try:
            response=requests.get(self.url,auth=self.auth,timeout=self.timeout)

            if response.status_code==200:
                print("Get Response is done")
                print("Headers:",response.headers)
                print("Status Code:",response.status_code)
                return response.json()
            elif response.status_code==404:
                raise FileNotFoundError("Error 404 : Not Found")
            else:
                response.raise_for_status()

        except requests.Timeout:
            print("Request timed out")
        except FileNotFoundError as e:
            print(e)
        except requests.RequestException as e:
            print(f"Request error:{e}")
        except InvalidURL:
            print("Invalid URL")

username=input("Enter the username :")
token=input("Enter the token :")
obj=MyHTTPS("https://api.github.com/user",username,token)
x=obj.user_req()