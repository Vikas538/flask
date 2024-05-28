from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, get_user_by_id

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    user = create_user(username, email)
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username, "email": user.email})
    return jsonify({"message": "User not found"}), 404
