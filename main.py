import requests
from bs4 import BeautifulSoup

url = "https://www.omgtu.ru/general_information/institutes/institute_of_distance_learning/employees/employees.php"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    sotrud = soup.find('div', class_='main__content')
    n=sotrud.find_all('i')
    with open('output.txt', 'w', encoding='utf-8') as file:
        for sn in sotrud.find_all('i'):
            name = sn.get_text(strip=True)
            if name.startswith(('Г')):
                file.write(name + '\n')





