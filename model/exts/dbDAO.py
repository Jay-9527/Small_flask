"""
数据DAO层
"""
from flask_sqlalchemy import SQLAlchemy
from setting import config

db = SQLAlchemy()

'''
映射数据类
'''


class usinfo(db.Model):
    __tablename__ = "user_basic"

    id = db.Column(db.Integer, primary_key=True, doc="用户ID")
    modile = db.Column(db.String(11), doc="手机号")
    name = db.Column(db.String(20), doc="用户名")
    password = db.Column(db.String(20), doc="用户密码")
    is_active = db.Column(db.Boolean, defaults=False)

    def to_dict(self):
        return {
            'id': self.id,
            'modile': self.modile,
            'name': self.name,
            'password': self.password,
            'active': self.is_active
        }

    def get_id(self):
        return self.id

    def get_active(self):
        return self.is_active

    def get_us_name(self):
        return self.name

    def get_us_model(self):
        return self.modile


# 建链接
db.create_all()
