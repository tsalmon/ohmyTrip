# -*- coding: UTF-8 -*-

#source: https://github.com/Yelp/yelp-api/blob/master/v2/python/sample.py
"""
Yelp API v2.0 code sample.

This program demonstrates the capability of the Yelp API version 2.0
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.

Please refer to http://www.yelp.com/developers/documentation for the API documentation.

This program requires the Python oauth2 library, which you can install via:
`pip install -r requirements.txt`.

Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
import json
import pprint
import sys
import urllib
import urllib2

import oauth2

#CONFIG FILES 
from homytrip.secret_settings import YELP_CONSUMER_KEY as CONSUMER_KEY
from homytrip.secret_settings import YELP_CONSUMER_SECRET as CONSUMER_SECRET
from homytrip.secret_settings import YELP_TOKEN as TOKEN
from homytrip.secret_settings import YELP_TOKEN_SECRET as TOKEN_SECRET

#MODELS
from place import *


API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
#DEFAULT_LOCATION = 'San Francisco, CA'
DEFAULT_LOCATION = 'Paris, France'
SEARCH_LIMIT = 5
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'http://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    
    #print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

def search(term, location):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """
    
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def get_business(business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path)

def query_api(term, location):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    
    #print ("%s %s") % (term.__name__, location)
    #return []
    places = []
    response = search(term.__name__, str(location))

    businesses = response.get('businesses')

    if not businesses:
        print u'No businesses for {0} in {1} found.'.format(term, location)
        return []

    print "---------------------------------------------------------"
    for i in range(0, len(businesses)):
        #print "rating = %s" % businesses[i][u'rating']
        #print "count review = %s" % businesses[i][u'count_review']
        #print ""
        pprint.pprint(businesses[i])
        return []
        business_id = businesses[i]['id']
        response = get_business(business_id)
        adresse = response[u'location'][u'display_address']
        coordinate = response[u'location'][u'coordinate']
        name = response[u'name']
        places.append(term(adresse, coordinate, name))

    return places  

def main():
    try:
        return query_api(DEFAULT_TERM, DEFAULT_LOCATION)
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))


if __name__ == '__main__':
    main()
