# NBA MVP Prediction Project

This project aims to predict the Most Valuable Player (MVP) of the NBA season using web scraping techniques with Python, along with data manipulation and analysis. The project collects data from [basketball-reference.com](https://www.basketball-reference.com/) for MVPs, team standings, and player statistics. The collected data is then processed to create CSV files for further analysis and prediction.

## Project Structure

- **`scraping.py`**: Python script responsible for scraping data from basketball-reference.com.
- **`pre_processing.ipynb`**: Jupyter Notebook for data manipulation and analysis.
- **`mvps/`**: Directory containing HTML mvp stats files from basketball-reference.com.
- **`players/`**: Directory containing HTML players stats files from basketball-reference.com.
- **`teams/`**: Directory containing HTML teams stats files from basketball-reference.com.
- **`data/`**: Directory containing CSV files generated from the scraped data.
  - **`mvps.csv`**: MVPs data.
  - **`players.csv`**: Player statistics data.
  - **`teams.csv`**: Team standings data.

## Dependencies

- `requests`: For making HTTP requests to fetch web pages.
- `selenium`: For browser automation to handle JavaScript-rendered pages.
- `beautifulsoup4`: For parsing HTML content.
- `pandas`: For data manipulation and analysis.

## Usage

1. Run `scraping.py` to fetch data from basketball-reference.com and save HTML pages.
2. Execute `pre_processing.ipynb` to process the HTML pages and create CSV files.

## Developers

- Ellen Shen
- José Fernandes
