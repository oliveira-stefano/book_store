
from app.api.V1.hello_world import HelloWorld

def load_routes_v1(api):
    api.add_resource(HelloWorld, 'hello')