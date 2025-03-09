document.addEventListener("DOMContentLoaded", () => {
    fetch("http://127.0.0.1:5000/employee-data", {
        method: "GET",  // Make sure the request method is GET
        headers: {
            "Content-Type": "application/json"  // Ensure the request expects JSON data
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log("Fetched Data:", data);  // Debugging log

        const years = Object.keys(data);  // Extract years (keys from the employee data)
        const employeeCount = years.map(year => data[year].count);  // Employee count data
        const yearChange = years.map(year => data[year].change);  // Year-over-year change data
        const percentChange = years.map(year => data[year].percentage);  // Percentage change data

        // Get Table & Chart Elements
        const tableBody = document.getElementById("employeeTable");
        const chartCanvas = document.getElementById("employeeChart");

        if (!tableBody || !chartCanvas) {
            console.error("Table or chart element not found in the DOM.");
            return;
        }

        // Populate Table with employee data
        let rows = "";
        years.forEach(year => {
            rows += `<tr>
                <td>${year}</td>
                <td>${data[year].count.toLocaleString()}</td>
                <td>${data[year].change.toLocaleString()}</td>
                <td>${data[year].percentage}%</td>
            </tr>`;
        });
        tableBody.innerHTML = rows;  // Insert rows into the table

        // Render Chart.js
        const ctx = chartCanvas.getContext("2d");
        new Chart(ctx, {
            type: "bar",  // Bar chart type
            data: {
                labels: years,  // Set years as the labels
                datasets: [
                    {
                        label: "Number of Employees",
                        data: employeeCount,
                        backgroundColor: "rgba(54, 162, 235, 0.7)",  // Blue color for employees
                        borderColor: "rgba(54, 162, 235, 1)",  // Border color for employees
                        borderWidth: 1
                    },
                    {
                        label: "Year-over-Year Change",
                        data: yearChange,
                        backgroundColor: "rgba(255, 99, 132, 0.7)",  // Red color for year change
                        borderColor: "rgba(255, 99, 132, 1)",  // Border color for year change
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: true,  // Enable responsiveness
                maintainAspectRatio: true,  // Maintain aspect ratio
                animation: {
                    duration: 0  // Disable animations to make it fixed
                },
                scales: {
                    y: {
                        beginAtZero: true,  // Start the Y axis from zero
                        grid: {
                            color: "rgba(255, 255, 255, 0.1)"  // Dark grid lines
                        },
                        ticks: {
                            color: "#fff"  // White color for Y axis ticks
                        }
                    },
                    x: {
                        ticks: {
                            color: "#fff"  // White color for X axis ticks
                        }
                    }
                },
                plugins: {
                    legend: {
                        labels: {
                            color: '#fff'  // Legend text color
                        }
                    }
                },
                elements: {
                    bar: {
                        borderWidth: 1
                    }
                },
                layout: {
                    padding: 10
                }
            },
            plugins: [
                {
                    beforeDraw: function (chart) {
                        const ctx = chart.ctx;
                        ctx.save();
                        ctx.fillStyle = '#333';  // Set background color to dark
                        ctx.fillRect(0, 0, chart.width, chart.height);  // Apply dark background
                        ctx.restore();
                    }
                }
            ]
        });
    })
    .catch(error => console.error("Error fetching employee data:", error));
});
