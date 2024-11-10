import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale,
  PointElement,
  LineElement,
  BarElement } from 'chart.js';

// Register necessary Chart.js components
ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, BarElement );

function createAffordabilityBarChart(Labels, highData, mediumData, lowData, veryLowData) {

  const data = {
    labels: Labels,
    datasets: [
      {
        label: "High",
        data: highData,
        backgroundColor: "blue",
        borderColor: "blue",
        borderWidth: 1,
      },
      {
        label: "Medium",
        data: mediumData,
        backgroundColor: "green",
        borderColor:"green",
        borderWidth: 1,
      },
      {
        label: 'Low',
        data: lowData,
        backgroundColor: "orange",
        borderColor:"orange",
        borderWidth: 1,
      },
      {
        label: "Very Low",
        data: veryLowData,
        backgroundColor: "#FF6666",
        borderColor:"#FF6666",
        borderWidth: 1,
      }
    ],
  };


  return <Bar data= {data} options width={500} height={250}/>;
};

export default createAffordabilityBarChart;

