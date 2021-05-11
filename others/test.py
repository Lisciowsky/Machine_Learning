import requests
import base64
import os
dire = "/home/kuba/Downloads"
os.chdir(dire)

URL = "http://127.0.0.1:5000/zdjecie"

#  first, encode our image with base64
with open("comic(1).png", "rb") as imageFile:
    img = base64.b64encode(imageFile.read())

response = requests.post(URL, data={"name":"obama", "img":str(img)})
print(response.content)