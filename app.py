# app.py
from flask import Flask, render_template
from routes.api import api_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use the DATABASE_URL environment variable defined in docker-compose.yml
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/flaskdb'
db = SQLAlchemy(app)

# Register the blueprints
app.register_blueprint(api_bp)

# Default route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # You can replace this with your preferred response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    
