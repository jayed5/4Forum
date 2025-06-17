import bcrypt
from cryptography.fernet import Fernet
import secrets

class Security:
def init(self):
self.key = Fernet.generate_key()
self.cipher_suite = Fernet(self.key)

def hash_password(self, password):
salt = bcrypt.gensalt()
return bcrypt.hashpw(password.encode(), salt)

def verify_password(self, password, hashed):
return bcrypt.checkpw(password.encode(), hashed)

def generate_admin_key(self):
return secrets.token_urlsafe(32)

def encrypt_data(self, data):
return self.cipher_suite.encrypt(data.encode())

def decrypt_data(self, encrypted_data):
return self.cipher_suite.decrypt(encrypted_data).decode()

Implementacja rate limitingu
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
app,
key_func=get_remote_address,
default_limits=["200 per day", "50 per hour"]
)

from flask_talisman import Talisman
from flask_seasurf import SeaSurf
import re

Konfiguracja zabezpieczeń
talisman = Talisman(app,
content_security_policy={
'default-src': "'self'",
'img-src': '',
'script-src': "'self'",
}
)

csrf = SeaSurf(app)

def validate_input(text):
"""Walidacja wprowadzanych danych"""
if not text:
return False
Sprawdzanie niebezpiecznych znaków
pattern = re.compile(r'^[a-zA-Z0-9\s\-_\.]+$')
return bool(pattern.match(text))

Rate limiting dla API
@limiter.limit("5 per minute")
@app.route("/api/login", methods=["POST"])
def login():
pass

Blokowanie podejrzanych IP
def check_ip_blacklist(ip):
with open('blacklist.txt', 'r') as f:
blacklist = f.read().splitlines()
return ip in blacklist