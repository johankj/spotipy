import spotipy

album = spotipy.search.album('The Midsummer Station', page=1)['albums'][0]
print '{} by {}: {}'.format(album['name'], album['artists'][0]['name'], album['href'])

artist = spotipy.search.artist('Foo Fighters')['artists'][0]
print '{}: {}'.format(artist['name'], artist['href'])

res = spotipy.search.track('Christmas Lights')['tracks'][0]
print '{} is on the album {} by {}: '.format(res['name'], res['album']['name'], res['artists'][0]['name'], res['href'])

print spotipy.lookup('spotify:artist:1bDWGdIC2hardyt55nlQgG')['artist']['name']