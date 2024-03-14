import schedule
import time
import requests

# Set up your bot's API token
TOKEN = '6469429177:AAF62qr8pS7eu3mzD8q-yVUbZM271clNchE'

# Set up the URL for the sendDocument method
url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

# Specify the chat ID where you want to send the document
chat_id = '1316618548'

# Specify the file path of the document to upload
document_path = './beach.jpg'

# Function to upload the document
def upload_document():
    with open(document_path, 'rb') as document:
        files = {'document': document}
        data = {'chat_id': chat_id}
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print("Document uploaded successfully")
        else:
            print("Failed to upload document:", response.text)

# Schedule the document upload every five seconds
schedule.every(5).seconds.do(upload_document)

# Main loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
