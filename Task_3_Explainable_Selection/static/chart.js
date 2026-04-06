// Chart styling defaults
Chart.defaults.color = '#8b949e';
Chart.defaults.font.family = 'Inter, sans-serif';

function renderCharts() {
    // 1. Model Accuracy Chart
    const accCtx = document.getElementById("accuracyChart");
    if (accCtx && typeof metrics !== 'undefined') {
        new Chart(accCtx, {
            type: "bar",
            data: {
                labels: Object.keys(metrics),
                datasets: [{
                    label: "Accuracy (%)",
                    data: Object.values(metrics),
                    backgroundColor: [
                        "rgba(88, 166, 255, 0.8)",
                        "rgba(35, 134, 54, 0.8)",
                        "rgba(210, 153, 34, 0.8)"
                    ],
                    borderWidth: 0,
                    borderRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: { 
                        beginAtZero: true, 
                        max: 100,
                        grid: { color: 'rgba(48, 54, 61, 0.5)' }
                    },
                    x: {
                        grid: { display: false }
                    }
                }
            }
        });
    }

    // 2. Feature Importance Chart
    const featCtx = document.getElementById("featureChart");
    if (featCtx && typeof features !== 'undefined') {
        new Chart(featCtx, {
            type: "bar",
            data: {
                labels: Object.keys(features),
                datasets: [{
                    label: "Importance",
                    data: Object.values(features),
                    backgroundColor: "rgba(163, 113, 247, 0.8)",
                    borderRadius: 4
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        grid: { color: 'rgba(48, 54, 61, 0.5)' }
                    },
                    y: {
                        grid: { display: false }
                    }
                }
            }
        });
    }

    // 3. Probabilities Doughnut Chart
    const probCtx = document.getElementById("probChart");
    if (probCtx && typeof probabilities !== 'undefined' && probabilities) {
        new Chart(probCtx, {
            type: "doughnut",
            data: {
                labels: Object.keys(probabilities),
                datasets: [{
                    data: Object.values(probabilities),
                    backgroundColor: [
                        "rgba(35, 134, 54, 0.8)",  // Low
                        "rgba(210, 153, 34, 0.8)", // Medium
                        "rgba(248, 81, 73, 0.8)"   // High
                    ],
                    borderColor: "#0d1117",
                    borderWidth: 2,
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { padding: 20, usePointStyle: true }
                    }
                },
                cutout: '70%'
            }
        });
    }
}