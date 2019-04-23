from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'Best item',
                'price': 15.99
            }
        ]
    }
]


def createErrorMessage(message):
    return {'message': message}


@app.route('/')  # Home page of the site
def home():
    return render_template('exercise_index.html')


@app.route('/store')
def getStores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>')
def getStore(name):
    store = list(filter(lambda x: x['name'] == name, stores))
    if len(store) > 0:
        return jsonify({'store': store})
    else:
        return jsonify(createErrorMessage('No store found!'))


@app.route('/store', methods=['POST'])
def createStore():
    requestData = request.get_json()
    newStore = {
        'name': requestData['name'],
        'items': []
    }
    stores.append(newStore)
    return jsonify(newStore)


@app.route('/store/<string:name>/item', methods=['POST'])
def createItem(name):
    requestData = request.get_json()
    store = list(filter(lambda x: x['name'] == name, stores))
    item = {
        'name': requestData['name'],
        'price': requestData['price']
    }
    if len(store) > 0:
        store[0]['items'].append(item)
        return jsonify(item)
    else:
        return jsonify(createErrorMessage('Error: Item could not be created.'))


@app.route('/store/<string:name>/item')
def getItems(name):
    store = list(filter(lambda store: store['name'] == name, stores))
    if len(store) > 0:
        items = store[0]['items']
        return jsonify({'items': items})
    else:
        return jsonify(createErrorMessage('Error: Could not retrieve items for that store'))


app.run(port=5000)
