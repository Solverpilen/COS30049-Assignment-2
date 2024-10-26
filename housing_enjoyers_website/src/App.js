import './App.css';
import React from 'react';
import ResponsiveAppBar from './components/navbar/navbar.js';
import LineChart from './components/charts/LineChart.js'; 
import { Grid, Container, Paper } from '@mui/material';
import 


function App() {

  return (

  <div className="App">
    <ResponsiveAppBar/>
    <div>
      <h1>React Line Chart with Chart.js</h1>
      <Container maxWidth="lg" style={{ height: '100vh', display: 'flex' }}>
      {/* Grid Container to center the charts */}
      <Grid
        container
        spacing={2}
        justifyContent="center"
        alignItems="center"
        style={{ flex: 1 }}
      >
      <LineChart/>
      </Grid>
      </Container>
    </div>



  </div>
  );


}

export default App;
