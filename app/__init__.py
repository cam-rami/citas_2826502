from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

##IMPORTAR EL COFING
from .config import Config

##crear objeto de aplicacion 
app = Flask (__name__)

## configurar  el objeto flask con el config
app.config.from_object(Config)

##objeto SQLALAchemy
db = SQLAlchemy(app)

## objeto para las migraciones 
migrate = Migrate(app , db)

#importar los modelos
from .models import Medico

