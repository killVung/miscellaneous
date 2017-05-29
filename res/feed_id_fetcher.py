'''
A script to fetch feeds information from the group via Facebook Graph API
'''
import json
# from pprint import pprint as pp
from FacebookInfo import ACCESS_TOKEN, GROUP_ID
from facepy import GraphAPI

def fetch_feed_id(group_id, limit=100):
    '''
    Fetch each feed's id from the selected group
    '''

    # Initialize Facebook GRAPH API with the temporary access token
    graph = GraphAPI(ACCESS_TOKEN)

    # get the list of feeds via the Facepy library
    result = graph.get(path=group_id + '/feed',
                       limit=limit,
                       fields='id',
                       page=True)

    feed_ids = []
    for each_response in result:
        feed_ids.extend(
            list(map(lambda feed: feed['id'], each_response['data'])))

    with open(GROUP_ID + '-feed-ids.json', 'w') as output:
        json.dump({'data': feed_ids}, output)       