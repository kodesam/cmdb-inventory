from flask import Flask, render_template

app = Flask(__name__)

# Sample inventory data
inventory_data = [
    {
        'hostname': 'server1',
        'ip': '192.168.0.10',
        'os': 'Linux',
        'memory': '8GB',
        'storage': '500GB'
    },
    {
        'hostname': 'server2',
        'ip': '192.168.0.20',
        'os': 'Windows',
        'memory': '16GB',
        'storage': '1TB'
    },
    {
        'hostname': 'server3',
        'ip': '192.168.0.30',
        'os': 'Linux',
        'memory': '4GB',
        'storage': '250GB'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def view_inventory():
    return render_template('inventory.html', inventory=inventory_data)

if __name__ == '__main__':
    app.run(debug=True)
