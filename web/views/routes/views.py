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

    base_distances = json.loads(request.data)
    NearestNeighbor().find_min_distance(base_distances['dm'])

    json_out = {'name': [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]}
    # if id == 'status':
    #     json_out = {'name': 'ok'}  # get_group_options_as_name_dict(db.session)
    print(json_out)
    http_resp = _create_http_response(json_out)
    return http_resp
    # return redirect(url_for('main.index'))


def _create_http_response(json_txt):
    resp = Response(json.dumps(json_txt), mimetype='application/json')
    resp.status_code = 201
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = '*'
    resp.headers['Access-Control-Allow-Domain'] = '*'
    resp.headers['Access-Control-Allow-Credentials'] = True
    return resp
