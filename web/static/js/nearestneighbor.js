    /////////////////////
    // NEAREST NEIGHBOR
    /////////////////////

    function cloneArray( arr ) {
        let i, copy;

        if( Array.isArray( arr ) ) {
            copy = arr.slice( 0 );
            for( i = 0; i < copy.length; i++ ) {
                copy[ i ] = cloneArray( copy[ i ] );
            }
            return copy;
        } else if( typeof arr === 'object' ) {
            throw 'Cannot clone array containing an object!';
        } else {
            return arr;
        }
    }

    function deleteCol(arr, col_idx){
        for(var i = 0 ; i < arr.length ; i++)
        {
           arr[i].splice(col_idx, 1);
        }
        return arr;
    }

    function deleteRow(arr, row_idxs) {
        arr.splice(row_idxs, 1);
        return arr;
    }

    function splice_at_matrix_idx(ref_arr, idx){
        arr = cloneArray(ref_arr);
        return deleteRow(deleteCol(arr, idx), idx);
    }

    /*function get_col_as_array(arr, col_idx){
        let col_arr = [];
        for(i=0; i<arr.length; i++){
            col_arr.push(arr[i][col_idx]);
        }
        return col_arr;
    }*/

    function find_row_idxs(arr, col_idx, ref_val){
        let row_idxs = -1;
        if (ref_val != def_dst){
            for(i=0; i<arr.length; i++){
                if(arr[i][col_idx] == ref_val) {
                    row_idxs = i;
                    break;
                }
            }
        }
        return row_idxs;
    }

    function find_path_at_node(dm, kruskal_idx){
        let ref_dsts = splice_at_matrix_idx(dm, kruskal_idx);

        let col_min_vals = math.min(ref_dsts, 0);

        // min lat, lon idx finder...
        let row_idxs = [];
        let min_idx = -1;
        for(dm_col=0; dm_col < dm.length; dm_col++){
            if(dm_col != kruskal_idx){
                min_idx++;
                row_idxs[dm_col] = find_row_idxs(dm, dm_col, col_min_vals[min_idx]);
            }else{
                console.log("In kruskal column:"+kruskal_idx);
                row_idxs[dm_col] = dm[kruskal_idx].indexOf(math.min(dm[kruskal_idx])); //-2;
            }
        }
        console.log(row_idxs);

        // for four locs on the map, kruskal = 2; row_idxs = [-1, 0, , 1] reads
        // '-1' is route not found,
        // '0', From loc idx '0' to col 1,
        // '_', kruskal row is 2
        // '1', From loc idx '1', to col 3
        /// from kruskal pos 3 to krusal 2

        return row_idxs;
    }

    function calc_path_distance(dm, row_idxs){
        let total_dist = 0.0;
        for(i=0; i<row_idxs.length; i++){
            let dist = 0.0;
            if(row_idxs[i] >= 0){
                if(row_idxs[i] > i)
                    dist = dm[i][row_idxs[i]];
                else
                    dist = dm[row_idxs[i]][i];
                console.log("From idx="+row_idxs[i]+" to idx="+i+", the distance is: "+dist);
                total_dist += dist;
            }
        }
        return total_dist;

    }
