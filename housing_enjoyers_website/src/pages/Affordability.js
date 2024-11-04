import ResponsiveAppBar from '../components/navbar/navbar.js';
import createPieChart from '../services/createPieChart.js';
import { Grid, Container, Paper } from '@mui/material';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import axios from 'axios'
import React, { useEffect, useState } from 'react';
import Button from '@mui/material/Button';
import updatePieChart from '../services/updatePieChart.js';

import Typography from '@mui/material/Typography';



function Affordability() {

    const [chartData, setChartData] = useState({});
    const [borrow, setBorrow] = useState('');
    const [newData, setNewData] = useState('');

    useEffect(() => {
        axios.get('http://localhost:8000/price_prediction/default_pie_chart')  // Example API call to FastAPI
            .then(response => {
                console.log('Fetched Data:', response.data); // Log data for debugging
                setChartData(response.data.ratings); // Update state with fetched data
            })
            .catch(error => console.error('Error fetching data:', error));
            
    }, []); 

    function updatePieChart() {
        axios.post('http://localhost:8000/price_prediction/{borrow}')
        .then(response => {
            console.log('Fetched Data:', response.data);
            setNewData(response.data.ratings);
        })
    };


    const defaultPieChart = createPieChart("Default Pie Chart", ["High", "Medium", "Low", "Very Low"], 
        [chartData.high, chartData.medium, chartData.low, chartData["very low"]], ["blue", "green", "orange", "#FF6666"], 
        ["blue", "green", "orange", "#FF6666"]);
    
    
    


    return (
    <div className="App">
        <ResponsiveAppBar/>

  
    <h1>React Line Chart with Chart.js</h1>
    <Container maxWidth="lg" style={{ marginTop: '200px'}} xs={{ display: 'flex' }}>
    {/* Grid Container to center the charts */}
        <Grid container
        spacing={4}
        justifyContent="center">
        
        <Grid container item xs={12} spacing={10} justifyContent="center">

            <Grid xs = {12} md = {6} xs={{ display: "flex", justifyContent : "center"}}>
            <div>
                {defaultPieChart}
            </div>
            </Grid>
            <Grid  container spacing={6}
            item xs={12} md={6} xs={{display: "flex"}}
            >

                <Box xs={{display: "flex", flexDirection: 'column'} }
                >
                <Typography className='text_box' align='justify' xs={{border: '2px solid #1976d2' , borderRadius: '16px'}}>The median weekly income of Australia is $1,500 in 2023. If that person works 50 weeks of the year
                    then that comes to a total of $75,000 per year. Assuming monthly expenses of 1,000 per month, 
                    this particular person can borrow a maximum of $394,000 to pay for their property. 
                    This is what the pie chart to the left shows the affordability of such properties from 2017 to 2018 according 
                    these statistics.
                </Typography>

                <Typography align='center' style={{ paddingTop: '20px'}}>
                    What are your affordability options looking like? Put it in the text box below!
                </Typography>

                <Box style={{paddingTop: '50px'}} >

                <TextField id="outlined-basic" value={borrow} label="Borrowing amount ($)" variant="outlined" 
                onChange={(e) => {setBorrow(e.target.value)}}/>  

                </Box>
                <Grid container spacing={10} justifyContent="center" style={{ paddingTop: '50px' }}>

                    <Grid item>
                        <Button variant="outlined"onClick={(event) => {
                        updatePieChart();}}
                >       Calculate Affordability</Button>

                    </Grid>
                    <Grid item>
                        <Button variant="outlined">Return to Default Data</Button>
                    </Grid>

                </Grid>

                </Box>


            </Grid>

        <Grid display="flex" alignItems="center">

            

        </Grid>

        </Grid>
        </Grid>
       
    </Container>
   

    </div>

    );

}

export default Affordability;