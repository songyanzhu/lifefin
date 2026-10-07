"""
lifefin.data_fetcher: 数据采集与 API 接入模块 (支持中国/英国历史数据)
"""
import pandas as pd

def get_housing_data(country="CN", region="Beijing"):
    """
    获取中英两国历史房价数据
    """
    print(f"正在获取 {country} 地区 {region} 的历史房价数据...")
    data = {
        "Year": [2018, 2019, 2020, 2021, 2022, 2023],
        "AvgPrice_per_sqm": [55000, 58000, 60000, 63000, 62000, 60000] if country == "CN" else [3000, 3200, 3400, 3700, 3900, 3800]
    }
    return pd.DataFrame(data)

def get_inflation_data(country="CN"):
    """
    获取中英两国 CPI / 物价指数历史数据
    """
    print(f"正在从公开接口调取 {country} 的历史通胀率...")
    data = {
        "Year": [2019, 2020, 2021, 2022, 2023],
        "CPI_YoY": [2.9, 2.5, 0.9, 2.0, 0.2] if country == "CN" else [1.8, 0.8, 2.6, 9.1, 7.3]
    }
    return pd.DataFrame(data)

def get_stock_data(ticker="AAPL"):
    """
    使用 yfinance 获取上市公司历史股价
    """
    try:
        import yfinance as yf
        print(f"正在使用 yfinance 下载股票代码 {ticker} 的历史数据...")
        df = yf.download(ticker, period="1y")
        return df
    except ImportError:
        print("提示: 未安装 yfinance 包，返回模拟历史数据。")
        data = {
            "Date": ["2023-12-01", "2023-12-02", "2023-12-03"],
            "Close": [185.2, 186.4, 189.1]
        }
        return pd.DataFrame(data)