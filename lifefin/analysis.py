"""
lifefin.analysis: 复杂理财策略与决策分析模块
"""

def dca_simulator(monthly_investment, annual_return_rate, years, verbose=True):
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

def buy_vs_rent_decision(home_price, down_payment_ratio, annual_growth_rate, monthly_rent, rent_growth_amount, annual_invest_return, years, inflation_rate=2.0, verbose=True):
    """
    买房 vs 租房 机会成本权衡分析 (融入通货膨胀率折现)
    :param inflation_rate: 年化通货膨胀率 (如 2.0 代表 2.0%)
    """
    actual_home_price = home_price * 1000
    down_payment = actual_home_price * down_payment_ratio
    loan_amount = actual_home_price - down_payment

    # 1. 买房路径
    # 名义房产估值 (名义价格)
    nominal_final_home_value = actual_home_price * ((1 + (annual_growth_rate / 100)) ** years)
    # 剔除通胀后的真实房产购买力估值
    real_final_home_value = nominal_final_home_value / ((1 + (inflation_rate / 100)) ** years)

    # 假设 30年基准商贷 4.5% 利率进行计算
    monthly_mortgage_estimate = (loan_amount * 0.045 * ((1 + 0.00375)**360)) / (((1 + 0.00375)**360) - 1)

    # 2. 租房路径 (名义理财终值)
    nominal_rent_invest_pool = down_payment * ((1 + (annual_invest_return / 100)) ** years)

    # 累计名义租金支出
    total_rent_paid_nominal = 0
    current_rent = monthly_rent
    for y in range(years):
        total_rent_paid_nominal += current_rent * 12
        current_rent += rent_growth_amount

    # 租房期末结余名义值
    nominal_rent_surplus = nominal_rent_invest_pool - total_rent_paid_nominal
    # 剔除通胀后的租房期末结余真实购买力
    real_rent_surplus = nominal_rent_surplus / ((1 + (inflation_rate / 100)) ** years)

    if verbose:
        print(f"[买/租权衡输入] 房屋总价: {actual_home_price}元 | 房价名义年变动: {annual_growth_rate}% | 预设年通胀率: {inflation_rate}%")
        print(f"               初始月租金: {monthly_rent}元 | 理财年收益率: {annual_invest_return}%")
        print(f"[名义资产对比] 10年后名义房产估值: {round(nominal_final_home_value, 2)} 元")
        print(f"               10年后租房理财名义净结余: {round(nominal_rent_surplus, 2)} 元")

    return {
        "buy_scenario": {
            "down_payment": round(down_payment, 2),
            "estimated_monthly_mortgage": round(monthly_mortgage_estimate, 2),
            "nominal_final_home_value": round(nominal_final_home_value, 2),
            "real_final_home_value_discounted": round(real_final_home_value, 2)
        },
        "rent_scenario": {
            "down_payment_investment_growth_nominal": round(nominal_rent_invest_pool, 2),
            "total_rent_paid_nominal": round(total_rent_paid_nominal, 2),
            "real_rent_surplus_discounted": round(real_rent_surplus, 2)
        },
        "suggested_decision": "买房" if real_final_home_value > real_rent_surplus else "租房并投资"
    }