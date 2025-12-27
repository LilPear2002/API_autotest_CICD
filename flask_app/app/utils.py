"""工具函数"""
from functools import wraps
from flask import request, jsonify, current_app
from app.models import User
import os
import uuid

def token_required(f):
    """Token认证装饰器"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({'code': 401, 'message': '缺少认证Token'}), 401
        
        user = User.verify_token(token)
        if not user:
            return jsonify({'code': 401, 'message': 'Token无效或已过期'}), 401
        
        if not user.is_active:
            return jsonify({'code': 403, 'message': '用户已被禁用'}), 403
        
        return f(user, *args, **kwargs)
    return decorated

def admin_required(f):
    """管理员权限装饰器"""
    @wraps(f)
    @token_required
    def decorated(user, *args, **kwargs):
        if user.role != 'admin':
            return jsonify({'code': 403, 'message': '需要管理员权限'}), 403
        return f(user, *args, **kwargs)
    return decorated

def allowed_file(filename):
    """检查文件类型是否允许"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def generate_filename(original_filename):
    """生成唯一文件名"""
    ext = original_filename.rsplit('.', 1)[1].lower() if '.' in original_filename else ''
    return f"{uuid.uuid4().hex}.{ext}" if ext else uuid.uuid4().hex

def paginate_query(query, page, per_page):
    """分页查询"""
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    return {
        'items': [item.to_dict() for item in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page,
        'per_page': per_page,
        'has_next': pagination.has_next,
        'has_prev': pagination.has_prev
    }

def success_response(data=None, message='操作成功', code=200):
    """成功响应"""
    return jsonify({'code': code, 'message': message, 'data': data}), code

def error_response(message='操作失败', code=400):
    """错误响应"""
    return jsonify({'code': code, 'message': message}), code
