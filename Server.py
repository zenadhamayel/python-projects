from flask import Flask

app=Flask(__name__)

#localhost:5000/ - have it say "Hello World!
@app.route('/')
def index():
    return"Helo world"

@app.route('/dojo')
def dogo():
    return"Dojo"
#localhost:5000/say/flask - have it say "Hi Flask!"
@app.route('/say/<word>')
def input(word):
    return f'Helo {word}'
#localhost:5000/repeat/35/hello - have it say "hello" 35 times
@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    return f'{word} ' *int(num)    

if __name__=="__main__":
    app.run(debug=True)
