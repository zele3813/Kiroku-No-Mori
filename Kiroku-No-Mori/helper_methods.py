import json
import requests
import os
from dotenv import load_dotenv

# === Myanimelist (MAL) API calls===
# Refer to https://myanimelist.net/apiconfig/references/api/v2 for information on MAL API,
# including the credentials needed for and data structures returned by each respective API 
# endpoint through the API.

load_dotenv()
# Myanimelist (MAL) API client id, stored as an environment var. 
# and not under version control. Local users need to obtain their own client id through MAL. 
# Refer to https://myanimelist.net/forum/?topicid=1973141 for instructions on how to obtain a client id.
CLIENT_ID = os.getenv("CLIENT_ID") 


# Myanimelist API call through (url) endpoint; Look for (type) of works matching the given name, 
# with an offset corresponding to the current page number and entry limit per page
def mal_search_by_name(type: str, name: str, page: int, limit=5):
    url = f"https://api.myanimelist.net/v2/{type}?q={name}&limit={limit}&offset={(page*limit)}"
    response = requests.get(url, headers={
        'X-MAL-CLIENT-ID': CLIENT_ID
    })

    response.raise_for_status()
    response_json = response.json()
    response.close()
    
    return response_json

# Myanimelist API call; Search for a specific work given the work id and type of work
def mal_search_by_id(type: str, id: int):
    fields = "id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics"
    # test_fields = "recommendations"
    # fields = test_fields

    url = f"https://api.myanimelist.net/v2/{type}/{id}?fields={fields}"
    response = requests.get(url, headers={
        'X-MAL-CLIENT-ID': CLIENT_ID
    })
    
    response.raise_for_status()
    response_json = response.json()
    response.close()

    return response_json


# === Parsers ===
def mal_parse_name_search(json):
    #TODO parse json data into custom ds

    parsed_data = json["data"]
    return parsed_data

def mal_parse_id_search(json):
    #TODO parse json data, specifically recommendations, into custom ds

    parsed_json = []
    return parsed_json


# === General helpers ===

# Create an increment array of length 5 with cur_page int as the element in the center
def generate_pages_arr(cur_page):
    prev_page_bound = max(1, cur_page - 2)
    next_page_bound = max(5, cur_page + 2)
    pages = [i for i in range(prev_page_bound, next_page_bound+1)]
    return pages


# === Exception Handlers ===

def arg_validator(input, expected_args):
    #TODO 
    # ensure the correct number of input is passed
    # ensure the correct keys exist in the input dictionary 
    try:
        pass
    except:
        pass

    return True