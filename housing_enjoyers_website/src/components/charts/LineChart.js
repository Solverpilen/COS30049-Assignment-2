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
  const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

  // Define the data for the chart
  const data = {
    labels: labels,
    datasets: [
      {
        label: 'My First Dataset',
        data: [65, 59, 80, 81, 56, 55, 40],
        fill: false,
        borderColor: 'black',
        tension: 0.1,
      },
    ],
  };


  const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Line Chart Example' },
    },
    scales: {
      x: {
        type: 'category', 
        title: {
          display: true,
          text: 'Months' 
        }
      },
      y: {
        title: {
          display: true,
          text: 'Predicted Price ($)'
        }
      }
    }
  };

  // Render the Line chart
  return        <Grid item xs={12} md={5}>
  <Paper elevation={3} style={{ padding: '16px' }}>
    <Line data={data} options={options} />
  </Paper>
</Grid>;

};

export default LineChart;