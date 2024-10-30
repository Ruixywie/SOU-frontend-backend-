from flask import Blueprint, request, jsonify, current_app, send_from_directory
import os

# 创建蓝图
personal_blueprint = Blueprint('personal_blueprint', __name__)


# 查找头像
@personal_blueprint.route('/get_avatar')
def get_avatar():
    # 设置头像的保存路径
    UPLOAD_FOLDER = os.path.join(current_app.root_path, 'static', 'personal')

    # 在 UPLOAD_FOLDER 目录下查找以 'avatar' 开头的文件
    for file in os.listdir(UPLOAD_FOLDER):
        if file.startswith('avatar'):
            return send_from_directory(UPLOAD_FOLDER, file, mimetype='image/png')
        
    return jsonify({'status': 'error', 'message': 'Avatar image not found'}), 404

# 查找背景图片
@personal_blueprint.route('/get_background')
def get_background():
    # 设置背景的保存路径
    UPLOAD_FOLDER = os.path.join(current_app.root_path, 'static', 'personal')

    # 在 UPLOAD_FOLDER 目录下查找以 'background' 开头的文件
    for file in os.listdir(UPLOAD_FOLDER):
        if file.startswith('background'):
            return send_from_directory(UPLOAD_FOLDER, file)

    return jsonify({'status': 'error', 'message': 'Background image not found'}), 404

# 上传储存头像
@personal_blueprint.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    # 设置上传头像的保存路径
    UPLOAD_FOLDER = os.path.join(current_app.root_path, 'static', 'personal')  # 使用根目录
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)  # 如果目录不存在，则创建

    # 检查请求是否包含文件
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': '头像文件未找到'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': '头像文件为空'}), 400
    
    if file:
        # 获取文件扩展名
        _, file_extension = os.path.splitext(file.filename)
        
        # 统一文件名为 'avatar'，不管上传的文件扩展名是什么
        filename = 'avatar' + file_extension
        
        # 构造完整文件路径
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # 保存新上传的文件
        file.save(file_path)
        
        return jsonify({'status': 'success'}), 200