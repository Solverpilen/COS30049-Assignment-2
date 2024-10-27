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
import generateChartConfig from '../../services/chartData.js';

// Register the chart elements you want to use
ChartJS.register(LineElement, PointElement, Title, Tooltip, Legend, CategoryScale, LinearScale);

const LineChart = () => {
  // Define labels for the chart
  const chartConfig = generateChartConfig('Example label', [1,2,3,4,5,6,7], 'black', ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']);

  const data = chartConfig.data;
  const options = chartConfig.options;
  // Render the Line chart
  return       <Grid item xs={12} md={5}>
  <Paper elevation={3} style={{ padding: '16px' }}>
    <Line data={data} options={options}/>
  </Paper>
</Grid>;

};

export default LineChart;