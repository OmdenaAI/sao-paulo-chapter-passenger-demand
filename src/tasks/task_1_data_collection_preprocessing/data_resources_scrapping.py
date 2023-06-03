import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://transparencia.metrosp.com.br/dataset/demanda"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

resources_list = soup.find("div", {"class": "item-list"}).find_all("li")

data = []
for resource in resources_list:
    try:
        resource_name = resource.find('a')['title']
        resource_link = resource.find('span', {'class': 'links'}).find('a')['href']
        file_type = resource.find('span', {'class': 'links'}).find('a')['href'][-3:]
    except:
        pass
    data.append({'resource_name': resource_name, 'resource_link': resource_link, 'file_type': file_type})

df = pd.DataFrame(data)

df.to_csv("sao-paulo-chapter-passenger-demand/src/tasks/task_1_data_collection_preprocessing/resources_list.csv", index=False)

print(df)