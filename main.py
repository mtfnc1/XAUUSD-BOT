from data.fetcher import fetch_data
from strategy.math_strategy import apply_strategy
from risk.risk_manager import calculate_risk_levels
from execution.backtester import run_backtest, plot_results
from config.settings import STOP_LOSS_PCT, RISK_REWARD_RATIO

def main():
    print("=== شروع اجرای ربات نسخه اول XAUUSD (همراه با بک‌تست و نمودار) ===")
    
    # ۱. دریافت داده‌ها
    df = fetch_data()
    
    # ۲. اعمال استراتژی
    df = apply_strategy(df)
    
    # ۳. اجرای موتور بک‌تست
    backtest_results = run_backtest(df)
    
    print("\n--- نتایج ارزیابی عملکرد (بک‌تست) ---")
    print(f"بازدهی کل استراتژی: {backtest_results['Total_Strategy_Return_Pct']:.2f}%")
    print(f"بازدهی کل بازار (خرید و نگهداری): {backtest_results['Total_Market_Return_Pct']:.2f}%")
    print(f"تعداد کل معاملات انجام شده: {backtest_results['Trades_Count']}")
    
    # ۴. بررسی وضعیت آخرین کندل بازار
    latest = backtest_results['Final_DataFrame'].iloc[-1]
    current_price = latest['Close']
    current_position = int(latest['Position']) if not pd.isna(latest['Position']) else 0
    
    print("\n--- وضعیت فعلی بازار (آخرین کندل) ---")
    print(f"آخرین قیمت طلا: {current_price:.2f}")
    
    signal_text = "خرید (Buy / Long)" if current_position == 1 else "فروش یا خروج (Sell / Flat)"
    print(f"سیگنال فعال: {signal_text}")
    
    # ۵. محاسبه سطوح ریسک
    if current_position != 0:
        sl, tp = calculate_risk_levels(current_price, current_position, STOP_LOSS_PCT, RISK_REWARD_RATIO)
        print(f"حد ضرر (Stop Loss): {sl:.2f}")
        print(f"حد سود (Take Profit): {tp:.2f}")
        
    # ۶. رسم نمودار عملکرد نهایی
    print("\nدر حال باز کردن پنجره نمودار عملکرد...")
    plot_results(backtest_results['Final_DataFrame'])

if __name__ == "__main__":
    main()

