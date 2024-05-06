from flask import Flask, render_template, request
import pandas as pd

# Read financial data from CSV into a DataFrame
financial_data = pd.read_csv('Financial_data.csv')

# Define Flask app
app = Flask(__name__)

# Define chatbot function
def simple_chatbot(user_query, company, year):
    # Filter DataFrame based on company and year
    company_data = financial_data[(financial_data['Company'] == company) & (financial_data['Fiscal Year'] == year)]
    
    if user_query == "What is the total revenue?":
        total_revenue = company_data['Total Revenue'].values[0]
        return f"The total revenue for {company} in {year} is {total_revenue}."
    elif user_query == "How has net income changed over the last year?":
        net_income_change = company_data['Net Income'].diff().values[0]
        net_income_percentage = (net_income_change / company_data['Net Income'].values[0]) * 100
        return f"The net income for {company} has changed by {net_income_change} ({net_income_percentage:.2f}%) over the last year."
    elif user_query == "What are the total assets?":
        total_assets = company_data['Total Assets'].values[0]
        return f"The total assets for {company} in {year} are {total_assets}."
    elif user_query == "What are the total liabilities?":
        total_liabilities = company_data['Total Liabilities'].values[0]
        return f"The total liabilities for {company} in {year} are {total_liabilities}."
    elif user_query == "What is the cash flow from operating activities?":
        cash_flow = company_data['Cash Flow from Operating Activities'].values[0]
        return f"The cash flow from operating activities for {company} in {year} is {cash_flow}."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form['user_query']
    company = request.form['company']
    year = int(request.form['year'])
    response = simple_chatbot(user_query, company, year)
    return render_template('index.html', response=response)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
