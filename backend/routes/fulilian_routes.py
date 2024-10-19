from flask import Blueprint, request, jsonify, current_app, session, send_from_directory
from models import db, ImageSet, ImageReview, User
import os
from datetime import datetime
from werkzeug.utils import secure_filename


# 创建蓝图
fulilian_blueprint = Blueprint('fulilian_blueprint', __name__)


# 上传图片
@fulilian_blueprint.route('/upload_image', methods=['POST'])
def upload_image():
    # 设置上传文件的保存路径（仅用于存储时的路径）
    UPLOAD_FOLDER = os.path.join(current_app.root_path, 'static', 'uploads', 'atlas', 'fulilian')
    # 确保上传文件夹存在
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # 从请求中获取文件
    file = request.files['image_input']
    image_name = request.form['name']  # 从表单获取图像名称
    image_description = request.form['description']

    # 确保文件名安全并生成完整路径
    filename = secure_filename(file.filename)
    file_extension = os.path.splitext(filename)[1]  # 获取文件扩展名

    # 生成新的文件名（例如：fulilian_当前时间.扩展名）
    current_time = datetime.now().strftime("%Y%m%d%H%M%S") # 获取当前时间并格式化为所需格式（例如：20240925185953）
    new_filename = f"fulilian_{current_time}{file_extension}"

    # 原始图片保存路径
    file_path = os.path.join(UPLOAD_FOLDER, new_filename)

    # 保存原始图片
    file.save(file_path)

    # 生成保存的相对路径，从 "static" 后开始存储）
    relative_file_path = os.path.join('uploads', 'atlas', 'fulilian', new_filename)

    # 将文件路径中的反斜杠替换为正斜杠
    relative_file_path = relative_file_path.replace('\\', '/')

    # 创建新的 ImageSet 实例，仅存储文件路径
    new_image_set = ImageSet(
        name=image_name,
        image_url=relative_file_path,  # 存储相对路径
        description=image_description
    )
    db.session.add(new_image_set)
    db.session.commit()

    # 获取新插入行的 id
    new_id = new_image_set.id

    return jsonify(success=True, image_url=relative_file_path, id=new_id)


# 获取每个set的详细信息
@fulilian_blueprint.route('/get_set_info/<int:set_id>', methods=['GET'])
def get_set_info(set_id):
    image_set = ImageSet.query.get(set_id)
    if image_set:
        return jsonify({
            'url': image_set.image_url,
            'name': image_set.name,
            'description': image_set.description
        })
    return jsonify({'error': 'Image set not found'}), 404


# 添加评论
@fulilian_blueprint.route('/add_comment', methods=['POST'])
def add_comment():
    # if 'user_uid' not in session:
    #     return jsonify({'error': '用户未登录'}), 401

    data = request.json
    image_id = data.get('image_id')
    comment_text = data.get('comment')
    # user_uid = session['user_uid']  # 从 session 获取当前用户的 UID
    user_uid = '22017530364057'

    # 创建新的评论
    new_review = ImageReview(
        image_id=image_id,
        user_uid=user_uid,
        comment=comment_text
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify({'success': '评论提交成功'}), 201


# 获取图片集
@fulilian_blueprint.route('/get_sets', methods=['GET'])
def get_sets():
    # 从数据库中查询所有图片集信息
    sets = ImageSet.query.all()

    # 创建一个结果列表来存储每个图片集的信息
    result = []
    
    for s in sets:
        # 构造图片存储的路径
        image_path = os.path.join(current_app.root_path, 'static', s.image_url)
        
        # 检查图片是否存在
        if os.path.exists(image_path):
            # 返回存在的图片集信息
            result.append({
                'id': s.id,
                'name': s.name,
                'image_url': f'/get_image/{s.id}',  # 获取原图
                'description': s.description
            })
        else:
            # 记录图片丢失错误
            current_app.logger.error(f"Image file for set {s.id} not found: {image_path}")
    
    if not result:
        # 如果没有找到任何有效的图片集，返回 404 错误
        return jsonify({'status': 'error', 'message': 'No image sets found'}), 404
    
    return jsonify(result)



# 返回具体图片文件的路由
@fulilian_blueprint.route('/get_image/<int:set_id>', methods=['GET'])
def get_image(set_id):
    # 根据图片集的 ID 查找对应的记录
    image_set = ImageSet.query.get_or_404(set_id)
    
    # 图片的路径
    image_path = os.path.join(current_app.root_path, 'static', image_set.image_url)
    image_path = image_path.replace("\\", "/")  # 将反斜杠替换为斜杠
    
    # 检查图片是否存在，并将其返回给前端
    if os.path.exists(image_path):
        return send_from_directory(os.path.dirname(image_path), os.path.basename(image_path), mimetype='image/png')
    
    return jsonify({'status': 'error', 'message': 'Image not found'}), 404



@fulilian_blueprint.route('/get_comments')
def get_comments():
    image_id = request.args.get('image_id')

    comments = ImageReview.query.filter_by(image_id=image_id).all()  # 查询该图片的所有评论
    
    response_data = []
    for review in comments:
        user = User.query.filter_by(uid=review.user_uid).first()
        if user:
            response_data.append({
                'avatar': f'/get_avatar',  # 返回头像
                'username': user.username,
                'comment': review.comment
            })

    return jsonify(response_data)