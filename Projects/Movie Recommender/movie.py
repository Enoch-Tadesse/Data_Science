import os
# import json
import pprint
import pandas as pd
import requests as r
from  dotenv import load_dotenv

load_dotenv()

api = os.getenv("API")
read_access = os.getenv("Read_Access_Token")

def getMovie(id):
    url = f"https://api.themoviedb.org/3/find/{id}?external_source=imdb_id"
    print(url)
    header = {
        'Authorization' : f"Bearer {read_access}",
        'accept' : "application/json"
    }
    response = r.get(url=f"{url}",headers=header)
    print(response.json())
    # if response.status_code == 200:
    #     data = response.json()
    #     result = data.get("results",[])
    #     # print(result)
    #     df = pd.DataFrame(result)
    #     print(df.head())
    # else:
    #     print(f"Error code {response}")
    
getMovie("tt16366836")

