from flask import Blueprint, request, jsonify, current_app, url_for, render_template
from models import db, Article
from datetime import datetime
import os
import shutil
import urllib.parse

# 创建蓝图
articles_blueprint = Blueprint('articles_blueprint', __name__)


# 打开文章页面
@articles_blueprint.route('/articles')
def articles():
    return render_template('articles.html')



@articles_blueprint.route('/article/<int:article_id>')
def article_page(article_id):
    article = Article.query.get(article_id)
    if article:
        return render_template('current_article.html', article=article)
    else:
        return 'Article not found', 404



@articles_blueprint.route('/upload_article_link', methods=['POST'])
def upload_article_link():
    # 获取文章名称和描述
    article_url = request.form.get('articleUrl')
    article_title = request.form.get('articleTitle')

    # 检查输入是否合法
    if not article_url or not article_title:
        return jsonify(success=False, message='文章URL、标题不能为空。'), 400
    
    # 将文章信息存储到数据库
    new_article = Article(
        name=article_title,
        article_url=article_url
    )
    db.session.add(new_article)
    db.session.commit()

    # 获取新插入行的 id
    article_id = new_article.id

    return jsonify(success=True, message='文章上传成功！', articleID = article_id, articleTitle=article_title, articleUrl=article_url)



@articles_blueprint.route('/get_articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()  # 获取所有文章
    articles_data = [{
        'id': article.id,
        'title': article.name,
        'link': article.article_url, # URL
        'description': article.description,
        'date': article.created_at.strftime('%Y-%m-%d')
    } for article in articles]

    return jsonify(articles_data)



@articles_blueprint.route('/get_article/<int:article_id>')
def get_article(article_id):
    # 假设你有一个Article模型存储文章数据
    article = Article.query.get(article_id)
    
    if article:
        # 获取文章的相对路径，并添加 static 文件夹路径
        article_name = article.name
        article_relative_path = article.article_url
        article_path = os.path.join(current_app.static_folder, article_relative_path)
        # 获取文章的文件夹路径（假设它在 static 文件夹内）
        article_folder_path = os.path.dirname(article_relative_path)

        # 检查文件是否存在
        if os.path.exists(article_path) and article_path.endswith('.html'):
            try:
                # 读取 html 文件内容
                with open(article_path, 'r', encoding='utf-8') as file:
                    html_content = file.read()

                # 返回文章内容和文件夹路径
                return jsonify({
                    'article_name' : article_name,
                    'html_content': html_content,
                    'folder_path': article_folder_path  # 传递文件夹路径
                })
            except Exception as e:
                return jsonify({'error': 'Error reading file', 'details': str(e)}), 500
        else:
            return jsonify({'error': 'File not found or invalid file format'}), 404
    else:
        return jsonify({'error': 'Article not found'}), 404
    


@articles_blueprint.route('/save_article_content', methods=['POST'])
def save_article_content():
    data = request.get_json()
    article_id = data.get('articleID')
    new_content = data.get('content')

    if not article_id or not new_content:
        return jsonify(success=False, message="缺少文章 ID 或内容"), 400

    # 从数据库中查找文章
    article = Article.query.get(article_id)
    if not article:
        return jsonify(success=False, message="未找到对应的文章"), 404

    # 获取文章对应的 HTML 文件路径
    html_file_path = os.path.join('static', article.article_url)  # 使用数据库中的路径

    try:
        # 将新内容写入文件
        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        # 如果需要，还可以在数据库中更新文章记录
        db.session.commit()

        return jsonify(success=True, message="文章内容已保存")

    except Exception as e:
        return jsonify(success=False, message=f"保存文件时出错: {str(e)}"), 500
    


@articles_blueprint.route('/update_article/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    data = request.get_json()
    article = Article.query.get(article_id)
    if article:
        article.name = data.get('name', article.name)
        article.description = data.get('description', article.description)
        db.session.commit()  # 提交更改
        return jsonify({'success': True, 'message': 'Article updated successfully'})
    return jsonify({'success': False, 'message': 'Article not found'}), 404



@articles_blueprint.route('/delete_article/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = Article.query.get(article_id)
    if article:
        # 获取 article_url 中的文件夹路径
        article_folder = os.path.dirname(article.article_url)  # 获取文件夹路径

        # 构建文件夹的绝对路径
        folder_path = os.path.join(current_app.static_folder, article_folder)

        # 检查文件夹是否存在
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # 删除整个文件夹及其内容
            shutil.rmtree(folder_path)

        # 删除数据库中的记录
        db.session.delete(article)
        db.session.commit()  # 提交删除
        return jsonify({'success': True, 'message': 'Article deleted successfully'})
    
    return jsonify({'success': False, 'message': 'Article not found'}), 404
