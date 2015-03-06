import mimetypes

# http://docs.python-requests.org/en/latest/user/advanced/#post-multiple-multipart-encoded-files

def encode_multipart_formdata(args):

        data = {}
        files = []

	for (key, value) in args.items():
		if hasattr(value, 'read'):

			file_name = None
			content_type = None

			if hasattr(value, 'name'):
				file_name = value.name
			elif args.has_key('title'):
				file_name = args['title']
			else:
				file_name = 'unknown'

			content_type = get_content_type(file_name)
			f = (key, (file_name, value, content_type))

			files.append(f)
		else:
			data[key] = value

	# This is so that we can maintain backwards compatibility with
	# the pre- requests (httplib) versions of this library
	# (20150306/copea)

	encoded = {}

	if len(files):
		encoded['files'] = files

	if len(data.keys()):
		encoded['data'] = data

	return encoded
	
def encode_urlencode(data):
        return {'data': data}

def get_content_type(filename):
	return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
