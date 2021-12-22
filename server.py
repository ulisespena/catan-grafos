from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from algorithm import calc_best_positions

app = Flask(__name__)
app.static_folder = 'static'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc-best-positions', methods=['POST'])
@cross_origin()
def calc():
    data = request.get_json()
    best_positions, edges = calc_best_positions(data['prizes'])
    best_positions = [str(pos) for pos in best_positions]
    edges = [str(edge) for edge in edges]
    json_str_positions = '[' + ','.join(best_positions) + ']'
    json_str_edges = '[' + ','.join(edges) + ']'
    return "{ \"positions\": %s, \"edges\": %s }" % (json_str_positions, json_str_edges)