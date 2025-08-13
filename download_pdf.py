import requests
import os

URL = "https://www.nasa.gov/wp-content/uploads/2021/12/sls_fact_sheet.pdf"
LOCAL_FILE_NAME = os.path.basename(URL)

response = requests.get(URL)
if response.ok:
    with open(LOCAL_FILE_NAME, "wb") as file_out:
        file_out.write(response.content)
