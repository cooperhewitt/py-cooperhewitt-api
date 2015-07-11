# py-cooperhewitt-api

Python bindings to the Cooper-Hewitt collections API.

## Installation

You can install this by either cloning this repository and running

    	$ python setup.py

or you can use `pip` and just do the following

       $ pip install cooperhewitt.api

## Example

### Plain vanilla

	import cooperhewitt.api.client
	import pprint

	api = cooperhewitt.api.client.OAuth2(ACCESS_TOKEN)

	now = int(time.time())
	args = {'foo': 'bar', 'timestamp': now}

	rsp = api.execute_method('api.test.echo', args)

	print pprint.pformat(rsp)

### Using a proxy

Just pass a `proxy` argument to the constructor

	import cooperhewitt.api.client
	import pprint

	api = cooperhewitt.api.client.OAuth2(ACCESS_TOKEN, proxy='http://proxy.example.com:80')

	now = int(time.time())
	args = {'foo': 'bar', 'timestamp': now}

	rsp = api.execute_method('api.test.echo', args)

	print pprint.pformat(rsp)
	
### Uploading a file

	import cooperhewitt.api.client
	import cooperhewitt.api.request

	import pprint

	api = cooperhewitt.api.client.OAuth2(ACCESS_TOKEN)

	fh = open('/path/to/file', 'rb')
	args = {'file': fh}

	rsp = api.execute_method('api.test.uploadMe', args, cooperhewitt.api.request.encode_multipart_formdata)
	print pprint.pformat(rsp)
	
## See also

* [py-cooperhewitt-api-multiclient](https://github.com/cooperhewitt/py-cooperhewitt-api-multiclient)
* [Smithsonian Cooper-Hewitt National Design Museum collections website](https://collection.cooperhewitt.org/)
* [Smithsonian Cooper-Hewitt National Design Museum collections API](https://collection.cooperhewitt.org/api/)


