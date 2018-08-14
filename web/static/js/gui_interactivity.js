    ///////////////////////
    //  UI/MAP INTERACTIVITY
    ///////////////////////

    let coords = [];  // Points we set on the map; array
    let draw; // global so we can remove it later.
    let type_selected = "Point"; //Possible options are: Point, LineString,Polygon

    let container = document.getElementById('popup');
    let content = document.getElementById('popup-content');
    let closer = document.getElementById('popup-closer');


    function display_coords() {
        let coords_as_html = "<tr><th>Index</th><th>Lat</th><th>Lon</th><tr>";
        $.each(coords, function( index, value ) {
          // console.log('>>>', index , value[0], value[1] );
          coords_as_html += "<tr><td>"+index+"</td><td>"+to3dps(value[0]) +"</td><td>"+to3dps(value[1])+"</td><tr>";
        });
        return '<table>'+coords_as_html+'</table>';
    }

    function display_coords_distances(){
        let html_result = "<tr><th>Src Id</th><th>Dst Id</th><th>Distance (miles)</th><tr>";
        for (i = 0; i < coords.length-1; i++) {
            for (j = i+1; j < coords.length; j++) {
                d = distance(coords[i][0],coords[i][1],coords[j][0],coords[j][1]);
                html_result+=
                    "<tr><td>"+i+"</td><td>"+j+"</td><td>"+
                        to3dps(m2ml(d))+"</td></tr>";
            }
        }
        return '<table>'+html_result+'</table>';
    }

    function get_best_distance(dm) {
//        let paths = [];
//        for(kruskal_idx = 0; kruskal_idx < dm.length; kruskal_idx++){
//            let row_idxs = find_path_at_node(dm, kruskal_idx);
//            paths[kruskal_idx] = row_idxs;
//
//            let total_dist = calc_path_distance(dm, paths[kruskal_idx]);
//            console.log("Total distance at node idx "+kruskal_idx+" = "+to3dps(total_dist) + " miles");
//        }

//        let data = {x: [[[2,1.0],[2.0,4]],[[2,3.0],[4,5]]]};
        let data = {'dm':dm}

        const url = "http://127.0.0.1:5000/routes/check/status";

//        $.post( url, data, function( result ) {
//          $( "#info" ).html( result );
//        });


        $.ajax({
          type: "POST",
          url: url,
          data: JSON.stringify(data),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          error: function() {
            alert("Error");
          },
          success: function(data_back) {
            console.log(data_back);
            alert("OK");
          }
        });
    }


    let raster = new ol.layer.Tile({
        source: new ol.source.Stamen({
            layer: 'terrain'
        })
    });

    let source = new ol.source.Vector({ wrapX: false });
    let vector = new ol.layer.Vector({
        source: source
    });

    let mousePositionControl = new ol.control.MousePosition({
        coordinateFormat: ol.coordinate.createStringXY(4),
        projection: 'EPSG:4326',
        undefinedHTML: '&nbsp;'
    });

    let overlay = new ol.Overlay({
        element: container,
        autoPan: true,
        autoPanAnimation: {
            duration: 250
        }
    });

    closer.onclick = function() {
        overlay.setPosition(undefined);
        closer.blur();
        return false;
    };

    let map = new ol.Map({
        controls: ol.control.defaults({
            attributionOptions: {
                collapsible: false
            }
        }).extend([mousePositionControl]),
        layers: [
            new ol.layer.Tile({
                source: new ol.source.Stamen({
                    layer: 'terrain'
                })
            }),
            new ol.layer.Tile({
                source: new ol.source.Stamen({
                    layer: 'terrain-labels'
                })
            }),

            raster,
            vector
        ],
        overlays: [overlay],
        target: 'map',
        view: new ol.View({
            // Center map on this location...  West of DC
            center: ol.proj.transform([-77.5, 39], 'EPSG:4326', 'EPSG:3857'),
            zoom: 10
        })
    });


    map.on('singleclick', function(evt) {
        let coordinate = evt.coordinate;
        let hdms = ol.coordinate.toStringHDMS(ol.proj.transform(
            coordinate, 'EPSG:3857', 'EPSG:4326'));

        overlay.setPosition(coordinate);

        let lonlat = ol.proj.transform(evt.coordinate, 'EPSG:3857', 'EPSG:4326');
        let lon = lonlat[0];
        let lat = lonlat[1];
        coords.push([lat, lon]);
        console.log("lat,lon=", lat, lon);

        content.innerHTML = '<form><table>'+
            '<tr><td>Lat:</td><td>' + to3dps(lat) + '</td></tr>'+
            '<tr><td>Lon:</td><td>' + to3dps(lon) + '</td></tr>'+
            '</table></form>';
    });


    map.on("dblclick", function(evt) {
        let pixel = evt.pixel;

        let output = display_coords() + display_coords_distances();
        $("#info").html(output);

        // let features = [];
        // map.forEachFeatureAtPixel(pixel, function(feature) {
        //     features.push(feature);
        // });
        // if (features.length > 0) {
        //     let coordinate = features[0].getGeometry().getFirstCoordinate();
        //     console.log(coordinate);
        // } else {
        //     document.getElementById("info").innerHTML = "&nbsp;";
        // }
        dm = build_distance_matrix(coords);


        // let kruskal_idx = 3;
        get_best_distance(dm);

    });


    function addInteraction() {
        let value = type_selected; //typeSelect.value;
        if (value !== 'None') {
            draw = new ol.interaction.Draw({
                source: source,
                type: type_selected
            });
            map.addInteraction(draw);
        }
    }
    addInteraction();