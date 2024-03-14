#import area
import requests

TOKEN = '6469429177:AAF62qr8pS7eu3mzD8q-yVUbZM271clNchE'
url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

chat_id = '1316618548'

# Specify the file to upload
file_path = './beach.jpg'

# Open the file
with open(file_path, 'rb') as file:
    # Prepare the request payload
    files = {'document': file}
    data = {'chat_id': chat_id}

    # Send the request
    response = requests.post(url, files=files, data=data)

# Check the response
if response.status_code == 200:
    print("File uploaded successfully")
else:
    print("Failed to upload file:", response.text)