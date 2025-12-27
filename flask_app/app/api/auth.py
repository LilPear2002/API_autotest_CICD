"""用户认证API"""
from flask import request
from app.api import api_bp
from app import db
from app.models import User
from app.utils import token_required, admin_required, success_response, error_response
import re

@api_bp.route('/auth/register', methods=['POST'])
def register():
    """用户注册"""
    data = request.get_json()
    
    if not data:
        return error_response('请求数据为空')
    
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    
    # 验证
    if not username or not email or not password:
        return error_response('用户名、邮箱和密码不能为空')
    
    if len(username) < 3 or len(username) > 20:
        return error_response('用户名长度应为3-20个字符')
    
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return error_response('邮箱格式不正确')
    
    if len(password) < 6:
        return error_response('密码长度至少6个字符')
    
    if User.query.filter_by(username=username).first():
        return error_response('用户名已存在')
    
    if User.query.filter_by(email=email).first():
        return error_response('邮箱已被注册')
    
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    return success_response(user.to_dict(), '注册成功', 201)

@api_bp.route('/auth/login', methods=['POST'])
def login():
    """用户登录"""
    data = request.get_json()
    
    if not data:
        return error_response('请求数据为空')
    
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    if not username or not password:
        return error_response('用户名和密码不能为空')
    
    user = User.query.filter_by(username=username).first()
    
    if not user or not user.check_password(password):
        return error_response('用户名或密码错误', 401)
    
    if not user.is_active:
        return error_response('用户已被禁用', 403)
    
    token = user.generate_token()
    
    return success_response({
        'token': token,
        'user': user.to_dict()
    }, '登录成功')

@api_bp.route('/auth/logout', methods=['POST'])
@token_required
def logout(current_user):
    """用户登出"""
    # JWT是无状态的，客户端删除token即可
    return success_response(message='登出成功')

@api_bp.route('/auth/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    """获取当前用户信息"""
    return success_response(current_user.to_dict())

@api_bp.route('/auth/profile', methods=['PUT'])
@token_required
def update_profile(current_user):
    """更新用户信息"""
    data = request.get_json()
    
    if not data:
        return error_response('请求数据为空')
    
    email = data.get('email', '').strip()
    
    if email:
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return error_response('邮箱格式不正确')
        if User.query.filter(User.email == email, User.id != current_user.id).first():
            return error_response('邮箱已被使用')
        current_user.email = email
    
    db.session.commit()
    return success_response(current_user.to_dict(), '更新成功')

@api_bp.route('/auth/password', methods=['PUT'])
@token_required
def change_password(current_user):
    """修改密码"""
    data = request.get_json()
    
    old_password = data.get('old_password', '')
    new_password = data.get('new_password', '')
    
    if not old_password or not new_password:
        return error_response('旧密码和新密码不能为空')
    
    if not current_user.check_password(old_password):
        return error_response('旧密码错误')
    
    if len(new_password) < 6:
        return error_response('新密码长度至少6个字符')
    
    current_user.set_password(new_password)
    db.session.commit()
    
    return success_response(message='密码修改成功')

# 管理员接口
@api_bp.route('/admin/users', methods=['GET'])
@admin_required
def get_users(current_user):
    """获取用户列表（管理员）"""
    from app.utils import paginate_query
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    query = User.query.order_by(User.created_at.desc())
    result = paginate_query(query, page, per_page)
    
    return success_response(result)

@api_bp.route('/admin/users/<int:user_id>', methods=['GET'])
@admin_required
def get_user(current_user, user_id):
    """获取用户详情（管理员）"""
    user = User.query.get_or_404(user_id)
    return success_response(user.to_dict())

@api_bp.route('/admin/users/<int:user_id>', methods=['PUT'])
@admin_required
def update_user(current_user, user_id):
    """更新用户（管理员）"""
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    if 'role' in data:
        if data['role'] not in ['admin', 'user']:
            return error_response('无效的角色')
        user.role = data['role']
    
    if 'is_active' in data:
        user.is_active = bool(data['is_active'])
    
    db.session.commit()
    return success_response(user.to_dict(), '更新成功')

@api_bp.route('/admin/users/<int:user_id>', methods=['DELETE'])
@admin_required
def delete_user(current_user, user_id):
    """删除用户（管理员）"""
    if user_id == current_user.id:
        return error_response('不能删除自己')
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    return success_response(message='删除成功')
