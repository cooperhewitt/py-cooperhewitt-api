# py-cooperhewitt

Python bindings to the Cooper-Hewitt collections API.

They lack some basic things like a `setup.py` but are being made available, now,
as a reference implementation and will be updated in real-time.

## Example

	import cooperhewitt.api.client
	import pprint

	# see also: https://collection.cooperhewitt.org/api/oauth2/

	api = cooperhewitt.api.client.OAuth2(ACCESS_TOKEN)

        now = int(time.time())
        rsp = api.call('api.test.echo', foo='bar', timestamp=now)
        print pprint.pformat(rsp)

## See also

* [Smithsonian Cooper-Hewitt National Design Museum collections website](https://collection.cooperhewitt.org/)
* [Smithsonian Cooper-Hewitt National Design Museum collections API](https://collection.cooperhewitt.org/api/)


