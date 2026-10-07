"""
lifefin.calculators: 基础金融计算器模块
"""

def mortgage_calculator(principal, annual_rate, years, payment_type="equal_payment"):
    """
    房贷计算器
    :param principal: 贷款本金 (元)
    :param annual_rate: 年利率 (例如 0.045 代表 4.5%)
    :param years: 贷款年限
    :param payment_type: 'equal_payment' (等额本息) 或 'equal_principal' (等额本金)
    """
    monthly_rate = annual_rate / 12
    months = years * 12

    if payment_type == "equal_payment":
        # 等额本息每月还款额公式
        monthly_payment = principal * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
        total_payment = monthly_payment * months
        total_interest = total_payment - principal
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2)
        }
    elif payment_type == "equal_principal":
        # 等额本金
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

def savings_interest(principal, annual_rate, years, compound_frequency=1):
    """
    存款利息计算 (支持复利)
    :param compound_frequency: 每年复利次数，1为年复利，12为月复利
    """
    amount = principal * (1 + annual_rate / compound_frequency) ** (compound_frequency * years)
    interest = amount - principal
    return {
        "final_amount": round(amount, 2),
        "total_interest": round(interest, 2)
    }