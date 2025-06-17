@app.route('/api/servers', methods=['GET'])
@auth_required
def get_servers():
user = get_current_user()
if not user.is_premium and len(user.servers) >= 100:
return jsonify({'error': 'Limit serwerów osiągnięty'}), 403

return jsonify({
'servers': [server.to_dict() for server in user.servers]
})

@app.route('/api/servers', methods=['POST'])
@auth_required
def create_server():
data = request.get_json()
user = get_current_user()

if not user.is_premium and len(user.servers) >= 100:
return jsonify({'error': 'Limit serwerów osiągnięty'}), 403

server = Server(
name=data['name'],
owner_id=user.id
)
db.session.add(server)
db.session.commit()

return jsonify(server.to_dict()), 201

@app.route('/api/subscription', methods=['POST'])
@auth_required
def create_subscription():
if 'payment_proof' not in request.files:
return jsonify({'error': 'Brak dowodu wpłaty'}), 400

file = request.files['payment_proof']
if file.filename == '':
return jsonify({'error': 'Nie wybrano pliku'}), 400

filename = secure_filename(file.filename)
file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
file.save(file_path)

subscription = Subscription(
user_id=current_user.id,
payment_proof=filename
)
db.session.add(subscription)
db.session.commit()

return jsonify({'message': 'Subskrypcja oczekuje na zatwierdzenie'}), 200