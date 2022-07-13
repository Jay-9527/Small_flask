from flask import Flask
from model.exts.dbDAO import db
from setting import config
from model import users_bp
from model import index_bp
# 小程序后端程序创建
# 定义数据库


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 绑定数据库
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(users_bp)
    app.register_blueprint(index_bp)
    return app
