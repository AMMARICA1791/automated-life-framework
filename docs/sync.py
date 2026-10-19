import json
import os
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
PUBLIC_FOLDER_ID = "1lwjUclr-Kecj87eoXConjkZslcEBFGZw"
EXCLUDED_KEYWORDS = ("private", "خاص", "سري", "personal")
DESTINATION = Path("hayat")


def is_private_path(path):
    normalized = str(path).replace("\\", "/").casefold()
    return any(word in normalized for word in EXCLUDED_KEYWORDS)


def is_private_folder_name(name):
    return is_private_path(name)


def audit_directory(root=DESTINATION):
    root = Path(root)
    if not root.exists():
        return
    for path in root.rglob("*"):
        if path.is_symlink() or is_private_path(path.relative_to(root)):
            raise RuntimeError("SECURITY: excluded or symbolic-link path detected")
    print("SECURITY: downloaded paths passed privacy audit")


def get_drive_service():
    key_json = json.loads(os.environ["GDRIVE_KEY"])
    credentials = service_account.Credentials.from_service_account_info(
        key_json, scopes=SCOPES
    )
    return build("drive", "v3", credentials=credentials)


def download_folder(service, folder_id, destination):
    page_token = None
    while True:
        response = service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields="nextPageToken,files(id,name,mimeType)",
            pageSize=1000,
            pageToken=page_token,
        ).execute()
        for item in response.get("files", []):
            name = item["name"]
            if name in (".", "..") or "/" in name or "\\" in name:
                raise RuntimeError("SECURITY: unsafe Drive file name")
            target = destination / name
            if is_private_folder_name(name) or is_private_path(target.relative_to(DESTINATION)):
                print("SECURITY: Skipping excluded file or folder")
                continue
            if item["mimeType"] == "application/vnd.google-apps.folder":
                target.mkdir(parents=True, exist_ok=True)
                download_folder(service, item["id"], target)
                continue
            if item["mimeType"] == "application/vnd.google-apps.document":
                target = target.with_name(target.name + ".txt")
                if is_private_path(target.relative_to(DESTINATION)):
                    continue
                data = service.files().export(
                    fileId=item["id"], mimeType="text/plain"
                ).execute()
                target.write_bytes(data)
            else:
                request = service.files().get_media(fileId=item["id"])
                with target.open("wb") as handle:
                    downloader = MediaIoBaseDownload(handle, request)
                    done = False
                    while not done:
                        _, done = downloader.next_chunk()
        page_token = response.get("nextPageToken")
        if not page_token:
            break


if __name__ == "__main__":
    if DESTINATION.exists():
        raise RuntimeError("SECURITY: hayat/ already exists; refusing to overwrite")
    DESTINATION.mkdir()
    print("Only public/ will be published")
    download_folder(get_drive_service(), PUBLIC_FOLDER_ID, DESTINATION)
    audit_directory()
    print("Allowlisted files:", sorted(str(p.relative_to(DESTINATION)) for p in DESTINATION.rglob("*") if p.is_file()))
