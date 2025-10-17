# x-scrapper

Scrape a single public X/Twitter post into clean Markdown. Opens the URL in a real browser (Selenium), waits for the tweet to render, parses it with BeautifulSoup, and saves the result.

- Main script: [/home/wanony/x-scrapper/main.py](/home/wanony/x-scrapper/main.py)
- Requirements: [/home/wanony/x-scrapper/requirements.txt](/home/wanony/x-scrapper/requirements.txt)
- Experiments: [/home/wanony/x-scrapper/experiment](/home/wanony/x-scrapper/experiment)

## What you get

- A Markdown file at `Data/Data.md` containing:
  - Display name and handle
  - The tweet text (best-effort)
- The same content printed to your terminal

## How it works

Under the hood, [`scrap`](/home/wanony/x-scrapper/main.py) does this:
1. Launches Chrome via Selenium and `webdriver-manager`.
2. Opens your tweet URL.
3. Waits (up to 15s) for `article[data-testid="tweet"]` to appear.
4. Parses the page source with BeautifulSoup.
5. Extracts the display name, handle, and main text.
6. Writes Markdown to `Data/Data.md`.

## Prerequisites

- Linux
- Python 3.8+
- Google Chrome or Chromium installed and on PATH
- Internet access (for `webdriver-manager` to fetch the driver)

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If you’re missing packages, the script will tell you how to install them.

## Run

```bash
python main.py "https://x.com/yourclouddude/status/1973463347895861267"
```

- Waits up to 15s for the tweet to load.
- Saves to `Data/Data.md` and prints the same content.

Example output:

```
Display Name - @handle

Tweet content line 1
Tweet content line 2
```

## Tips and gotchas

- Make sure the URL is a public tweet. A login wall can block scraping.
- If it times out:
  - Try again, or increase the 15s timeout in [`WebDriverWait(..., 15)`](/home/wanony/x-scrapper/main.py).
  - The CSS selector might have changed; update `article[data-testid="tweet"]` in [/home/wanony/x-scrapper/main.py](/home/wanony/x-scrapper/main.py).
- `webdriver-manager` downloads a matching ChromeDriver automatically. Ensure Chrome/Chromium is installed.

## Project layout

```
.
├── main.py
├── requirements.txt
└── experiment
    ├── exp.py
    ├── markdown.py
    └── sample.py
```

- [/home/wanony/x-scrapper/main.py](/home/wanony/x-scrapper/main.py): scraper that writes to `Data/Data.md`.
- [/home/wanony/x-scrapper/experiment/exp.py](/home/wanony/x-scrapper/experiment/exp.py): minimal Selenium demo.
- [/home/wanony/x-scrapper/experiment/sample.py](/home/wanony/x-scrapper/experiment/sample.py): simple requests + BeautifulSoup example.
- [/home/wanony/x-scrapper/experiment/markdown.py](/home/wanony/x-scrapper/experiment/markdown.py): simple directory creation snippet.

## Limitations

- Page structure on X changes frequently; you may need to adjust selectors/slicing.
- Only extracts the main tweet text (no media, replies, or quoted tweets).

## Legal

Use responsibly and follow X/Twitter’s Terms of Service. Only scrape content you are allowed to access.