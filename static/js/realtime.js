
setInterval(() => {
  fetch('/data')
    .then(res => res.json())
    .then(data => {
      document.getElementById("status").innerText = data.occupancy_status;
      updateBadSmellGauge(data.bad_smell_level); // update chart with new data
    });
}, 1000);

// Update the Bad Smell Gauge Chart
function updateBadSmellGauge(value) {
  const ctx = document.getElementById('badSmellGauge').getContext('2d');
  const badSmellGauge = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Bad Smell', 'Clean'],
      datasets: [{
        data: [value, 100 - value],
        backgroundColor: ['#ff5733', '#f0f0f0'],
        borderWidth: 0
      }]
    },
    options: {
      cutoutPercentage: 80,
      rotation: Math.PI,
      circumference: Math.PI,
      animation: {
        animateRotate: true,
        animateScale: true
      }
    });
  });
}
