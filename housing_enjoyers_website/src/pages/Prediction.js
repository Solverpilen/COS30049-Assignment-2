// Libraries
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import dayjs, { isDayjs, startOf } from 'dayjs'; // This is the date library I chose, it has a small file size
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
    const [date, setDate] = useState(''); // The date value from the date picker (should only be a year value)
    const [lineChartData, setLineChartData] = useState(''); // The data passed into createLineChart so that the line chart can be rendered
    const [currentLineChart, setCurrentLineChart] = useState(''); // The actual chart that gets displayed
    const [predictionData, setPredictionData] = useState(''); // the raw data from the server which gets filtered by the date (not sure if best method)

    // useeffect runs the code below on first render to get the default pie chart and bar charts
    useEffect(() => {
        axios.get('http://localhost:8000/models/LinearRegModel') // This may need to change when Bryan makes backend fixes
            .then(response => {
                console.log('Fetched Year and prediction data', response.data);
                // these 2 should initially be the same to show all data
                setPredictionData(response.data.price_prediction);
                setLineChartData(predictionData);
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []); 

    
    // use effect takes place once the chartData changes, creating a new pie chart and setting it to
    // the current pie chart
    useEffect(() => {

        const personalisedLineChart = createLineChart("Predicted House Pricing", 
            lineChartData.x, lineChartData.y, // hopefully this is the correct data, haven't had the backend work for this yet, james you might understand chartjs better
            ["blue", "green", "orange", "#FF6666"], 
            ["blue", "green", "orange", "#FF6666"]
        );
        setCurrentLineChart(personalisedLineChart); // Set the chart to the personalised one
        
    }, [lineChartData]);


    // This should filter the data to a single year (we could do a range of years if we have time)
    function updateLineChart(DateInput) {

        if (isNaN(DateInput))
        {
            return <div>You can only input a year.</div>;
        }

        if (isDayjs(DateInput)) // just checking the MUI date picker isn't a problem
        {
            const Year = dayjs(DateInput);
            const start = Year.startOf();
            const end = Year.endOf();

            // I'm afraid that without actually seeing what the data type looks like I couldn't really start the next part
            // The idea is that if it's an array, loop through and discard any data from dates outside the range, without changing the original raw data
            // Not changing the raw data is so we don't have to ask the backend for it anymore
            const dateRange = predictionData
            // remove dateRange values before start
            // remove dateRange values after end

            setLineChartData(dateRange); // providing new data to the line chart
        }
        else
        {
            return <div>Error: Date picker is not working properly</div>
        }
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
                            {/* This stuff here could change it was just copied over from Affordability */}
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
                                        // the commented out version threw errors but the new one doesn't so could remove
                                        onChange={ (newValue) => setDate(newValue) }
                                        // onChange={ (event) => { setDate(event.target.value); } }
                                    />
                                </LocalizationProvider>
                            </Box>
                            <Grid container spacing={10} columns={2} style={{ paddingTop: '20px' }}>
                                <Grid size={2}>
                                    {/* puts the new chart data on the page */}
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