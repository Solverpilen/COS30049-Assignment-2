// Libraries
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import dayjs from 'dayjs';
import { 
    Grid2 as Grid, 
    Container, Box, Button, Typography 
} from '@mui/material';
import { DateCalendar } from '@mui/x-date-pickers/DateCalendar'
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
// Local Files
import ResponsiveAppBar from '../components/navbar';
import createLineChart from '../services/createLineChart';


function Prediction() {
    const [date, setDate] = useState('');
    const [lineChartData, setLineChartData] = useState('');
    const [currentLineChart, setCurrentLineChart] = useState('');
    const [predictionData, setPredictionData] = useState('');

    // useeffect runs the code below on first render to get the default pie chart and bar charts
    useEffect(() => {
        axios.get('http://localhost:8000/models/LinearRegModel')
            .then(response => {
                console.log('Fetched Year and prediction data', response.data);
                setPredictionData(response.data.price_prediction);
                setLineChartData(predictionData);
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []); 

    
    // use effect takes place once the chartData changes, creating a new pie chart and setting it to
    // the current pie chart
    useEffect(() => {

        const personalisedLineChart = createLineChart("Predicted House Pricing", 
            lineChartData.x, lineChartData.y, 
            ["blue", "green", "orange", "#FF6666"], 
            ["blue", "green", "orange", "#FF6666"]
        );
        setCurrentLineChart(personalisedLineChart); // Set the chart to the personalised one
        
    }, [lineChartData]);


    // does a post request based on the argument borrowingInput. invokes the backend function to then return data    
    function updateLineChart(DateInput) {

        if (isNaN(DateInput))
        {
            return <div>You can only input a year.</div>;
        }

        const Year = DateInput;
        dateRange = predictionData

        setLineChartData(dateRange);
    };



    return (
    <div className="App">
        <ResponsiveAppBar/>
        <h1>React Line Chart with Chart.js</h1>

        <Container maxWidth="lg" style={{ marginTop: '200px'}} xs={{ display: 'flex' }}>
            {/* Grid Container to center the charts */}
            <Grid container spacing={4}>
                <Grid container columns={2} rowSpacing={6} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>

                    <Grid container size={2} rowSpacing={1}>
                        <Grid container size={1}>
                            <Typography className='text_box' align='justify' xs={{border: '2px solid #1976d2' , borderRadius: '16px'}}>
                                The median weekly income of Australia is $1,500 in 2023. If that person works 50 weeks of the year
                                then that comes to a total of $75,000 per year. Assuming monthly expenses of 1,000 per month, 
                                this particular person can borrow a maximum of $394,000 to pay for their property. 
                                This is what the pie chart to the left shows the affordability of such properties from 2017 to 2018 according 
                                these statistics.
                            </Typography>
                        </Grid>

                        <Grid container size={1} direction={'column'}>
                            <Typography align='center' style={{ paddingTop: '20px'}}>
                                When are you looking to buy a house? Use the date pickers below!
                            </Typography>

                            <Box style={{padding: '2em 4em 0em'}}>
                                <LocalizationProvider dateAdapter={AdapterDayjs}>
                                    <DateCalendar 
                                        views={['year']}
                                        openTo="year"
                                        onChange={ (newValue) => setDate(newValue) }
                                        // onChange={ (event) => { setDate(event.target.value); } }
                                    />
                                </LocalizationProvider>
                            </Box>
                            <Grid container spacing={10} columns={2} style={{ paddingTop: '20px' }}>
                                <Grid size={2}>
                                    <Button variant="outlined" onClick={() => updateLineChart(date)}>Predict Prices</Button>
                                </Grid>
                            </Grid>
                        </Grid>
                    </Grid>

                    <Grid size={2}>
                        <div>{currentLineChart}</div>
                    </Grid>
                </Grid>
            </Grid>
        </Container>
    </div>
    );
}

export default Prediction;