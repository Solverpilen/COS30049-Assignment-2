import ResponsiveAppBar from '../components/navbar/navbar.js';
import createChart from '../components/charts/createChart.js';
import LineChart from '../components/charts/LineChart.js'; 
import { Grid, Container, Paper } from '@mui/material';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import axios from 'axios'
import React, { useEffect, useState } from 'react';



function Affordability() {

    const [chartData, setChartData] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:8000/price_prediction/default_pie_chart')  // Example API call to FastAPI
            .then(response => {
                console.log('Fetched Data:', response.data); // Log data for debugging
                setChartData(response.data); // Update state with fetched data
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []); 

    return (
    <div className="App">
        <ResponsiveAppBar/>

  
    <h1>React Line Chart with Chart.js</h1>
    <Container maxWidth="lg" style={{ height: '100vh', display: 'flex' }}>
    {/* Grid Container to center the charts */}
    <Grid container
      spacing={2}
      justifyContent="center"
      alignItems="center"
      item xs={6}>

        <p> {chartData} </p>

    </Grid>

    <Grid container
    spacing={6}
    justifyContent="center"
   // alignItems="center"
    item xs={6}>

    <Box>
    <p> The median weekly income of Australia is $1,500 in 2023. If that person works 50 weeks of the year
        then that comes to a total of $75,000 per year. Assuming monthly expenses of 1,000 per month, 
        this particular person can borrow a maximum of $394,000 to pay for their property. 
        This is what the pie chart to the left shows the affordability of such properties from 2017 to 2018 according 
        these statistics.
    </p>
    </Box>


    </Grid>

   
    </Container>
    </div>




    );

}

export default Affordability;