import jwt
import json
from codecs import encode, decode
import requests
import hashlib
import hmac
import base64

print("----- PARAMS -----")

payload = open('data/payload.json', 'rb').read()
print (payload)

print("----- ENCODE -----")

# create an appropriate JSON object for header
header = b'{"typ":"JWT","alg":"none"}' # NOTE: old implementations may want 'None'
header = base64.urlsafe_b64encode(header).rstrip(b"=")

# create an appropriate JSON object for payload
payload = base64.urlsafe_b64encode(payload).rstrip(b"=")

# sign the payload
sig = b""

# print the json token
encoded = '{}.{}.{}'.format(header.decode(), payload.decode(), sig.decode())
print(encoded)

print("----- VERIFY -----")
header = jwt.get_unverified_header(encoded)
print(header)

payload = jwt.decode(encoded, options={"verify_signature": False})
print(payload)

