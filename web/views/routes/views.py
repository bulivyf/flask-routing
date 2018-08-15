import simplekml
from flask import Response, json, request

from web.views.routes import routes

import json

from web.views.routes.nearestneighbor import NearestNeighbor

print("Loading routes.views")


@routes.route('/check/<id>', methods=['GET', 'POST'])
def get_distance(id):
    if request.method == 'POST':
        print('POST')
        data = request.get_json()
        x = data['dm']
        print(x)

    gui_data = json.loads(request.data)
    dst, res_path = NearestNeighbor().find_min_distance(gui_data['dm'])
    coords = gui_data['points']

    kml = simplekml.Kml()
    for src, dst in enumerate(res_path):
        linestring = kml.newlinestring(name=str(src))
        linestring.coords = [(coords[src][1], coords[src][0]), (coords[dst][1], coords[dst][0])]
        # kml.newpoint(name=str(src), coords=[(dst, src)])

    ref = kml.save('result.kml')

    result = {'idxs': res_path.tolist()}
    # if id == 'status':
    #     json_out = {'name': 'ok'}  # get_group_options_as_name_dict(db.session)
    print(result)
    http_resp = _create_http_response_for_json(result)
    return http_resp
    # return redirect(url_for('main.index'))


def _create_http_response_for_json(json_txt):
    resp = Response(json.dumps(json_txt), mimetype='application/json')
    resp.status_code = 201
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = '*'
    resp.headers['Access-Control-Allow-Domain'] = '*'
    resp.headers['Access-Control-Allow-Credentials'] = True
    return resp
