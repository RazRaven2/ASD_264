from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# Core financial logic preserved from the original console application.
def calculate_future_value(monthly_payment, years, annual_interest_rate):
    months = years * 12
    monthly_interest_rate = annual_interest_rate / 12 / 100
    future_value = 0

    for _ in range(months):
        future_value = (future_value + monthly_payment) * (1 + monthly_interest_rate)

    return future_value


# Validation helpers keep request parsing clean and easy to extend.
def parse_positive_float(value, field_name):
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must be a number.") from exc

    if parsed < 0:
        raise ValueError(f"{field_name} cannot be negative.")

    return parsed


# Years is an integer field to match the original behavior.
def parse_positive_int(value, field_name):
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must be a whole number.") from exc

    if parsed < 0:
        raise ValueError(f"{field_name} cannot be negative.")

    return parsed


# Main page route that serves the single-page user interface.
@app.route("/")
def index():
    return render_template("index.html")


# API route used by fetch() from the browser to compute future value.
@app.route("/calculate", methods=["POST"])
def calculate():
    payload = request.get_json(silent=True) or {}

    try:
        monthly_payment = parse_positive_float(payload.get("monthly_payment"), "Monthly payment")
        years = parse_positive_int(payload.get("years"), "Number of years")
        annual_interest_rate = parse_positive_float(payload.get("annual_interest_rate"), "Annual interest rate")

        future_value = calculate_future_value(monthly_payment, years, annual_interest_rate)
        return jsonify(
            {
                "future_value": future_value,
                "formatted_future_value": f"{future_value:.2f}",
            }
        )
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    # Debug mode helps during local development.
    app.run(debug=True)
