"""
lifefin.analysis: 复杂理财策略与决策分析模块
"""

def dca_simulator(monthly_investment, annual_return_rate, years):
    """
    基金/股票定投 (DCA) 模拟器
    """
    monthly_rate = annual_return_rate / 12
    months = years * 12
    total_invested = monthly_investment * months
    portfolio_value = 0

    for _ in range(months):
        portfolio_value = (portfolio_value + monthly_investment) * (1 + monthly_rate)

    total_return = portfolio_value - total_invested
    return {
        "total_invested": round(total_invested, 2),
        "portfolio_value": round(portfolio_value, 2),
        "total_return": round(total_return, 2),
        "return_rate": round((total_return / total_invested) * 100, 2)
    }

def buy_vs_rent_decision(home_price, down_payment_ratio, annual_growth_rate, monthly_rent, rent_growth_rate, annual_invest_return, years):
    """
    买房 vs 租房 机会成本权衡 (Trade-off) 分析
    """
    # 买房路径
    down_payment = home_price * down_payment_ratio
    loan_amount = home_price - down_payment
    # 假设30年基准商贷 4.5% 利率进行计算
    mortgage_info = loan_amount * 0.045 / 12  # 简化为首年平均每月利息+本金支出
    monthly_mortgage_estimate = (loan_amount * 0.045 * ((1 + 0.00375)**360)) / (((1 + 0.00375)**360) - 1)

    # 终期房屋估值
    final_home_value = home_price * ((1 + annual_growth_rate) ** years)

    # 租房路径 (首付款拿去理财)
    rent_invest_pool = down_payment * ((1 + annual_invest_return) ** years)

    # 租金机会成本模拟
    total_rent_paid = 0
    current_rent = monthly_rent
    for y in range(years):
        total_rent_paid += current_rent * 12
        current_rent *= (1 + rent_growth_rate)

    return {
        "buy_scenario": {
            "down_payment": round(down_payment, 2),
            "estimated_monthly_mortgage": round(monthly_mortgage_estimate, 2),
            "final_home_value_after_years": round(final_home_value, 2)
        },
        "rent_scenario": {
            "down_payment_investment_growth": round(rent_invest_pool, 2),
            "total_rent_paid": round(total_rent_paid, 2)
        },
        "suggested_decision": "买房" if final_home_value > (rent_invest_pool - total_rent_paid) else "租房并投资"
    }