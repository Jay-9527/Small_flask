from flask import Blueprint, request, jsonify
from model.exts.dbDAO import db, usinfo

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login/<int:user_id>,<string:user_name>", methods=['GET', 'POST'])
def login():
    name = request.args.get('user_name')
    user_id = request.args.get("user_id")
    return "user Pi" + jsonify({'name': name, 'user_id': user_id})


# def login():
#     name = request.args.get('name')
#     user_id = request.args.get('user_id')
#     return jsonify({'name': name, 'user_id': user_id})


'''
查询
'''
