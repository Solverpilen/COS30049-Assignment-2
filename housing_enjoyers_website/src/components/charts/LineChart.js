// Import required dependencies
import { Line } from 'react-chartjs-2';
import { 
  Chart as ChartJS, 
  LineElement, 
  PointElement, 
  Title, 
  Tooltip, 
  Legend, 
  CategoryScale 
} from 'chart.js';
import {LinearScale } from 'chart.js';
import { Grid, Paper } from '@mui/material';

// Register the chart elements you want to use
ChartJS.register(LineElement, PointElement, Title, Tooltip, Legend, CategoryScale, LinearScale);

const LineChart = () => {
  // Define labels for the chart

  // Render the Line chart
  return       <Grid item xs={12} md={5}>
  <Paper elevation={3} style={{ padding: '16px' }}>
    <Line/>
  </Paper>
</Grid>;

};

export default LineChart;