## TickerFetcher

A Python-based tool for fetching all stock tickers listed on major exchanges (NYSE + NASDAQ + AMEX) and formatting them into a single CSV or XLS formatted spreadsheet for consumption by other applications.

- Full master CSV
- Diff CSV
- Color-coded Excel diff (New / Delisted / Renamed / Exchange Changed)
- Daily log of counts

## Installation

```bash
git clone https://github.com/yourusername/StockTickerss.git
cd StockTickerss
pip install -e .


## Usage

from StockTickerss.fetcher import StockTickerFetcher

fetcher = StockTickerFetcher()
fetcher.run()

## Or run nightly using CLI:

python -m scripts.run_nightly

## Requirements

- Python 3.9+
- pandas
- requests
- openpyxl
