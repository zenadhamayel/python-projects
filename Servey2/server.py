from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name=request.form["first_name"]
    last_name=request.form["last_name"]
    
    strawberry=request.form["strawberry"]
    raspberry=request.form["raspberry"]
    apple=request.form["apple"]
    
    count= int(strawberry)+int(raspberry)+int(apple)
    
    print(request.form)
    return render_template("checkout.html", strawberry=strawberry,raspberry=raspberry , apple=apple,  count=count ,first_name=first_name,last_name=last_name)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True) 