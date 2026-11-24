def calculate_risk_levels(entry_price: float, side: int, stop_loss_pct: float, rr_ratio: float):
    """محاسبه حد ضرر (Stop Loss) و حد سود (Take Profit) بر اساس درصد ثابت"""
    if side == 1:  # پوزیشن خرید (Buy)
        stop_loss = entry_price * (1 - stop_loss_pct)
        take_profit = entry_price * (1 + (stop_loss_pct * rr_ratio))
    elif side == -1:  # پوزیشن فروش (Sell)
        stop_loss = entry_price * (1 + stop_loss_pct)
        take_profit = entry_price * (1 - (stop_loss_pct * rr_ratio))
    else:
        stop_loss, take_profit = None, None
        
    return stop_loss, take_profit
