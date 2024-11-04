import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

function updatePieChart(pieChart, newData) {

    pieChart.data.datasets[1].pop();

    pieChart.data.datasets[1].push(newData)

    console.log("update pie chart has ran");

}

export default updatePieChart;