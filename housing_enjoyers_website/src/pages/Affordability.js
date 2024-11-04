import ResponsiveAppBar from '../components/navbar/navbar.js';
import createPieChart from '../components/charts/createPieChart.js';
import { 
    Grid2 as Grid, 
    Container, TextField, Box, Button, Typography 
} from '@mui/material';
import axios from 'axios'
import React, { useEffect, useState } from 'react';




function Affordability() {

    const [chartData, setChartData] = useState({});

    const [income, setIncome] = useState('');

    useEffect(() => {
        axios.get('http://localhost:8000/price_prediction/default_pie_chart')  // Example API call to FastAPI
            .then(response => {
                console.log('Fetched Data:', response.data); // Log data for debugging
                setChartData(response.data.ratings); // Update state with fetched data
            })
            .catch(error => console.error('Error fetching data:', error));
            
    }, []); 

    const defaultPieChart = createPieChart("Default Pie Chart", ["High", "Medium", "Low", "Very Low"], 
        [chartData.high, chartData.medium, chartData.low, chartData["very low"]], ["blue", "green", "orange", "#FF6666"], 
        ["blue", "green", "orange", "#FF6666"]);

    return (
    <div className="App">
        <ResponsiveAppBar/>

  
        <h1>React Line Chart with Chart.js</h1>
        <Container maxWidth="lg" style={{ marginTop: '200px'}} xs={{ display: 'flex' }}>
        {/* Grid Container to center the charts */}
        <Grid container spacing={4}>
        
            <Grid container columns={2} rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>

                <Grid size={1}>
                    <div>{defaultPieChart}</div>
                </Grid>

                <Grid container size={1} direction="column">
                    <Typography className='text_box' align='justify' xs={{border: '2px solid #1976d2' , borderRadius: '16px'}}>
                        The median weekly income of Australia is $1,500 in 2023. If that person works 50 weeks of the year
                        then that comes to a total of $75,000 per year. Assuming monthly expenses of 1,000 per month, 
                        this particular person can borrow a maximum of $394,000 to pay for their property. 
                        This is what the pie chart to the left shows the affordability of such properties from 2017 to 2018 according 
                        these statistics.
                    </Typography>

                    <Typography align='center' style={{ paddingTop: '20px'}}>
                        What are your affordability options looking like? Put it in the text box below!
                    </Typography>

                    <Box style={{padding: '3em 6em 0em'}} >
                        <TextField type="number" id="outlined-basic" label="Maximum borrowing amount ($)" variant="outlined" placeholder="75000" fullWidth
                            onChange={ (event) => { setIncome(parseInt(event.target.value)); } }
                        />
                    </Box>
                    <Grid container spacing={10} columns={2} style={{ paddingTop: '50px' }}>
                        <Grid size={1}>
                            <Button variant="outlined">Calculate Affordability</Button>
                        </Grid>
                        <Grid size={1}>
                            <Button variant="outlined">Return to Default Data</Button>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </Grid>
       
        </Container>
   

    </div>

    );

}

export default Affordability;