"""
数据DAO层
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy(app=create_engine())

'''
映射数据类
'''

# 创建链接
db.create_all(bind="userid")
