from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class User:
def init(self):
self.id = str(uuid.uuid4())
self.key = self.generate_key()
self.password_hash = None
self.is_premium = False
self.servers = []

@staticmethod
def generate_key():
return str(uuid.uuid4())[:12]

class Server:
def init(self):
self.id = str(uuid.uuid4())
self.name = None
self.members = []
self.threads = []
self.max_file_size = 5 1024 1024 5MB default

class Subscription(db.Model):
id = db.Column(db.Integer, primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
payment_proof = db.Column(db.String(255))
status = db.Column(db.String(20), default='pending')
created_at = db.Column(db.DateTime, default=datetime.utcnow)
expires_at = db.Column(db.DateTime)

def init(self, user_id, payment_proof):
self.user_id = user_id
self.payment_proof = payment_proof
self.expires_at = datetime.utcnow() + timedelta(days=30)
