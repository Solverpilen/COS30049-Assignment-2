import ResponsiveAppBar from '../components/navbar/navbar.js';
import createPieChart from '../services/createPieChart.js';
import { 
    Grid2 as Grid, 
    Container, TextField, Box, Button, Typography 
} from '@mui/material';
import axios from 'axios'
import React, { useEffect, useState } from 'react';
import BedBathAffordability from '../components/BedBathAffordability.js'


function Affordability() {

    const [pieChartData, setPieChartData] = useState({});
    const [borrow, setBorrow] = useState('');
    const [currentPieChart, setCurrentPieChart] = useState('');
    const [barChartData, setBarChartData] = useState('');

    // useeffect runs the code below on first render to get the default pie chart and bar charts
    useEffect(() => {
        axios.get('http://localhost:8000/price_prediction/default_pie_chart')
            .then(response => {
                console.log('Fetched Data:', response.data); // Log data for debugging
                setPieChartData(response.data.ratings); // Update state with fetched data
            })
            .catch(error => console.error('Error fetching data:', error));

        axios.get('http://localhost:8000/price_prediction/default_bar_chart')
            .then(response => {
                console.log('Fetched bedroom, bathroom data', response.data);
                setBarChartData(response.data.total_ratings);
            });


   
    }, []); 

    
    // use effect takes place once the chartData changes, creating a new pie chart and setting it to
    // the current pie chart
    useEffect(() => {

        const personalisedPieChart = createPieChart("Personal Affordability Options", 
            ["High", "Medium", "Low", "Very Low"], 
            [pieChartData[0], pieChartData[1], pieChartData[2], pieChartData[3]], 
            ["blue", "green", "orange", "#FF6666"], 
            ["blue", "green", "orange", "#FF6666"]);
        setCurrentPieChart(personalisedPieChart); // Set the chart to the personalised one
        
    }, [pieChartData]);

    // useEffect(() => {

    //     const personalisedBarChart = createBarChart("Personal Affordability Options", 
    //         ["High", "Medium", "Low", "Very Low"], 
    //         [pieChartData.high, pieChartData.medium, pieChartData.low, pieChartData["very low"]], 
    //         ["blue", "green", "orange", "#FF6666"], 
    //         ["blue", "green", "orange", "#FF6666"]);
    //     setCurrentPieChart(personalisedPieChart); // Set the chart to the personalised one
        
    // }, [barChartData]);



    // does a post request based on the argument borrowingInput. invokes the backend function to then return data
    function updatePieChart(borrowingInput) {

        if (isNaN(borrowingInput))
        {
            return <div>You can only input a whole number without seperators. e.g. 450000</div>;
        }

        const borrowInput = borrowingInput;

        axios.post(`http://localhost:8000/price_prediction/${borrowInput}`)
        .then(response => {
            console.log('Fetched Data:', response.data);

            // sets the chartData to the response from the backend, invoking the use effect that changes the chart data

            setPieChartData(response.data.ratings);

        




        })
 
    };



    return (
    <div className="App">
        <ResponsiveAppBar/>

        <h1>React Line Chart with Chart.js</h1>
        <Container maxWidth="lg" style={{ marginTop: '200px'}} xs={{ display: 'flex' }}>
        {/* Grid Container to center the charts */}
        <Grid container spacing={4}>
        

        <Grid container columns={2} rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>

        <Grid size={1}>
            <div>{currentPieChart}</div>
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
                    onChange={ (event) => { setBorrow(parseInt(event.target.value)); } }
                />
            </Box>
            <Grid container spacing={10} columns={2} style={{ paddingTop: '50px' }}>
                <Grid size={2}>
                    <Button variant="outlined" onClick={() => updatePieChart(borrow)}>Calculate Affordability</Button>
                </Grid>
            </Grid>
        </Grid>
        </Grid>

        </Grid>
    
       
        </Container>

        <BedBathAffordability/>
   
   

    </div>

    
      

    );

}

export default Affordability;