import './App.css';
import React from 'react';
import ResponsiveAppBar from './components/navbar/navbar.js';
import LineChart from './components/charts/LineChart.js'; 
import { Grid, Container, Paper } from '@mui/material';
import PieChart from './components/charts/pieChart.js';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';


function App() {

  return (

    
    <div className="background fade_in_image">
      <ResponsiveAppBar />
      <h1 class="fade_in_move title"> Welcome to Housing Enjoyers Predictive Website!</h1>
    </div>
  // <div className="App">
  //   <ResponsiveAppBar/>
  //   <div>
  //     <h1>React Line Chart with Chart.js</h1>
  //     <Container maxWidth="lg" style={{ height: '100vh', display: 'flex' }}>
  //     {/* Grid Container to center the charts */}
  //     <Grid
  //       container
  //       spacing={2}
  //       justifyContent="center"
  //       alignItems="center"
  //       style={{ flex: 1 }}
  //     >
  //     <LineChart
  //     height="200px"
  //     width="200px"/>
  //     </Grid>

  //     <Grid container
  //       spacing={2}
  //       justifyContent="center"
  //       alignItems="center"
  //       style={{ flex: 1 }}>
  //       <PieChart
  //       height="200px"
  //       width="50px"/>

  //     </Grid>
  //     </Container>
  //   </div>



  // </div>
  // );
  );

}

export default App;
