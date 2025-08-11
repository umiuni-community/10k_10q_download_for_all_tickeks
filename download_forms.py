# download_10k_10q.py
from sec_edgar_downloader import Downloader
import time
import pandas as pd

DELAY_SECONDS = 0.2

def download_10K_10Q_forms(ticker, dl = Downloader(company_name="UmiUni Research", email_address="you@example.com")):
    # IMPORTANT: set a descriptive user agent per SEC policy

    
    # These will create ./sec-edgar-filings/{FORM}/...
    try:
        dl.get("10-K", ticker, after="1900-01-01")
        dl.get("10-Q", ticker, after="1900-01-01")
        print("Done. See ./sec-edgar-filings/")

        time.sleep(DELAY_SECONDS)

    except Exception as e:
        print(f"❌ Error downloading {ticker}: {e}")




if __name__ == "__main__":
    nasdaq_df = pd.read_csv("./ticker_listing/nasdaq-listed.csv")
    nasdaq_df = nasdaq_df.rename(columns={
        "Symbol": "Symbol",
        "Security Name": "Security Name"
    })
    nasdaq_df["Exchange"] = "NASDAQ"
    print (nasdaq_df.head())

    nyse_df = pd.read_csv("./ticker_listing/nyse-listed.csv")
    nyse_df = nyse_df.rename(columns={
        "ACT Symbol": "Symbol",
        "Company Name": "Security Name"
    })
    nyse_df["Exchange"] = "NYSE"
    print (nyse_df.head())

    # Combine both into a single DataFrame
    combined_df = pd.concat([nasdaq_df, nyse_df], ignore_index=True)
    print(combined_df.head())
    print(combined_df.columns)
    # Loop through tickers
    for i, row in combined_df.iterrows():
        ticker = row["Symbol"].strip()
        print(f"\n[{i+1}/{len(combined_df)}] Processing {ticker} ({row['Exchange']})")
        download_10K_10Q_forms(ticker)
