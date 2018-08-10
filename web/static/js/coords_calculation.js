    ///////////////////////
    // COORDS CALCULATION
    ///////////////////////

    // Assume we dont go around the earth more than once...
    const def_dst = 50000.0; // Earth circumference is ~24900miles, ~39900km

    function sum(input){

        if (toString.call(input) !== "[object Array]")
            return false;

        let total =  0;
        for(i=0;i<input.length;i++)
        {
            if(isNaN(input[i]) || input[i] === def_dst){
                continue;
            }
            total += Number(input[i]);
        }
        return total;
    }

    function build_distance_matrix(coords){
        let dsts = [];
        for (i = 0; i < coords.length; i++) {
            let ref_row = [];
            for (j = 0; j < coords.length; j++) {
                if(j <= i){
                    ref_row[j] = def_dst;
                }
                else{
                    ref_row[j] = m2ml(distance(coords[i][0],coords[i][1],coords[j][0],coords[j][1]));
                }
            }
            dsts[i] = ref_row;
        }
        return dsts;
    }