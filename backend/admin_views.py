from flask_admin.contrib.sqla import ModelView
import os
import shutil
import uuid
import random
from werkzeug.security import generate_password_hash
from models import db, User
from flask import current_app

class ImageSetView(ModelView):
    # 自定义的视图，用于管理 ImageSet 模型
    def on_model_delete(self, model):
        """重写删除方法，删除数据库记录时也删除对应的评论"""
        # 删除与该 ImageSet 相关的所有评论
        for review in model.image_reviews:
            db.session.delete(review)  # 删除评论
        db.session.commit()  # 提交更改


        """重写删除方法，删除数据库记录时也删除对应的文件"""
        # 构建文件的绝对路径
        file_path = os.path.join(current_app.static_folder, model.image_url)

        # 检查原图片文件是否存在
        if os.path.exists(file_path):
            # 删除本地文件
            os.remove(file_path)

        # 调用父类的删除方法
        super().on_model_delete(model)



class UserView(ModelView):
    def on_model_change(self, form, model, is_created):
        # 只在创建新用户时生成 UID
        if is_created:
            model.uid = self.generate_uid()  # 自动生成 UID
            model.password = generate_password_hash(form.password.data)  # 哈希密码
            
    def generate_uid(self):
        while True:
            uid = str(uuid.uuid4().int)
            random_number = random.randint(1000, 9999)
            new_uid = uid[:10] + str(random_number)
            
            # 检查是否在数据库中已存在相同的 UID
            if not User.query.filter_by(uid=new_uid).first():
                return new_uid



class ImageReviewView(ModelView):
    pass  # 在这里可以添加自定义的 ImageReview 视图逻辑



class ArticleView(ModelView):
    def on_model_delete(self, model):
        """重写删除方法，删除数据库记录时也删除对应的文件夹"""
        # 获取 article_url 中的文件夹路径
        article_folder = os.path.dirname(model.article_url)  # 获取文件夹路径

        # 构建文件夹的绝对路径
        folder_path = os.path.join(current_app.static_folder, article_folder)

        # 检查文件夹是否存在
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # 删除整个文件夹及其内容
            shutil.rmtree(folder_path)

        # 调用父类的删除方法，删除数据库中的记录
        super().on_model_delete(model)
