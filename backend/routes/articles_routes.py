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



@articles_blueprint.route('/upload_article_content', methods=['POST'])
def upload_article_content():
    # 获取文章名称和描述
    article_name = request.form.get('articleName')
    article_description = request.form.get('articleDescription')
    html_content = request.form.get('htmlContent')

    # 检查输入是否合法
    if not article_name or not article_description or not html_content:
        return jsonify(success=False, message='文章名称、描述和内容不能为空。'), 400
    
    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 删除所有 <style> 标签（去除嵌入式 CSS）
    for style_tag in soup.find_all('style'):
        style_tag.decompose()

    # 删除所有行内样式
    for tag in soup.find_all(True):  # True 表示匹配所有标签
        if 'style' in tag.attrs:
            del tag.attrs['style']

    # 将处理后的 HTML 转换为字符串
    cleaned_html_content = str(soup)


    # 获取上传的图像文件
    images = request.files.getlist('images[]')
    if not images:
        return jsonify(success=False, message='未上传任何图像。'), 400
    

    # 创建新的文件夹路径，使用当前时间戳作为文件夹名称
    current_time = datetime.now().strftime("%Y%m%d%H%M%S") # 获取当前时间并格式化为所需格式（例如：20240925185953）
    folder_name = f'article_{current_time}'

    # 设置上传文件的保存路径（仅用于存储时的路径）
    UPLOAD_FOLDER = os.path.join('static', 'articles', folder_name)
    # 确保上传文件夹存在
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


    # 保存 html 文件，重命名为当前时间戳
    html_file_name = f'article_{current_time}.html'  # 将 html 文件重命名
    html_file_path = os.path.join(UPLOAD_FOLDER, html_file_name)  # 指定文件名和路径
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_html_content)

    # 保存所有图像文件
    for image in images:
        # 使用 os.path.basename() 来提取文件名
        image_filename = os.path.basename(image.filename)
        image_file_path = os.path.join(UPLOAD_FOLDER, image_filename)  # 指定文件名和路径
        image.save(image_file_path)

        # 在 HTML 中查找所有与该图片文件名匹配的 <img> 标签
        for img in soup.find_all('img'):
            original_src = img.get('src')  # 获取原始的 src 属性
            if original_src:
                # URL 解码，处理像空格等特殊字符
                decoded_src = urllib.parse.unquote(original_src)
                # 提取 src 中的文件名部分（忽略路径）
                img_filename = os.path.basename(decoded_src)

                if img_filename == image_filename:  # 如果文件名匹配
                    # 更新 <img> 标签的 src 路径为相对路径
                    img['src'] = f'/static/articles/{folder_name}/{image_filename}'
                    print(f"Updated image src: {img['src']}")

                    # 如果有父级 <a> 标签，更新其 href 属性
                    parent_link = img.find_parent('a')
                    if parent_link:
                        parent_link['href'] = img['src']
                        print(f"Updated parent link href: {parent_link['href']}")

    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))  # 使用 soup 生成最终的 HTML 内容


    # 生成相对路径(从 "static" 后开始存储）
    relative_file_path = os.path.join('articles', folder_name, html_file_name)

    # 将文件路径中的反斜杠替换为正斜杠
    relative_file_path = relative_file_path.replace('\\', '/')

    # 将文章信息存储到数据库
    new_article = Article(
        name=article_name,
        article_url=relative_file_path,
        description=article_description
    )
    db.session.add(new_article)
    db.session.commit()

    # 获取新插入行的 id
    article_id = new_article.id

    return jsonify(success=True, message='文章上传成功！', articleID = article_id, articleName=article_name, articleDescription=article_description, articleUrl=relative_file_path)



@articles_blueprint.route('/get_articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()  # 获取所有文章
    articles_data = [{
        'id': article.id,
        'title': article.name,
        'link': url_for('static', filename=article.article_url, _external=True),  # 转换为完整 URL
        'description': article.description,
        'date': article.created_at.strftime('%Y-%m-%d %H:%M:%S')
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
