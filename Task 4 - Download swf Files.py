import requests
from requests.exceptions import HTTPError

#Opening file
file1 = open('Task3/result.txt', 'r')

#initial
count = 0

#using for loop
for line in file1:
    count += 1
    sentence = line.strip()
    file2 = open('Task4/' + sentence , "wb")
    for url in ['https://dagobah.net/flashswf/' + sentence]:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occured: {http_err}')
        except Exception as err:
            print(f'Other error occured: {err}')
        finally:
            print(sentence + ' downloaded... success!')
            file2.write(response.content)
file1.close
file2.close
