import ResponsiveAppBar from '../components/navbar.js';
import createPieChart from '../services/createPieChart.js';
import { 
    Grid2 as Grid, 
    Container, TextField, Box, Button, Typography 
} from '@mui/material';
import axios from 'axios'
import React, { useEffect, useState } from 'react';


function Affordability() {

    const [pieChartData, setPieChartData] = useState('');
    const [borrow, setBorrow] = useState('');
    const [currentPieChart, setCurrentPieChart] = useState('');
    const [error, setError] = useState(true);
    const [nameError, setNameError] = useState(true)

     //useeffect runs the code below on first render to get the default pie chart
     useEffect(() => {
         axios.get('http://localhost:8000/price_prediction/default_pie_chart')
             .then(response => {
                 console.log('Fetched Data:', response.data); // Log data for debugging
                 setPieChartData(response.data.ratings); // Update state with fetched data
                })
             .catch(error => console.error('Error fetching data:', error));

    }, []); 



    
    // use effect takes place once the chartData changes, creating a new pie chart and setting it to
    // the current pie chart
    useEffect(() => {


        const personalisedPieChart = createPieChart("Personal Affordability Options", 
            ["High", "medium", "Low", "Very Low"], 
            [pieChartData.high, pieChartData.medium, pieChartData.low, pieChartData.very_low], 
            ["blue", "green", "orange", "#FF6666"], 
            ["blue", "green", "orange", "#FF6666"]);
        setCurrentPieChart(personalisedPieChart); // Set the chart to the personalised one
        
    }, [pieChartData]);

    // useEffect(() => {

    //     const personalisedBarChart = createBarChart("Personal Affordability Options", 
    //         ["High", "Medium", "Low", "Very Low"], 
    //         [pieChartData.high, pieChartData.medium, pieChartData.low, pieChartData.very_low], 
    //         ["blue", "green", "orange", "#FF6666"], 
    //         ["blue", "green", "orange", "#FF6666"]);
    //     setCurrentPieChart(personalisedPieChart); // Set the chart to the personalised one
        
    // }, [barChartData]);



    // does a post request based on the argument borrowingInput. invokes the backend function to then return data
    function updatePieChart(borrowingInput) {

        if (!Number.isInteger(borrowingInput))
        {
            return <div>You can only input a whole number without seperators. e.g. 450000</div>;
        }
        else {
            const borrowInput = borrowingInput;

            axios.post(`http://localhost:8000/price_prediction/${borrowInput}`)
            .then(response => {
                console.log('Fetched Data:', response.data);
    
                // sets the chartData to the response from the backend, invoking the use effect that changes the chart data
    
                setPieChartData(response.data.ratings);
            })
            
        }


    };

    const handleNameChange = event => {
        const value = event.target.value;

        // Check if the value is an integer
        if (/^[0-9]+$/.test(value)) {
            setBorrow(parseInt(value));

            setError(false); // Clear any previous error
        } else {
            setError(true); 

        }
    }


    return (
    <div className="App">

        
        {/* navbar for every page */}
        <ResponsiveAppBar/>  

        <h1>Affordability Options Pie Chart</h1>
        <Container maxWidth="lg" style={{ marginTop: '200px'}} xs={{ display: 'flex' }}>
        {/* Grid Container to center the charts */}
        <Grid container spacing={4}>
        

        <Grid container columns={2} rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>

        
        {/* Grid that holds the pie chart */}
        <Grid size={1}>
            <div>{currentPieChart}</div>
        </Grid>

        {/* Grid that holds the rest of the content, beginning with the explanation of the pag */}

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
                <TextField type="number"
                    id="outlined-basic"
                    label="Maximum borrowing amount ($)"
                    variant="outlined" placeholder="75000" 
                    fullWidth
                    onChange={ (event) => { handleNameChange(event) } }
                    inputProps={{
                        pattern: "^[0-9]+$",
                      }}

                     error={error}

                     helperText={
                        error ? "Please enter a valid whole number" : ""
                      }
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

   
   

    </div>

    
      

    );

}

export default Affordability;