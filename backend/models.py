from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy

# 创建一个 SQLAlchemy 实例
db = SQLAlchemy()


# 用户
class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_charset': 'utf8mb4'}  # 指定字符集
    
    id = db.Column(db.Integer, primary_key=True)  # 自增ID
    uid = db.Column(db.String(20), unique=True, nullable=False)  # UID
    username = db.Column(db.String(100), unique=True, nullable=False)  # 用户名
    avatar = db.Column(db.String(255), nullable=True)  # 头像URL
    role = db.Column(db.String(50), nullable=False)  # 用户类型，例如 'admin', 'regular'
    phone_number = db.Column(db.String(20), nullable=False)  # 电话号码
    email = db.Column(db.String(100), unique=True, nullable=True)  # 邮箱
    password = db.Column(db.String(255), nullable=False) # 密码
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # 创建时间


# 验证信息
class VerificationCode(db.Model):
    __tablename__ = 'verification_codes'
    id = db.Column(db.Integer, primary_key=True)  # 自增ID
    phone_number = db.Column(db.String(20), nullable=False)  # 用户电话号码
    code = db.Column(db.String(10), nullable=False)  # 验证码
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # 创建时间
    expires_at = db.Column(db.DateTime, nullable=False)  # 过期时间

    def is_expired(self):
        return datetime.utcnow() > self.expires_at



# 图片集
class ImageSet(db.Model):
    __tablename__ = 'image_sets'
    __table_args__ = {'mysql_charset': 'utf8mb4'}  # 指定字符集
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)  # 添加描述字段
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


# 种类
class Category(db.Model):
    __tablename__ = 'categories'
    __table_args__ = {'mysql_charset': 'utf8mb4'}  # 指定字符集
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# 图片的种类
class ImageCategory(db.Model):
    __tablename__ = 'image_categories'
    __table_args__ = {'mysql_charset': 'utf8mb4'}  # 指定字符集
    
    image_id = db.Column(db.Integer, db.ForeignKey('image_sets.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)


# 用户评价
class ImageReview(db.Model):
    __tablename__ = 'image_reviews'
    __table_args__ = {'mysql_charset': 'utf8mb4'}  # 指定字符集
    
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image_sets.id'), nullable=False)
    user_uid = db.Column(db.String(20), db.ForeignKey('users.uid'), nullable=False) # 使用 uid 作为外键
    comment = db.Column(db.Text, nullable=True)  # 评价字段
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # 定义关系
    image_set = db.relationship('ImageSet', backref='image_reviews')
    user = db.relationship('User', backref='image_reviews')


# 文章集
class Article(db.Model):
    __tablename__ = 'articles'
    __table_args__ = {'mysql_charset': 'utf8mb4'}  # 指定字符集

    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(255), nullable=False)  # 文章名称
    article_url = db.Column(db.String(255), nullable=False)  # 文章文件的相对路径
    description = db.Column(db.Text, nullable=True)  # 文章描述
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # 创建时间