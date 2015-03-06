# py-cooperhewitt

Python bindings to the Cooper-Hewitt collections API.

## Example

### Plain vanilla

	import cooperhewitt.api.client
	import pprint

	api = cooperhewitt.api.client.OAuth2(ACCESS_TOKEN)

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
	
## TO DO

* Use [py-flamework-api](https://github.com/cooperhewitt/py-flamework-api) as a base class

## See also

* [Smithsonian Cooper-Hewitt National Design Museum collections website](https://collection.cooperhewitt.org/)
* [Smithsonian Cooper-Hewitt National Design Museum collections API](https://collection.cooperhewitt.org/api/)


