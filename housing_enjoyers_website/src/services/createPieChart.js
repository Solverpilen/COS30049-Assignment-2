import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

// Register necessary Chart.js components
ChartJS.register(ArcElement, Tooltip, Legend);

function createPieChart(Label, Labels, Data, backGroundColor, Bordercolor) {

	const data = {
		labels: Labels,
		datasets: [
		{
			label: Label,
			data: Data,
			backgroundColor: backGroundColor,
			borderColor:Bordercolor,
			borderWidth: 1,
		},

		
		],
	};

	const options = {
		plugins: {
		legend: {
			position: 'top',
		},
		tooltip: {
			callbacks: {
			label: function (tooltipItem) {
				const value = tooltipItem.raw; // Get the raw value (e.g., 12, 19)
				const label = tooltipItem.label; // Get the label (e.g., "Red")
				return `${label}: ${value} units`; // Custom tooltip text
			},
			},
		},
		},
	};

	return <Pie data= {data} options = {options}/>;
	};




export default createPieChart;