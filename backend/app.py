from flask import Flask, jsonify
from __init__ import create_app, db # 去 __init__.py 创建app
from flask_cors import CORS

from routes.personal_routes import personal_blueprint

app = create_app()
CORS(app)


# 注册蓝图
app.register_blueprint(personal_blueprint)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # 创建数据库表
    app.run(debug=True)
