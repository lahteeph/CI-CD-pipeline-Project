# The code starts by importing the Flask class and the render_template function from the Flask library. Flask is used for developing web applications using python

from flask import Flask, render_template

# app = Flask(__name__) creates a new Flask web application instance, passing the current module name (__name__) as the app name.

app = Flask(__name__)

# @app.route('/') defines a route for the root URL (/) of the application. The home() function is associated with this route.

# return render_template('index.html') returns the rendered HTML content of the index.html template file, which is expected to be located in a templates directory.

@app.route('/')
def home():
    return render_template('index.html')

# if __name__ == '__main__': checks if the script is being run directly (not being imported as a module). If so, app.run(host='0.0.0.0', port=8000) starts the Flask development server, listening on all available network interfaces (0.0.0.0) on port 8000.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

