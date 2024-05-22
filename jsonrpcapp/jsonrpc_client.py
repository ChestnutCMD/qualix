import json
import ssl
import urllib.request
import urllib.error
from django.conf import settings


class JSONRPCClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def call_method(self, method, params=None):
        if params is None:
            params = {}
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        payload_bytes = json.dumps(payload).encode('utf-8')

        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_cert_chain(certfile=self._create_temp_file(settings.CLIENT_CERT),
                                keyfile=self._create_temp_file(settings.CLIENT_KEY))

        context.set_ciphers('HIGH:!DH:!aNULL')
        context.verify_mode = ssl.CERT_OPTIONAL

        req = urllib.request.Request(self.endpoint, data=payload_bytes, headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, context=context) as response:
                response_data = json.loads(response.read().decode())
                return response_data
        except urllib.error.HTTPError as e:
            return {"error": f"HTTPError: {e.reason} (code: {e.code})"}
        except urllib.error.URLError as e:
            return {"error": f"URLError: {e.reason}"}
        except ssl.SSLError as e:
            return {"error": f"SSLError: {e.strerror}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}

    @staticmethod
    def _create_temp_file(content):
        import tempfile
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(content.encode('utf-8'))
        temp.close()
        return temp.name
