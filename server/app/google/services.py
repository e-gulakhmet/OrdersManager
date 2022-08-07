from django.conf import settings
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from app.utils.patterns import MetaSingleton


class GoogleDriveService(metaclass=MetaSingleton):
    gauth = GoogleAuth(settings.GOOGLE_DRIVE_SETTINGS_FILE)
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    def get_file_data(self, file_id: str) -> str:
        file = self.drive.CreateFile({'id': file_id})
        return file.GetContentString()
