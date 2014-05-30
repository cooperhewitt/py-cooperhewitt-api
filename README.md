# py-cooperhewitt

Python bindings to the Cooper-Hewitt collections API.

## Example

	import cooperhewitt.api.client
	import pprint

	api = cooperhewitt.api.client.OAuth2(ACCESS_TOKEN)

	now = int(time.time())
	args = {'foo': 'bar', 'timestamp': now}

	rsp = api.execute_method('api.test.echo', args)

	print pprint.pformat(rsp)

## TO DO

* Use [py-flamework-api](https://github.com/cooperhewitt/py-flamework-api) as a base class

## See also

* [Smithsonian Cooper-Hewitt National Design Museum collections website](https://collection.cooperhewitt.org/)
* [Smithsonian Cooper-Hewitt National Design Museum collections API](https://collection.cooperhewitt.org/api/)


