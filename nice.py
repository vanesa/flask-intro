from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet" method="POST">
                <label>What's your name? <input type="text" name="person"></label>
                <br>
                <label>Which word best describes you? (You so humble) 
                <select name="compliment">
                    <option value="fabulous">Fabulous</option>
                    <option value="cool">So So Cool</option>
                    <option value="neato">Neato</option>
                    <option value="toll">Super Toll</option>
                    <option value="geil">Super Geil</option>
                </label>
                <br><br>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet',methods=["POST"])
def greet_person():
    player = request.form.get("person")
    selected_compliment = request.form.get("compliment")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
        <a href="http://localhost:5000/hello">Click here to go back!</a>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, selected_compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=False)
