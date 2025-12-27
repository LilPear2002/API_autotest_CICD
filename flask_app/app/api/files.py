"""文件管理API"""
from flask import request, send_from_directory, current_app
from app.api import api_bp
from app import db
from app.models_file import File
from app.utils import token_required, success_response, error_response, allowed_file, generate_filename, paginate_query
import os

@api_bp.route('/files', methods=['GET'])
@token_required
def get_files(current_user):
    """获取文件列表"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    file_type = request.args.get('file_type')
    
    query = File.query.filter_by(user_id=current_user.id)
    
    if file_type:
        query = query.filter_by(file_type=file_type)
    
    query = query.order_by(File.upload_at.desc())
    result = paginate_query(query, page, per_page)
    return success_response(result)

@api_bp.route('/files/upload', methods=['POST'])
@token_required
def upload_file(current_user):
    """上传文件"""
    if 'file' not in request.files:
        return error_response('没有文件')
    
    file = request.files['file']
    
    if file.filename == '':
        return error_response('没有选择文件')
    
    if not allowed_file(file.filename):
        return error_response('不支持的文件类型')
    
    original_filename = file.filename
    filename = generate_filename(original_filename)
    file_type = original_filename.rsplit('.', 1)[1].lower() if '.' in original_filename else ''
    
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    file_size = os.path.getsize(file_path)
    
    file_record = File(
        filename=filename,
        original_filename=original_filename,
        file_type=file_type,
        file_size=file_size,
        user_id=current_user.id
    )
    db.session.add(file_record)
    db.session.commit()
    
    return success_response(file_record.to_dict(), '上传成功', 201)

@api_bp.route('/files/<int:file_id>', methods=['GET'])
@token_required
def get_file_info(current_user, file_id):
    """获取文件信息"""
    file_record = File.query.filter_by(id=file_id, user_id=current_user.id).first_or_404()
    return success_response(file_record.to_dict())

@api_bp.route('/files/<int:file_id>/download', methods=['GET'])
@token_required
def download_file(current_user, file_id):
    """下载文件"""
    file_record = File.query.filter_by(id=file_id, user_id=current_user.id).first_or_404()
    return send_from_directory(
        current_app.config['UPLOAD_FOLDER'],
        file_record.filename,
        as_attachment=True,
        download_name=file_record.original_filename
    )

@api_bp.route('/files/<int:file_id>', methods=['DELETE'])
@token_required
def delete_file(current_user, file_id):
    """删除文件"""
    file_record = File.query.filter_by(id=file_id, user_id=current_user.id).first_or_404()
    
    # 删除物理文件
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file_record.filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    
    db.session.delete(file_record)
    db.session.commit()
    
    return success_response(message='删除成功')
