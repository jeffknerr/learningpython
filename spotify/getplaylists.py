"""
trying to pull playlists from spotify

following:
https://stmorse.github.io/journal/spotify-api.html

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
    print(access_token)


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
