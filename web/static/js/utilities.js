    //////////////
    // UTILITIES
    //////////////

    function distance(lat1, lon1, lat2, lon2) {

        // Convert degrees to radians
        let latRad1 = lat1 * Math.PI / 180.0;
        let lonRad1 = lon1 * Math.PI / 180.0;

        let latRad2 = lat2 * Math.PI / 180.0;
        let lonRad2 = lon2 * Math.PI / 180.0;

        // radius of earth in metres
        let r = 6378100;

        // P
        let rho1 = r * Math.cos(latRad1);
        let z1 = r * Math.sin(latRad1);
        let x1 = rho1 * Math.cos(lonRad1);
        let y1 = rho1 * Math.sin(lonRad1);

        // Q
        let rho2 = r * Math.cos(latRad2);
        let z2 = r * Math.sin(latRad2);
        let x2 = rho2 * Math.cos(lonRad2);
        let y2 = rho2 * Math.sin(lonRad2);

        // Dot product
        let dot = (x1 * x2 + y1 * y2 + z1 * z2);
        let cos_theta = dot / (r * r);

        let theta = Math.acos(cos_theta);

        // Distance in Metres
        return r * theta;
    }

    function to3dps(refVal) { return String(refVal.toFixed(3)); }

    function m2ml(m_val) { return Number(m_val) * 0.000621371; }
