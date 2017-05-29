'''
A script to fetch feeds information from the group via Facebook Graph API
'''
import json
from pprint import pprint as pp
from FacebookInfo import ACCESS_TOKEN, GROUP_ID
from facepy import GraphAPI


def main():
    '''
    Start fetching data from the group through Facebook graph API
    '''

    # Initialize Facebook GRAPH API with the temporary access token
    graph = GraphAPI(ACCESS_TOKEN)

    # get the list of feeds via the Facepy library
    result = graph.get(path=GROUP_ID + '/feed',
                       limit=150,
                       fields='id',
                       page=True)
    feed_ids = []
    for each_response in result:
        feed_ids.extend(
            list(map(lambda feed: feed['id'], each_response['data'])))
        pp(feed_ids)
    with open(GROUP_ID + '-feed-ids.json', 'w') as output:
        json.dump({'data': feed_ids}, output)

if __name__ == '__main__':
    main()
