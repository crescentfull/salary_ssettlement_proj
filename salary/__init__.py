from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def start():
        return "start proj"
    return app

if __name__=="__main__":
    create_app().debug = True
    create_app().run(host="0.0.0.0", port="8080")