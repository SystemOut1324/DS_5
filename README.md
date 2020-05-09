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

| Type     | Naming Convention                                                                                               | Examples                                |
| --- | --- | --- |
| Function | Use a lowercase word or words. Separate words by underscores to improve readability.                            | function, my_function                   |
| Variable | Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.          | x, var, my_variable                     |
| Class    | Start each word with a capital letter. Do not separate words with underscores. This style is called camel case. | Model, MyClass                          |
| Method   | Use a lowercase word or words. Separate words with underscores to improve readability.                          | class_method, method                    |
| Constant | Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.         | CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT |
| Module   | Use a short, lowercase word or words. Separate words with underscores to improve readability.                   | module.py, my_module.py                 |
| Package  | Use a short, lowercase word or words. Do not separate words with underscores.                                   | package, mypackage                      |
