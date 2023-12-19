"""
trying to pull playlists from spotify

started with:
https://stmorse.github.io/journal/spotify-api.html
https://lvngd.com/blog/accessing-spotify-api-python/

J. Knerr
Jan 2022
"""

import requests
import click


@click.command()
@click.option('--username', default="jeffknerr", help='spotify user name')
@click.option('--gettracks', is_flag=True, help='add if you want tracks')
def main(username, gettracks):
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
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # to get user playlists
    BASE_URL = 'https://api.spotify.com/v1/users/%s/playlists' % username
    offset = 0
    limit = 50
    done = False
    while not done:
        options = '/?offset=%d&limit=%d' % (offset, limit)
        url = BASE_URL+options
        r = requests.get(url, headers=headers)
        r = r.json()
        playlists = r.get('items')
        if playlists is None:
            print("Incorrect spotify username??? (%s)" % username)
            done = True
        else:
            for i in range(len(playlists)):
                p = playlists[i]
                print(i+offset, p["name"])
                if gettracks:
                    tracks = playlists[i]["tracks"]
                    href = tracks["href"]
                    displayTracks(href, headers)
            if len(playlists) == limit:
                offset += limit
            else:
                done = True


def displayTracks(href, headers):
    """given href link, get all track info, display it/save it"""
    r = requests.get(href, headers=headers)
    r = r.json()
    thetracks = r.get('items')
    for i in range(len(thetracks)):
        track = thetracks[i]["track"]
        if track is not None:
            print(i, track["name"])
            print("  ", track["album"]["name"])
            for j in range(len(track["artists"])):
                print("    ", track["artists"][j]["name"])
        else:
            print(i, "None")
    print("#"*40)


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
