"""
lifefin.calculators: 基础金融计算器模块
"""

def mortgage_calculator(principal, annual_rate, years, payment_type="equal_payment", verbose=True):
    """
    房贷计算器
    :param principal: 贷款本金 (元)
    :param annual_rate: 年利率百分比 (如 4.5 代表 4.5%)
    :param years: 贷款年限
    :param payment_type: 'equal_payment' (等额本息) 或 'equal_principal' (等额本金)
    """
    if verbose:
        print(f"[房贷计算输入] 本金: {principal}元 | 年利率: {annual_rate}% | 期限: {years}年 | 还款方式: {payment_type}")

    decimal_rate = annual_rate / 100
    monthly_rate = decimal_rate / 12
    months = years * 12

    if payment_type == "equal_payment":
        monthly_payment = principal * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
        total_payment = monthly_payment * months
        total_interest = total_payment - principal
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2)
        }
    elif payment_type == "equal_principal":
        monthly_principal = principal / months
        payments = []
        total_interest = 0
        for m in range(1, months + 1):
            interest = (principal - monthly_principal * (m - 1)) * monthly_rate
            total_interest += interest
            payments.append(monthly_principal + interest)
        total_payment = principal + total_interest
        return {
            "first_month_payment": round(payments[0], 2),
            "last_month_payment": round(payments[-1], 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2)
        }
    else:
        raise ValueError("payment_type 必须是 'equal_payment' 或 'equal_principal'")

def savings_interest(principal, annual_rate, years, compound_frequency=1, verbose=True):
    """
    存款利息计算 (支持复利)
    :param annual_rate: 年利率百分比 (如 3 代表 3%)
    """
    if verbose:
        print(f"[存款利息输入] 本金: {principal}元 | 年利率: {annual_rate}% | 期限: {years}年 | 每复利频率: {compound_frequency}次/年")

    decimal_rate = annual_rate / 100
    amount = principal * (1 + decimal_rate / compound_frequency) ** (compound_frequency * years)
    interest = amount - principal
    return {
        "final_amount": round(amount, 2),
        "total_interest": round(interest, 2)
    }