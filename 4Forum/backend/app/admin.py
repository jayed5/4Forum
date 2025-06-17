from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class AdminView(BaseView):
@expose('/')
def index(self):
if not current_user.is_admin:
return redirect(url_for('index'))
return self.render('admin/index.html')

@expose('/subscriptions')
def subscriptions(self):
pending_subs = Subscription.query.filter_by(status='pending').all()
return self.render('admin/subscriptions.html', subs=pending_subs)

@expose('/approve/<int:sub_id>')
def approve_subscription(self, sub_id):
sub = Subscription.query.get_or_404(sub_id)
sub.status = 'approved'
sub.user.is_premium = True
db.session.commit()
return redirect(url_for('.subscriptions'))