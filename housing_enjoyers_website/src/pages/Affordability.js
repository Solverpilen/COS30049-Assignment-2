import ResponsiveAppBar from '../components/navbar/navbar.js';
<<<<<<< HEAD
import createPieChart from '../services/createPieChart.js';
import { Grid, Container, Paper } from '@mui/material';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import axios from 'axios'
import React, { useEffect, useState } from 'react';
import Button from '@mui/material/Button';
import updatePieChart from '../services/updatePieChart.js';
=======
import createPieChart from '../components/charts/createPieChart.js';
import { 
    Grid2 as Grid, 
    Container, TextField, Box, Button, Typography 
} from '@mui/material';
import axios from 'axios'
import React, { useEffect, useState } from 'react';
>>>>>>> f1d3c6883326382c87c49c9bee86283421f7fe70




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
        <Grid container spacing={4}>
        
<<<<<<< HEAD
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
=======
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
>>>>>>> f1d3c6883326382c87c49c9bee86283421f7fe70

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
<<<<<<< HEAD

        <Grid display="flex" alignItems="center">

            

        </Grid>

        </Grid>
=======
>>>>>>> f1d3c6883326382c87c49c9bee86283421f7fe70
        </Grid>
       
        </Container>
   

    </div>

    );

}

export default Affordability;