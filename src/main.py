import flask 

app = Flask()

@app.route('/')
def hello_world():
   return 'Hello World’


app.run(port=8080)