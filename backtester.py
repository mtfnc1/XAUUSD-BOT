import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_backtest(df: pd.DataFrame) -> dict:
    """محاسبه بازدهی استراتژی در مقایسه با بازار بر اساس داده‌های تاریخی"""
    
    df['Market_Return'] = df['Close'].pct_change()
    df['Strategy_Return'] = df['Market_Return'] * df['Position']
    
    df.dropna(inplace=True)
    
    # محاسبه رشد تجمعی (مبنای ۱ واحد پول)
    df['Cumulative_Market'] = (1 + df['Market_Return']).cumprod()
    df['Cumulative_Strategy'] = (1 + df['Strategy_Return']).cumprod()
    
    total_market_return = (df['Cumulative_Market'].iloc[-1] - 1) * 100
    total_strategy_return = (df['Cumulative_Strategy'].iloc[-1] - 1) * 100
    
    trades_count = df['Position'].diff().abs().sum() / 2
    
    performance_metrics = {
        "Total_Market_Return_Pct": total_market_return,
        "Total_Strategy_Return_Pct": total_strategy_return,
        "Trades_Count": int(trades_count),
        "Final_DataFrame": df
    }
    
    return performance_metrics

def plot_results(df: pd.DataFrame):
    """رسم نمودار مقایسه عملکرد استراتژی و بازار با matplotlib"""
    plt.figure(figsize=(12, 6))
    
    # رسم خط عملکرد بازار (خرید و نگهداری)
    plt.plot(df.index, df['Cumulative_Market'], label='Market (Buy & Hold)', color='gray', alpha=0.8, linestyle='--')
    
    # رسم خط عملکرد استراتژی ریاضی
    plt.plot(df.index, df['Cumulative_Strategy'], label='Strategy (SMA Crossover)', color='blue', linewidth=2)
    
    plt.title('XAUUSD Algorithmic Trading Strategy vs Market Performance', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Growth of $1 Investment', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    # نمایش پنجره نمودار
    plt.show()

