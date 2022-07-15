from flask import Blueprint

from app import create_app
from model.exts.dbDAO import db

bp = Blueprint("user", __name__, url_prefix="/user")

apps = create_app()


@bp.route("/login/<int:user_id>", methods=['GET', 'POST'])
def getUserId(user_id):
    db.create_all(['user_info'])  # 引用表

    return


# def login():
#     name = request.args.get('name')
#     user_id = request.args.get('user_id')
#     return jsonify({'name': name, 'user_id': user_id})


'''
查询
'''
