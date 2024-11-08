import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register();

function createLineChart(Label, Labels, Data, backGroundColor, Bordercolor) {

    const config = {
        type: 'line',
        data: data,
    };

    const data = {
		labels: Labels,
		datasets: [
		{
			label: Label,
			data: Data,
            fill: false,
            tension: 0,
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

	return <Line data={data} options={options}/>;
};

export default createLineChart;