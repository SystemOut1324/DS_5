# DS_5 - "Politics and Conflict" spider
> Scrapes articles from "Politics and Conflict" with a specific starting charater (A-Z) chosen by changing group_nr.


## Usage

To install you need scrapy

```sh
pip install scrapy
```
Download repo and navigate to it with the terminal. From the terminal you can run any spider written in wikiSpider.py. The default spider is "wiki"

To run wiki-spider with output.csv write:
```sh
scrapy crawl wiki -o output.csv
```

## General usage

The wiki-spider is setup to only get the first article for each 200-link-page as well as all metadata besides content. This can be changed in wikiSpider.py

| Command | Description | Description |
| --- | --- | --- |
| `git status` | List all *new or modified* files |
| `git diff` | Show file differences that **haven't been** staged |
