spotipy
=======

A very basic one-file-wrapper around the Spotify Web API.

It supports the ``search`` and ``lookup`` and the parameters supported for the endpoints, as per the [Spotify Web API](https://developer.spotify.com/technologies/web-api/).

## Requirements
This simple module requires [requests](http://docs.python-requests.org/). It has only been tested with requests >= 1.0 and with Python 2.7.

```console
pip install requests
```

## Usage

This app is very straight-forward to use. To get started, import the Spotify API-wrapper:

```python
import spotipy
```

From here, you can search for artists, albums, and tracks:

```python
# search for albums
results = spotipy.search.album('This Is War')
for album in results['albums']:
    print u'{} by {}'.format(album['name'], album['artists'][0]['name'])

# search for artists
results = spotipy.search.artist('Coldplay')
for artist in results['artists']:
    print artist['name']

# search for tracks
results = spotipy.search.track('Alligator Sky')
for track in results['tracks']:
    print u'{trackname} on {album} by {artist}'.format(trackname=track['name'], album=track['album']['name'], artist=track['artists'][0]['name'])
```

You can also look up an album, an artist or a song by its Spotify URI. 

```python
# find album by uri
album = spotipy.lookup('spotify:album:6z5HJQIAnzBaaEbYwfbwq9', extras='trackdetail')
```
