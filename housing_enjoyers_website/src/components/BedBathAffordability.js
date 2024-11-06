
import { 
    Grid2 as Grid, 
    Container, TextField, Box, Button, Typography 
} from '@mui/material';
import axios from 'axios'
import React, { useEffect, useState } from 'react';
import createAffordabilityBarChart from '../services/createAffordabilityBarChart.js';

function BedBathAffordability() {

    const bathroomBarChart = createAffordabilityBarChart(["1", "2", "3", "4"],[1,2,1,1], [1,2,1,1], [1,2,321,123,1], [1,2,3213,12]);
    const anotherchart =  createAffordabilityBarChart(["1", "2", "3", "4"],[1,2,1,1], [1,2,1,1], [1,2,321,123,1], [1,2,3213,12]);


    return (
    <div>

        <Container maxWidth="lg" style={{ marginTop: '100px'}}>
            <Grid container spacing={2} alignItems="center" justifyContent="center">
                <Grid item xs={12} md={6} style={{ display: 'flex', justifyContent: 'center' }}>
                    <div>{bathroomBarChart}</div>
                </Grid>

                <Grid item xs={12} md={6} style={{ display: 'flex', justifyContent: 'center' }}>
                    <div>{anotherchart}</div>
                </Grid>
            </Grid>
        </Container>

    </div>

    );
}

export default BedBathAffordability;


