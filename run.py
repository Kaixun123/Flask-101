# This a practical of the flask 
# Flask installation: http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/
from HelloWold import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
