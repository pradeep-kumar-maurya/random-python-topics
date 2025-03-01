import requests

# Path to the self-signed certificate (CA cert)
cert_path = 'server.crt'  # Path to the certificate you used for the server

# Make a GET request to the server, passing the custom CA cert for verification
response = requests.get('http://localhost:4443/server.py', verify=cert_path)

print("Status Code:", response.status_code)
print("Response Content:", response.text)
