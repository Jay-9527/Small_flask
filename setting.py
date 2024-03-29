"""
配置文件
"""
import base64
import os


class Config:
    # 项目安全密钥
    SECRET_KEY = base64.b64encode(os.urandom(24)).decode()
    # 微信ID
    APP_ID = ''
    APP_SECRET = ''
    # APP_API_URL 'GET https://api.weixin.qq.com/sns/jscode2session'
    APP_API_URL = 'https://api.weixin.qq.com/sns/jscode2session?appid=${0}&secret=${1}&js_code=${2}&grant_type=authorization_code'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # DB_USERS = os.getenv("DB_USERS")
    # DB_PASSW = os.getenv("DB_PASSW")

    DB_USERS = 'adiao'
    DB_PASSW = 'adiao'
    DB_CHARSET = 'utf-8'
    # DB_URL = os.getenv("DB_URL", os.environ.get("DB_URL")) + "%s+%s+%s" + DB_USERS + DB_PASSW + DB_CHARSET
    DB_URL = 'localhost'


class ProductionsConfig(Config):
    # DB_USERS = os.getenv("DB_USERS")
    # DB_PASSW = os.getenv("DB_PASSW")
    DB_USERS = 'adiao'
    DB_PASSW = 'adiao'
    DB_CHARSET = 'utf-8'
    # DB_URL = os.getenv("DB_URL", os.environ.get("DB_URL")) + "%s+%s+%s" + DB_USERS + DB_PASSW + DB_CHARSET
    DB_URL = 'localhost'


class TestingConfig(Config):
    TESTING = True
    # DB_USERS = os.getenv("DB_USERS")
    # DB_PASSW = os.getenv("DB_PASSW")
    DB_URL = 'localhost'
    DB_USERS = 'adiao'
    DB_PASSW = 'adiao'
    DB_CHARSET = 'utf-8'
    # DB_URL = os.getenv("DB_URL", os.environ.get("DB_URL")) + "%s+%s+%s" + DB_USERS + DB_PASSW + DB_CHARSET


config = {
    'development': DevelopmentConfig,
    'productions': ProductionsConfig,
    'testing': TestingConfig,
    'defaults': DevelopmentConfig
}
