import os
import jwt
import requests
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

PRIVY_APP_ID = "cmph0wa1300110cjr9eyypdv6"
PRIVY_JWKS_URL = f"https://auth.privy.io/api/v1/apps/{PRIVY_APP_ID}/jwks.json"
_jwks_client = jwt.PyJWKClient(PRIVY_JWKS_URL, cache_keys=True)

try:
    signing_key = _jwks_client.get_signing_key_from_jwt("dummy_token")
except Exception as e:
    print(e)
