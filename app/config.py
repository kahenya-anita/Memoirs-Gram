import os



class Config:
    SECRET_KEY =  os.urandom(32)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://scgyqlylggnxkt:35e51f5b6aa14afe9bdc51402c729bd461206862a039d4a9d7b6aee2e7ccb4fb@ec2-34-234-185-150.compute-1.amazonaws.com:5432/dfneilmdasjmin'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}