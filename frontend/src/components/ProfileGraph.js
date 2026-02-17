import React from 'react';
import { Line } from 'react-chartjs-2';

const ProfileGraph = ({ data }) => {
  const chartData = {
    labels: data.labels,
    datasets: [
      {
        label: 'Profile Data',
        data: data.values,
        fill: false,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
      },
    ],
  };

  return (
    <div>
      <h2>Profile Graph</h2>
      <Line data={chartData} />
    </div>
  );
};

export default ProfileGraph;
