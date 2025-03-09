const apiKey = 'YOUR_API_KEY';  // Replace with your actual API key
const stockSymbol = 'NVDA';  // Stock symbol for NVIDIA


// Function to Fetch Stock Data (Date Basis)
async function fetchStockData() {
    const url = `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=${stockSymbol}&apikey=${apiKey}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data['Time Series (Daily)']) {
            const timeSeries = data['Time Series (Daily)'];
            let allDates = Object.keys(timeSeries).sort((a, b) => new Date(b) - new Date(a)); // Sort in descending order
            
            // Ensure only continuous trading days (exclude weekends and holidays)
            let latestDates = [];
            let prices = [];
            for (let i = 0; i < allDates.length; i++) {
                if (latestDates.length < 10) {
                    latestDates.push(allDates[i]);
                    prices.push(parseFloat(timeSeries[allDates[i]]['4. close']));
                } else {
                    break;
                }
            }
            latestDates.reverse();
            prices.reverse();

            // Update Current Price
            document.getElementById('stock-price').innerText = `$${prices[prices.length - 1]}`;

            // Update Chart
            updateChart(latestDates, prices);
        } else {
            document.getElementById('stock-price').innerText = 'Data not available';
        }
    } catch (error) {
        document.getElementById('stock-price').innerText = 'Error fetching stock data';
    }
}

// Function to Update Chart
function updateChart(labels, data) {
    const ctx = document.getElementById('stockChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Stock Price (USD)',
                data: data,
                borderColor: '#3498db',
                backgroundColor: 'rgba(52, 152, 219, 0.2)',
                borderWidth: 2,
                pointRadius: 3
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: 'Date' } },
                y: { title: { display: true, text: 'Price (USD)' } }
            }
        }
    });
}

// Fetch stock data on page load
fetchStockData();
