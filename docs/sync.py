import os
import json
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import subprocess
import shutil

EXCLUDED_FOLDERS = {'private', 'Private'}
EXCLUDED_PATH_KEYWORDS = ['journal/private', 'private']

def is_private_path(path):
    parts = path.replace('\\', '/').lower().split('/')
    return 'private' in parts or any(keyword in path.replace('\\', '/').lower() for keyword in EXCLUDED_PATH_KEYWORDS)

# هذا السكريبت يعمل في GitHub Actions - يسحب من Drive ويدفع إلى GitHub
# أنت لا تشغله يدوياً

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = '1esjXi0Lb8S8jeXYEPCb7BaN6zpqGe2n2'  # automated-life-framework

def get_drive_service():
    key_json = json.loads(os.environ['GDRIVE_KEY'])
    creds = service_account.Credentials.from_service_account_info(key_json, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

def download_folder(service, folder_id, dest='.'):
    query = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields="files(id, name, mimeType)").execute()
    files = results.get('files', [])
    for f in files:
        path = os.path.join(dest, f['name'])
        if is_private_path(path) or f['name'].lower() == 'private':
            print('Skipping private folder - stays in Drive only')
            continue
        if f['mimeType'] == 'application/vnd.google-apps.folder':
            os.makedirs(path, exist_ok=True)
            download_folder(service, f['id'], path)
        else:
            # للـ Google Docs نصدرها كـ md أو txt
            if 'document' in f['mimeType']:
                data = service.files().export(fileId=f['id'], mimeType='text/plain').execute()
                with open(path + '.txt', 'wb') as fh:
                    fh.write(data)
            else:
                request = service.files().get_media(fileId=f['id'])
                fh = io.FileIO(path, 'wb')
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while not done:
                    _, done = downloader.next_chunk()

if __name__ == '__main__':
    service = get_drive_service()
    if os.path.exists('hayat'):
        shutil.rmtree('hayat')
    os.makedirs('hayat', exist_ok=True)
    download_folder(service, FOLDER_ID, 'hayat')
    print("Downloaded from Drive")
