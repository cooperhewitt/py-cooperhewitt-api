import urllib
import mimetypes

def encode_multipart_formdata(args):
	""" Encode upload as multipart/form-data. From http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/146306 """
	BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
	CRLF = '\r\n'
	L = []
	for (key, value) in args.items():
		if hasattr(value, 'read'):
			if hasattr(value, 'name'):
				filename = value.name
			elif args.has_key('title'):
				filename = args['title']
			else:
				filename = 'unknown'
			L.append('--' + BOUNDARY)
			L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
			L.append('Content-Type: %s' % get_content_type(filename))
			L.append('')
			L.append(value.read())
		else:
			L.append('--' + BOUNDARY)
			L.append('Content-Disposition: form-data; name="%s"' % key)
			L.append('')
			L.append(value)
	L.append('--' + BOUNDARY + '--')
	L.append('')
	body = CRLF.join(L)
	headers = {
		'Content-Type': 'multipart/form-data; boundary=%s' % BOUNDARY,
		'Content-Length': len(body)
	}
	return (headers, body)

def encode_urlencode(args):
	return ({"Content-type": "application/x-www-form-urlencoded"},urllib.urlencode(args))

def get_content_type(filename):
	return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
