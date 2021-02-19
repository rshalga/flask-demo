from flask import Flask

app = Flask(__name__)

nameMap = {
    "Rohit" : "Shalgar"
}
@app.route('/')
def index():
    return '<h1>Hello world</h1>'

@app.route('/hello/<Name>')
def printHello(Name):
    for name1, lastName in nameMap.items():
        if name1== Name:
            return "Hi {} {}".format(name1,lastName)

@app.route("/CreateUser/<string:name>/<string:lastName>",
methods = ['POST'])
def CreateUser():
    nameMap["name"] = lastName
    return "User has been created"

        
if __name__ == "__main__":
    app.run()