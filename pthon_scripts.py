import hashlib, hmac, json, requests

secret_key = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "Olisa Macaulay Skyline",
    "email": "info@skylineict.com",
    "resume": "https://drive.google.com/file/d/1Qowr1lvIdOBxAWMJ76fnidiwEodOQJzO/view?usp=sharing",
    "location": "Port Harcourt, Nigeria",
    "linkedin": "https://www.linkedin.com/in/olisa-macaulay-skyline-619672185/",
    "codeLink": "URL to the repo/gist containing THIS script",
    "yearsPython": 7,
    "yearsDjango": 5,
}

body = json.dumps(payload)
my_signature = hmac.new(
    secret_key.encode(),
    body.encode(),
    hashlib.sha3_256,).hexdigest()


# print(my_signature)
# print(body)

response = requests.post(
    endpoint,
    data=body,
    headers={
         "Content-Type": "application/json",
        "X-HMAC-Signature": my_signature,
    }

)

print(response)

