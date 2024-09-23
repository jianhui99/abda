from datetime import date

class InvestmentFund:
    """
    A class to represent an investment fund.

    Operators:
    __str__

    Properties:
    fund_id, fund_name, fund_manager, description, nav, creation_date, performance
    """


    def __init__(self, fund_id, fund_name, fund_manager, description, nav, creation_date, performance):
        self.fund_id = fund_id  # Fund ID
        self.fund_name = fund_name  # Fund Name
        self.fund_manager = fund_manager  # Fund Manager Name
        self.description = description  # Fund Description
        self.nav = nav  # Fund Net Asset Value (NAV)
        self.creation_date = creation_date  # Fund Date of Creation
        self.performance = performance  # Fund Performance (as a percentage)

    def __str__(self):
        """
        Returns a formatted string representation of the fund's details.
        """
        return (f"Fund ID: {self.fund_id}\n"
                f"Fund Name: {self.fund_name}\n"
                f"Fund Manager: {self.fund_manager}\n"
                f"Description: {self.description}\n"
                f"NAV: ${self.nav}\n"
                f"Creation Date: {self.creation_date}\n"
                f"Performance: {self.performance}%")
    


# create an instance of InvestmentFund
fund = InvestmentFund(
    fund_id=1,
    fund_name="Global Equity Fund",
    fund_manager="John",
    description="A diversified global equity fund.",
    nav=150.7500,
    creation_date=date(2024, 9, 23),
    performance=12.5000
)

print(fund)