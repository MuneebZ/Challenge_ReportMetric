from flask import Flask

def configure_routes(app):

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'
    
    response = client.get(url)
    assert response.get_data() == b'Hello, World!'
    assert response.status_code == 200
    # assert response.content_type == 
    
    