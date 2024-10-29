import ResponsiveAppBar from '../components/navbar/navbar.js';
import PieChart from '../components/charts/PieChart.js';
import LineChart from '../components/charts/LineChart.js'; 
import { Grid, Container, Paper } from '@mui/material';
import TextField from '@mui/material/TextField';




function Affordability() {

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
      <PieChart
      height="10px"
      width="50px"/>
    </Grid>

    <Grid container
    spacing={2}
    justifyContent="center"
    alignItems="center"
    item xs={6}>

    <TextField id="outlined-basic" label="Outlined" variant="outlined" />

    </Grid>

   
    </Container>
    </div>




    );

}

export default Affordability;