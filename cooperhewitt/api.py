import urllib
import httplib
import json

class API:

    def __init__(self, access_token, host='api.collection.cooperhewitt.org', endpoint='/rest'):
        self.host = host
        self.endpoint = endpoint
        self.access_token = access_token
        
    def call (self, method, **kwargs):

        kwargs['method'] = method
        kwargs['format'] = 'json'
        kwargs['access_token'] = self.access_token

        headers = {"Content-type": "application/x-www-form-urlencoded"}

        body = urllib.urlencode(kwargs)

        conn = httplib.HTTPSConnection(self.host)
        conn.request('POST', self.endpoint, body, headers)

        rsp = conn.getresponse()
        data = json.load(rsp)

        # check status here...

        return data

if __name__ == '__main__':

    import sys
    import pprint
    import time
    import optparse

    parser = optparse.OptionParser(usage="python api.py --access-token <ACCESS TOKEN>")

    parser.add_option('--access-token', dest='access_token',
                        help='Your Cooper-Hewitt API access token',
                        action='store')

    parser.add_option('--endpoint', dest='endpoint',
                        help='The Cooper-Hewitt API endpoint',
                        action='store', default='api.collection.cooperhewitt.org')

    options, args = parser.parse_args()

    api = API(options.access_token, options.endpoint)

    try:
        now = int(time.time())

        rsp = api.call('test.echo', foo='bar', timestamp=now)
        print pprint.pformat(rsp)

    except Exception, e:
        print e

    sys.exit()
