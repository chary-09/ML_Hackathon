function renderModelChart(metrics) {
    new Chart(document.getElementById("modelChart"), {
        type: "bar",
        data: {
            labels: Object.keys(metrics),
            datasets: [{
                label: "Accuracy (%)",
                data: Object.values(metrics),
                backgroundColor: ["#2196F3","#9C27B0","#FF9800"]
            }]
        },
        options: {
            scales: { y: { beginAtZero: true, max: 100 } }
        }
    });
}