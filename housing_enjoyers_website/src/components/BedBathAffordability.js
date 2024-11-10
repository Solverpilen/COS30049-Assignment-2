
import { 
    Grid2 as Grid, 
    Container
} from '@mui/material';
import React, { useEffect, useState } from 'react';
import createAffordabilityBarChart from '../services/createAffordabilityBarChart.js';

function BedBathAffordability() {

    const bathroomBarChart = createAffordabilityBarChart(["1", "2", "3", "4"],[1,2,1,1], [1,2,1,1], [1,2,321,123,1], [1,2,3213,12]);
    const anotherchart =  createAffordabilityBarChart(["1", "2", "3", "4"],[1,2,1,1], [1,2,1,1], [1,2,321,123,1], [1,2,3213,12]);


    return (
    <div>

        <Container maxWidth="lg" style={{ marginTop: '100px'}}>
            <Grid container spacing={2} alignItems="center" justifyContent="center" display="flex" flexDirection="row" >
                    <div>
                        
                        {bathroomBarChart}
                        <h3> Number of Bathrooms</h3>
                    </div>

                    <div>{anotherchart}</div>

            </Grid>
        </Container>

    </div>

    );
}

export default BedBathAffordability;


