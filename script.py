from flask import Flask, render_template
import plotly
import plotly.graph_objects as go
import json

app = Flask(__name__)

# Sample inventory data...
inventory_data = [
    {
        'hostname': 'server1',
        'ip': '192.168.0.10',
        'os': 'Linux',
        'memory': '8GB',
        'storage': '500GB'
    },
    # Additional inventory data...
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def view_inventory():
    return render_template('inventory.html', inventory=inventory_data)

@app.route('/dashboard')
def dashboard():
    # Generate data for the inventory pie chart
    os_count = {
        'Linux': 0,
        'Windows': 0
    }
    for item in inventory_data:
        os_count[item['os']] += 1

    os_labels = list(os_count.keys())
    os_values = list(os_count.values())

    # Create the inventory pie chart
    inventory_pie = go.Figure(data=go.Pie(labels=os_labels, values=os_values))

    # Convert the Figure object to a JSON string
    inventory_pie_json = json.dumps(inventory_pie, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the dashboard template with the JSON data
    return render_template('dashboard.html', inventory_pie=inventory_pie_json)

if __name__ == '__main__':
    app.run(debug=True)
