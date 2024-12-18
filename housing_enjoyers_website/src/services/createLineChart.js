import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS} from 'chart.js';

ChartJS.register();

function createLineChart(Labels, Data) {

    const data = {
		labels: Labels,
		datasets: [
			{
				label: "Predicted House Pricing",
				data: Data,
				fill: false,
				tension: 0,
				borderColor: 'rgb(75, 192, 192)',
				borderWidth: 1,
			},
		]
	};

	const options = {
        type: 'line',
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

	return <Line data={data} options={options}/>;
};

export default createLineChart;