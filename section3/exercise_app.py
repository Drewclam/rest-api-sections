from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'THe first store',
        'items': [
            {
                'name': 'Best item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')  # Home page of the site
def home():
    return 'Hello, world!'


@app.route('/store')
def getStores():
    pass


@app.route('/store/<string:name>')
def getStore():
    pass


@app.route('/store', methods=['POST'])
def createStore():
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def createItem(name):
    pass


@app.route('/store/<string:name>/item')
def getItems():
    pass


app.run(port=5000)
