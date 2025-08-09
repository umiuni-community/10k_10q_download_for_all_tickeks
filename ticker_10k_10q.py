# download_10k_10q.py
from sec_edgar_downloader import Downloader

# IMPORTANT: set a descriptive user agent per SEC policy
dl = Downloader(company_name="UmiUni Research", email_address="you@example.com")

ticker = "UNH"  # change this

# These will create ./sec-edgar-filings/{FORM}/...
dl.get("10-K", ticker, after="1900-01-01")
dl.get("10-Q", ticker, after="1900-01-01")
print("Done. See ./sec-edgar-filings/")

