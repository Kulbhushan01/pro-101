import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(access_token)

    def upload_file(self, file_from, file_to):
        with open(file_from, 'rb') as f:
            file_name = os.path.basename(file_from)
            file_to = os.path.join(file_to, file_name)
            print(f"Uploading {file_name} to Dropbox...")
            self.dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))
            print("Upload successful!")

def main():
    access_token = input("Enter your Dropbox access token: ")

    file_from = input("Enter the full path of the file to upload: ")

    file_to = input("Enter the full path to upload the file to in Dropbox: ")

    transfer_data = TransferData(access_token)

    transfer_data.upload_file(file_from, file_to)

if __name__ == "__main__":
    main()
