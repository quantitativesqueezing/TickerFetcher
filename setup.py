from setuptools import setup, find_packages

setup(
    name="TickerFetcher",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5",
        "requests>=2.31",
        "openpyxl>=3.1"
    ],
    entry_points={
        'console_scripts': [
            'TickerFetcher=scripts.run_nightly:main',
        ]
    },
    python_requires='>=3.9',
    author="Quantitative Squeezing",
    description="A Python-based tool for fetching all stock tickers listed on major exchanges (NYSE + NASDAQ + AMEX) and formatting them into a single CSV or XLS formatted spreadsheet for consumption by other applications.",
    url="https://github.com/quantitativesqueezing/TickerFetcher",
)
