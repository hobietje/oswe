import jwt
import json
from codecs import encode, decode
import requests
import hashlib
import hmac
import base64
from cryptography import x509

print("----- PARAMS -----")

# openssl genrsa -out rsa.private 1024
private = open('data/rsa.private', 'rb').read()
print (private)

# openssl rsa -in rsa.private -out rsa.public -pubout -outform PEM
public = x509.load_pem_x509_certificate(open('data/rsa.public', 'rb').read())
print (public)

payload = json.loads(open('data/payload.json', 'r').read())
print (payload)

print("----- ENCODE -----")

encoded = jwt.encode(payload, private, algorithm="PS256", headers={"Me":"Mo"})

# # create an appropriate JSON object for header
# header = b'{"typ":"JWT","alg":"PS256"}'
# header = base64.urlsafe_b64encode(header).rstrip(b"=")

# # create an appropriate JSON object for payload
# payload = base64.urlsafe_b64encode(payload).rstrip(b"=")

# # sign the payload
# sig = hmac.new(public, header + b'.' + payload, hashlib.sha256).digest().strip()
# sig = base64.urlsafe_b64encode(sig).rstrip(b"=")

# print the json token
# encoded = '{}.{}.{}'.format(header.decode(), payload.decode(), sig.decode())
print(encoded)

print("----- VERIFY -----")
header = jwt.get_unverified_header(encoded)
print(header)

payload = jwt.decode(encoded, options={"verify_signature": False})
print(payload)

