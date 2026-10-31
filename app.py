from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///recoverza.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class DebtAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    debtor_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    outstanding_balance = db.Column(db.Float, nullable=False)
    days_overdue = db.Column(db.Integer, nullable=False)
    debicheck_status = db.Column(db.String(50), default='PENDING')
    section_11j_eligible = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "RecoverZA Backend", "version": "1.0.0"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
