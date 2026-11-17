def daily_return(prev_close, close):
    return (close - prev_close)/prev_close

def format_pct(x):
    return f"{x:+.2%}"