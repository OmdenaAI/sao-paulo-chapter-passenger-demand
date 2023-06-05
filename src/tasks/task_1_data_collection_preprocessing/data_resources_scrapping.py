import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    """
    Scrapes the content of a resource website specified by the given URL.

    Args:
        url (str): The URL of the resource website to scrape.

    Returns:
        BeautifulSoup: The parsed HTML content of the website.

    Examples:
        >>> soup = scrape_website('https://www.example.com')
        >>> title = soup.title.string
        >>> print(title)
        Example Website

    Note:
        This function requires the 'requests' and 'BeautifulSoup' modules to be installed.

    """
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    return soup


# initializing an empty list to save public metro lines data
public_dataframe = []

# datasets types available on the main source (public metro lines)
datasets = ["demanda", "oferta", "infraestrutura-dados-de-linhas-e-estações"]

# loop trough each available dataset from the main source
for type in datasets:
    soup = scrape_website(f"https://transparencia.metrosp.com.br/dataset/{type}")

    # finding last modified date from metadata available on the website
    metadata = soup.find("div", {"class": "table-responsive"})
    mod_date = pd.to_datetime(metadata.find("td", {"class": "field-content"}).text, format="%Y-%m-%d")

    # soup resources list
    resources_list = soup.find("div", {"class": "item-list"}).find_all("li")

    # iterating trough resources list
    for resource in resources_list:
        try:
            resource_name = resource.find('a')['title']
            resource_link = resource.find('span', {'class': 'links'}).find('a')['href']
            file_type = resource.find('span', {'class': 'links'}).find('a')['href'][-3:]
            
        except:
            pass
        # appending data and metadata to a list
        public_dataframe.append({'resource_name': resource_name, 'resource_link': resource_link, 'file_type': file_type, 'mod_date': mod_date})
        

df_public = pd.DataFrame(public_dataframe)
df_public.to_csv("sao-paulo-chapter-passenger-demand/src/tasks/task_1_data_collection_preprocessing/public_resources_list.csv", index=False)

# initializing empty list to save private metro lines data
private_dataframe = []

# line 4 resources webscrapping
soup_line4 = scrape_website("https://www.viaquatro.com.br/linha-4-amarela/passageiros-transportados")

resources_list = soup_line4.find_all("div", {"class": "box press-room"})

for resource in resources_list:
    for each in resource.find_all("li"):
        try:
            resource_name = each.find("a")["title"]
            resource_link = "https://www.viaquatro.com.br" + each.find("a")["href"]
            file_type = resource.find('span', {'class': 'links'}).find('a')['href'][-3:]
            
        except:
            pass
        private_dataframe.append({'resource_name': resource_name, 'resource_link': resource_link, 'file_type': file_type, 'line': 4})
        

# line 5 resources webscrapping
for year in range(2018, 2024):
    soup_line5 = scrape_website(f"https://www.viamobilidade.com.br/nos/passageiros-transportados/linha-5-lilas?periodo={year}")

    resources5_list = soup_line5.find_all("ul", {"class": "download"})
    for resource in resources5_list:
        for each in resource.find_all("li"):
            try:
                resource_name5 = each.find("a").text
                resource_link5 = "https://www.viamobilidade.com.br" + each.find("a")["href"]
                file_type5 = resource_link5[-3:]
                
            except:
                pass
            private_dataframe.append({'resource_name': resource_name5, 'resource_link': resource_link5, 'file_type': file_type5, 'line': 5})
        

df_private = pd.DataFrame(private_dataframe)

df_private.to_csv("sao-paulo-chapter-passenger-demand/src/tasks/task_1_data_collection_preprocessing/private_resources_list.csv", index=False)