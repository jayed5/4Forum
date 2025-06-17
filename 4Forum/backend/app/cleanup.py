from datetime import datetime, timedelta

def cleanup_old_data():
"""Usuwa stare dane z systemu"""

expired_subs = Subscription.query.filter(
Subscription.expires_at < datetime.utcnow()
).all()

for sub in expired_subs:
sub.user.is_premium = False
db.session.delete(sub)

inactive_users = User.query.filter(
User.last_login < datetime.utcnow() -