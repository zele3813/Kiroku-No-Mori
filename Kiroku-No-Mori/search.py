from flask import Blueprint
from flask import render_template
from flask import request
from . import helper_methods as h_methods

bp = Blueprint("search", __name__, url_prefix="/search") 
limit = 5 #Limit for the number of entries displayed per page.

# Search for anime or manga & novel by name
@bp.route("/name", methods=['GET'])
def search_name():
    print("======Search By Name======")
    # print(request.args)
    
    # if not h_methods.arg_validator(request.args, ["page", "name", "type"]):
    #     return render_template("")

    cur_page = int(request.args["page"]) # Currently viewing page.
    pages = h_methods.generate_pages_arr(cur_page) # Create an int array of length 5 (e.x. [1, 2, 3, 4, 5] if cur_page = 3) for result page navigation.

    type = request.args["type"] # Type of search: anime or manga & novels.
    response_json = h_methods.mal_search_by_name(type, request.args["name"], cur_page-1, limit) # Call myanimelist api to search for (type) by name given the current viewing page and a custom limit on the # of resulting entry per page.

    # print(response_json)
    parsed_data = h_methods.mal_parse_name_search(response_json) # Parse MAL json into an array of dictionaries
    paging = response_json["paging"]
    url_for_search_id = "search.search_id"
    url_for_search_name = "search.search_name"
    

    return render_template("search/search-result.html", 
                           name = request.args["name"], type=type, data = parsed_data, 
                           paging = paging, pages = pages, cur_page = cur_page, 
                           url_for_search_id=url_for_search_id, url_for_search_name=url_for_search_name)

# Search for anime by id
@bp.route("/<int:id>")
def search_id(id):
    print("======Search By ID======")
    type = request.args["type"]
    response_json = h_methods.mal_search_by_id(type, id)
    # print(response_json)
    parsed_data = h_methods.mal_parse_id_search(response_json)
    

    return render_template("search/search-detail.html", 
                           data = response_json)


def main():
    pass

if __name__ == "__main__":
    print("Running search.py script")
    main()