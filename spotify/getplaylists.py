"""
trying to pull playlists from spotify

following:
https://stmorse.github.io/journal/spotify-api.html
https://lvngd.com/blog/accessing-spotify-api-python/

J. Knerr
Jan 2022
"""

import requests


def main():
    """main prog for spotify read playlists program"""
    CLIENT_ID, CLIENT_SECRET = readSecrets("secrets")

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']
#   print(access_token)
#   print(auth_response_data)
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    # to get playlists
#   BASE_URL = 'https://api.spotify.com/v1/me/playlists'
#   r = requests.get(BASE_URL, headers=headers)
#   r = r.json()
#   print(r)

    BASE_URL = 'https://api.spotify.com/v1/'
    featured_playlists_endpoint = 'browse/featured-playlists/?limit=50'
    featured_playlists_url = ''.join([BASE_URL,featured_playlists_endpoint])
    response = requests.get(featured_playlists_url,headers=headers)
    playlists = response.json().get('playlists').get('items')
    print(playlists[0])

    # how to get user's public playlists, liked songs


def readSecrets(filename):
    """read spotify ID and SECRET from a file"""
    CLIENT_ID = None
    CLIENT_SECRET = None
    inf = open(filename)
    for line in inf:
        if line[0] != "#":
            key, val = line.strip().split(":")
            if key == "ClientID":
                CLIENT_ID = val
            elif key == "ClientSecret":
                CLIENT_SECRET = val
    return CLIENT_ID, CLIENT_SECRET


main()
