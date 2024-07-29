# py -m flask --app tapp run
from get_routes import get_routes
from post_routes import post_routes
from put_routes import put_routes
from delete_routes import delete_routes
from flask import Flask


app = Flask(__name__)   

#calling the API
app.register_blueprint(get_routes)
app.register_blueprint(post_routes)
app.register_blueprint(put_routes)
app.register_blueprint(delete)

if __name__ == '__main__':
  #app.run(debug=true)
  app.run(port=5000,debug=True)