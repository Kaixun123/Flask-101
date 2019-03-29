# Flask installation: http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/

# This is the main page to run the webpage
from HelloWold import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
