from flask import Flask
from models import db, User, ImageSet, ImageReview, Article
from flask_admin import Admin
from admin_views import UserView, ImageSetView, ImageReviewView, ArticleView


def create_app():
    app = Flask(__name__)
    app.secret_key = '550e8400-e29b-41d4-4466a716-55440000'

    
    
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Yxh20021211@localhost/ruixy?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # 初始化数据库
    db.init_app(app)


    # 设置管理面板
    admin = Admin(app, name='管理面板', template_mode='bootstrap3')
    # 添加模型到管理员界面
    admin.add_view(UserView(User, db.session))
    admin.add_view(ImageSetView(ImageSet, db.session))
    admin.add_view(ImageReviewView(ImageReview, db.session))
    admin.add_view(ArticleView(Article, db.session))


    # # 初始化 Redis
    # redis_client = Redis(host='localhost', port=6379, db=0)


    # # 配置 Flask-Limiter 使用 Redis 存储
    # limiter = Limiter(
    #     key_func=get_remote_address,
    #     storage_uri='redis://localhost:6379/0',  # 使用 Redis 存储
    #     default_limits=["20 per minute"]  # 每个IP地址每分钟最多5次请求
    # )
    # limiter.init_app(app)


    return app
