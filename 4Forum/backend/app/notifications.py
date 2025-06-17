from flask_socketio import SocketIO, emit
import redis

socketio = SocketIO(app)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

class NotificationSystem:
@staticmethod
def send_notification(user_id, message):
notification = {
'user_id': user_id,
'message': message,
'timestamp': datetime.now().isoformat()
}

redis_client.lpush(f'notifications:{user_id}', json.dumps(notification))

socketio.emit('notification', notification, room=user_id)

@staticmethod
def get_user_notifications(user_id):
notifications = redis_client.lrange(f'notifications:{user_id}', 0, -1)
return [json.loads(n) for n in notifications]