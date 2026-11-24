import yfinance as yf
import pandas as pd
from config.settings import SYMBOL, START_DATE, END_DATE, TIMEFRAME

def fetch_data() -> pd.DataFrame:
    """دریافت داده‌های تاریخی قیمت طلا"""
    print(f"در حال دریافت داده‌های تاریخی برای {SYMBOL}...")
    df = yf.download(SYMBOL, start=START_DATE, end=END_DATE, interval=TIMEFRAME)
    
    # اصلاح ساختار ستون‌ها در نسخه‌های جدید yfinance
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
        
    df.dropna(inplace=True)
    return df
