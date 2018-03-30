from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <h1 style="background-color:powderblue;"><center>Gaspare's Decode Box</center></h1>
        <form action="/encrypt" method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value={0}>
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{1}</textarea>
            <br>
            <input type="submit" value="Code/Decode">
        </form>
    </body>
</html>
"""

@app.route("/")
def home():
    return form.format(0,'[Enter text to be coded here]')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    text=str(request.form['text'])
    rot=int(request.form['rot'])
    content=rotate_string(text, rot)
    
    return form.format(str(26-rot), content)


if __name__=='__main__':
    app.run()