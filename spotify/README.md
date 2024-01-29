
# get spotify playlists

I just wanted to try the spotify api. Also wanted to pull
some info on my playlists, in case we ever lose access to 
spotify...

## quickstart

- set up your `ClientID` and `ClientSecrets` in the `secrets` file
- run the program with your username: `python3 getplaylists.py --username jeffknerr`
- more details see here: https://developer.spotify.com/documentation/web-api

## more details

Note: most of this was done in a terminal on an ubuntu linux 22.04 computer,
but should work on macs and windows, if you can get python3 installed and a 
few python libraries (click, requests).

- create an "app" at the spotify dashboard:
https://developer.spotify.com/dashboard

You're not really making an "app", you're just setting up access tokens.
I didn't even give it much information, just these:
- app name: testspot
- app description: testing spotify api
- redirect uris: http://localhost

If you then click on `Settings` you can see your ClientID, and then
click on the `View client secret`. You want to keep others from seeing/getting
these tokens, so don't add them to a git repo or leave them lying around. 

- copy the secrets-example file and add your tokens to it: `cp secrets-example secrets`

- now run the program with your spotify username:

```
python3 getplaylists.py --username your_user_name
```

By default it does *not* print out track info for each playlist.
Add the `--gettracks` option to get the track info (will take a few
minutes if you have lots of playlists and many tracks per playlist).

Add `--help` if you want to see help on the options.
