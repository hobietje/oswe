import jwt
import json
from codecs import encode, decode
import requests
import hashlib
import hmac
import base64

print("----- PARAMS -----")

secret = open('data/secret.txt', 'rb').read()
print (secret)

jwt_before = open('data/jwt.json', 'rb').read()
print (jwt_before)

payload_desired = open('data/payload.json', 'rb').read()
print (payload_desired)

print("----- PARSE -----")

# create an appropriate JSON object for header
header_before = jwt.get_unverified_header(jwt_before)
print(header_before)

payload_before = jwt.decode(jwt_before, secret, algorithms="HS256", options={"verify_signature": True})
print(payload_before)

print("----- ENCODE -----")
# create an appropriate JSON object for payload
payload = base64.urlsafe_b64encode(payload_desired).rstrip(b"=")

# sign the payload
header = base64.urlsafe_b64encode(json.dumps(header_before).encode()).rstrip(b"=")
sig = hmac.new(secret, header + b'.' + payload, hashlib.sha256).digest().strip()
sig = base64.urlsafe_b64encode(sig).rstrip(b"=")

# print the json token
encoded = '{}.{}.{}'.format(header.decode(), payload.decode(), sig.decode())
print(encoded)

print("----- VERIFY -----")
header_after = jwt.get_unverified_header(encoded)
print(header_after)

payload_after = jwt.decode(encoded, options={"verify_signature": False})
print(payload_after)

