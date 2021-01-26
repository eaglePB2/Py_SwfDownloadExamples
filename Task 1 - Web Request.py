import requests
from requests.exceptions import HTTPError


for i in range(1,277):
    j = str(i)
    f = open("Task1/page" + j + ".html", "w", encoding='utf-8')
    for url in ['https://dagobah.net?page=' + j]:
        try:
            response = requests.get(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Page ' + j + ' Success!')
            f.write(response.text)
            f.close()
