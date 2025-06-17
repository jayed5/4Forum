import jwt
from functools import wraps

def generate_auth_token(user_id):
return jwt.encode(
{'user_id': user_id},
app.config['SECRET_KEY'],
algorithm='HS256'
)

def auth_required(f):
@wraps(f)
def decorated(args, kwargs):
token = request.headers.get('Authorization')
if not token:
return jsonify({'message': 'Token is missing'}), 401
try:
data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
current_user = User.query.get(data['user_id'])
except:
return jsonify({'message': 'Invalid token'}), 401
return f(current_user, args, kwargs)
return decorated