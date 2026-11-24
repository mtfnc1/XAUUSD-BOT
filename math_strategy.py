import pandas as pd
from config.settings import FAST_MA, SLOW_MA

def apply_strategy(df: pd.DataFrame) -> pd.DataFrame:
    """اعمال استراتژی ریاضی تقاطع میانگین‌های متحرک (SMA Crossover)"""
    
    # محاسبه میانگین‌های متحرک ساده (ریاضیات کلاسیک روند)
    df['Fast_MA'] = df['Close'].rolling(window=FAST_MA).mean()
    df['Slow_MA'] = df['Close'].rolling(window=SLOW_MA).mean()
    
    # تولید سیگنال خام: 1 برای خرید، -1 برای فروش
    df['Signal'] = 0
    df.loc[df['Fast_MA'] > df['Slow_MA'], 'Signal'] = 1
    df.loc[df['Fast_MA'] < df['Slow_MA'], 'Signal'] = -1
    
    # شیفت دادن پوزیشن برای جلوگیری از خطای نگاه به آینده (Look-ahead Bias)
    df['Position'] = df['Signal'].shift(1)
    
    return df
