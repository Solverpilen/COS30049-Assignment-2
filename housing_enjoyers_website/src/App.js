import './App.css';
import React from 'react';
import ResponsiveAppBar from './components/navbar/navbar.js';
import LineChart from './components/charts/LineChart.js'; 
import { Grid, Container, Paper } from '@mui/material';
import PieChart from './components/charts/pieChart.js';
import { BrowserRouter as Router, Route, Routes, Link, BrowserRouter } from 'react-router-dom';
import Affordability from './pages/Affordability.js';
import Home from './pages/Home.js';


function App() {

  return (

<BrowserRouter>

    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/Affordability' element={<Affordability/>} />

    </Routes>

</BrowserRouter>
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
