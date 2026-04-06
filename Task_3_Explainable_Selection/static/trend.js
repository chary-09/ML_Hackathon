function renderTrendChart(history) {
    const canvas = document.getElementById("trendChart");
    if (!canvas || !history || history.length === 0) return;

    const labels = history.map((entry, i) => {
        if (entry.timestamp) {
            const d = new Date(entry.timestamp);
            return d.toLocaleDateString("en-IN", { day: "2-digit", month: "short" }) + " " + d.toLocaleTimeString("en-IN", { hour: "2-digit", minute: "2-digit" });
        }
        return "Session " + (i + 1);
    });

    const scores = history.map(entry => entry.score || entry.burnout_score || 0);
    const predictions = history.map(entry => entry.prediction || "Unknown");

    const pointColors = predictions.map(p => {
        if (p === "High" || p === "High Risk") return "#f85149";
        if (p === "Medium" || p === "Medium Risk") return "#d29922";
        return "#238636";
    });

    new Chart(canvas, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Burnout Risk Score (%)",
                data: scores,
                borderColor: "#58a6ff",
                backgroundColor: "rgba(88, 166, 255, 0.1)",
                fill: true,
                tension: 0.4,
                pointBackgroundColor: pointColors,
                pointBorderColor: pointColors,
                pointRadius: 6,
                pointHoverRadius: 9,
                borderWidth: 3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: 'rgba(22, 27, 34, 0.9)',
                    titleColor: '#e6edf3',
                    bodyColor: '#e6edf3',
                    borderColor: 'rgba(48, 54, 61, 0.8)',
                    borderWidth: 1,
                    padding: 12,
                    callbacks: {
                        afterLabel: function(ctx) {
                            return "Prediction: " + predictions[ctx.dataIndex];
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    grid: { color: "rgba(48, 54, 61, 0.5)" },
                    title: {
                        display: true,
                        text: 'Risk Score (%)'
                    }
                },
                x: {
                    grid: { display: false }
                }
            }
        }
    });
}
