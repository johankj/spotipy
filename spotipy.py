import requests

class spotifywebapi(object):
	"""docstring for spotifywebapi"""
	def __init__(self):
		self.baseurl = 'http://ws.spotify.com/'
		self.apiversion = 1
	
	def get(self, **kwargs):
		if not 'type' in kwargs: kwargs['type'] = ''
		r = requests.get(
				'%s%s/%i/%s.json' % (self.baseurl, kwargs['service'], self.apiversion, kwargs['type']),
				params=kwargs['params']
			)
		print r.url
		r.raise_for_status() # Raise on a bad request (status_code !== 200)
		return r.json()
		


class search(object):
	@classmethod
	def album(self, name, **kwargs):
		kwargs.update({'q':name})
		return spotifywebapi().get(service='search', type='album', params=kwargs)
	
	@classmethod
	def artist(self, name, **kwargs):
		kwargs.update({'q':name})
		return spotifywebapi().get(service='search', type='artist', params=kwargs)
	
	@classmethod
	def track(self, name, **kwargs):
		kwargs.update({'q':name})
		return spotifywebapi().get(service='search', type='track', params=kwargs)

def lookup(uri, **kwargs):
	kwargs.update({'uri':uri})
	return spotifywebapi().get(service='lookup', params=kwargs)

