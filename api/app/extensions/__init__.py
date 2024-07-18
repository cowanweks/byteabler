from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from app.extensions.folder_extension import FolderSetup
from app.extensions.db_extension import Base
from flask_cors import CORS


sess = Session()
db = SQLAlchemy(model_class=Base)
folder_setup = FolderSetup()
cors = CORS()
