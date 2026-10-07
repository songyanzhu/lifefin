"""
lifefin.analysis: 复杂理财策略与决策分析模块
"""

def dca_simulator(monthly_investment, annual_return_rate, years, verbose=True):
    """
    基金/股票定投 (DCA) 模拟器
    :param annual_return_rate: 年化收益率百分比 (如 8 代表 8%)
    """
    if verbose:
        print(f"[定投模拟输入] 每月投资额: {monthly_investment}元 | 年收益率: {annual_return_rate}% | 期限: {years}年")

    decimal_rate = annual_return_rate / 100
    monthly_rate = decimal_rate / 12
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

def buy_vs_rent_decision(home_price, down_payment_ratio, annual_growth_rate, monthly_rent, rent_growth_amount, annual_invest_return, years, verbose=True):
    """
    买房 vs 租房 机会成本权衡 (Trade-off) 分析
    :param home_price: 房屋总价 (单位: k, 即千)
    :param annual_growth_rate: 房价年增长率百分比 (如 2 代表 2%)
    :param rent_growth_amount: 租金每年上涨的绝对金额
    :param annual_invest_return: 理财年化收益率百分比 (如 3 代表 3%)
    """
    actual_home_price = home_price * 1000
    if verbose:
        print(f"[买/租权衡输入] 房屋总价: {actual_home_price}元 ({home_price}k) | 首付比例: {down_payment_ratio*100}% | 房价年增值率: {annual_growth_rate}%")
        print(f"               初始月租金: {monthly_rent}元 | 房租每年递增: {rent_growth_amount}元 | 理财年收益率: {annual_invest_return}% | 模拟周期: {years}年")

    down_payment = actual_home_price * down_payment_ratio
    loan_amount = actual_home_price - down_payment

    # 假设30年基准商贷 4.5% 利率进行计算
    monthly_mortgage_estimate = (loan_amount * 0.045 * ((1 + 0.00375)**360)) / (((1 + 0.00375)**360) - 1)

    # 终期房屋估值
    final_home_value = actual_home_price * ((1 + (annual_growth_rate / 100)) ** years)

    # 租房路径 (首付款拿去理财)
    rent_invest_pool = down_payment * ((1 + (annual_invest_return / 100)) ** years)

    # 租金机会成本模拟
    total_rent_paid = 0
    current_rent = monthly_rent
    for y in range(years):
        total_rent_paid += current_rent * 12
        current_rent += rent_growth_amount

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