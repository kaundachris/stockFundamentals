import yfinance as yf
import pandas as pd


class Financials:
    def __init__(self, ticker):
        self.ticker = ticker

    def stock(self):
        return yf.Ticker(self.ticker)

    def income_statement(self):
        financials = pd.DataFrame(self.stock().financials)
        total_revenue = pd.DataFrame(financials.loc['Total Revenue']).transpose()
        total_expenses = pd.DataFrame(financials.loc['Total Expenses']).transpose()
        net_income = pd.DataFrame(financials.loc['Net Income']).transpose()
        performance = [total_revenue, total_expenses, net_income]
        return pd.concat(performance)

    def balance_sheet(self):
        financials = pd.DataFrame(self.stock().balance_sheet)
        total_assets = pd.DataFrame(financials.loc['Total Assets']).transpose()
        goodwill = pd.DataFrame(financials.loc['Goodwill']).transpose()
        total_liabilities = pd.DataFrame(financials.loc['Total Liabilities Net Minority Interest']).transpose()
        current_assets = pd.DataFrame(financials.loc['Current Assets']).transpose()
        current_liabilities = pd.DataFrame(financials.loc['Current Liabilities']).transpose()
        assets_liabilities = [total_assets, goodwill, total_liabilities, current_assets, current_liabilities]
        return pd.concat(assets_liabilities)

    def cash_flow(self):
        cashflow = pd.DataFrame(self.stock().cash_flow)
        operating_activities = pd.DataFrame(cashflow.loc['Cash Flow From Continuing Operating Activities']).transpose()
        capex = pd.DataFrame(cashflow.loc['Capital Expenditure']).transpose()
        free_cash = [operating_activities, capex]
        return pd.concat(free_cash)

    def write_data(self):
        path = f'C:\\Users\\chris\\Documents\\Financial Independence\\{self.ticker}.xlsx'
        with pd.ExcelWriter(path) as writer:
            self.income_statement().to_excel(writer, 'Financials')
            self.balance_sheet().to_excel(writer, 'Balance Sheet')
            self.cash_flow().to_excel(writer, 'Cash Flow')
        return 'Done'


stocks = ['BNTX', 'KHC', 'OKTA', 'TDOC']
for stock in stocks:
    run = Financials(stock)
    run.write_data()
