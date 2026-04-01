// Cache DOM references for form handling and UI updates.
const form = document.getElementById("calculator-form");
const resultText = document.getElementById("result-text");
const errorText = document.getElementById("error-text");

// Currency formatter for displaying calculated future value.
const currencyFormatter = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
});

// Helper to keep result updates in one place.
function showResult(message) {
    resultText.textContent = message;
}

// Helper to keep error updates in one place.
function showError(message) {
    errorText.textContent = message;
}

// Submit handler sends form data to Flask and updates the results panel.
form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const monthlyPaymentValue = document.getElementById("monthly_payment").value;
    const yearsValue = document.getElementById("years").value;
    const annualRateValue = document.getElementById("annual_interest_rate").value;

    if (!monthlyPaymentValue || !yearsValue || !annualRateValue) {
        showResult("No result available.");
        showError("Please enter all input values before calculating.");
        return;
    }

    const payload = {
        monthly_payment: monthlyPaymentValue,
        years: yearsValue,
        annual_interest_rate: annualRateValue,
    };

    showError("");
    showResult("Calculating...");

    try {
        const response = await fetch("/calculate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        const data = await response.json();

        if (!response.ok) {
            showResult("No result available.");
            showError(data.error || "Unable to calculate future value.");
            return;
        }

        const rawValue = data.future_value ?? data.formatted_future_value;
        const numericValue = Number(rawValue);
        const formattedValue = Number.isFinite(numericValue)
            ? currencyFormatter.format(numericValue)
            : data.formatted_future_value;

        if (!formattedValue) {
            showResult("No result available.");
            showError("Calculation completed, but no value was returned.");
            return;
        }

        showResult(`Future value: ${formattedValue}`);
        showError("");
    } catch (error) {
        showResult("No result available.");
        showError("Network error. Please try again.");
        console.error(error);
    }
});
