export const generateChartConfig = (label, dataPoints, color, Labels) => {
    const data = {
    labels: Labels,
      datasets: [
        {
          label: label,
          data: dataPoints,
          borderColor: color,
          backgroundColor: `${color}33`, // Adds transparency
          tension: 0.3,
        },
      ],
    };
  
    const options = {
      responsive: true,
      plugins: {
        legend: { display: true, position: 'top' },
      },
    };
  
    return { data, options };
  };

  export default generateChartConfig;