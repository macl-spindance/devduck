import requests, os


def main():

    print("DUCK API TEST")

    # first set the environment variable with
    #   export DUCK_URL=<your lambda url> 

    url = os.environ["DUCK_URL"]

    #header_data =  {'x-api-key': 'NOTREQUIRED'}
    request_data = {'duck':'quack'}

    #r = requests.post(url, headers=header_data, json=request_data)
    r = requests.post(url, json=request_data)

    print(r.status_code)
    print(r.json())

if __name__ == '__main__':
    main()

