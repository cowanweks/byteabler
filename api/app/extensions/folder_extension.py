import os
from flask import Flask


class FolderSetup:
    """Setup templates and static folders"""

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.root_path = os.path.dirname(app.instance_path)
        app.static_foder = os.path.join(self.root_path, "static")
        app.template_folder = os.path.join(self.root_path, "templates")
        self.create_uploads_dir(app)

    def create_uploads_dir(self, app: Flask):
        try:
            upload_path = os.path.join(self.root_path, "uploads")
            app.config.update(UPLOADS_DIR=upload_path)
            os.mkdir(upload_path)
        except FileExistsError:
            print("[*] - Uploads Folder exists skipping this step!")
