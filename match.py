import requests

match_content = requests.get('https://olimpbet.kz/index.php?page=line&action=2&live[]=77799334&sid[]=40')

for cookie in match_content.cookies:
    print('name: ', cookie.name, ' | value: ', cookie.value)