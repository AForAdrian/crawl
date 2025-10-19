COMP 1405Z Web Crawler and Search Engine Project

Student Name: [Your Name Here]
Student ID: [Your Student ID Here]

Project Description:
This project implements a web crawler and search engine with three main modules:
- crawler.py: Performs web crawling starting from a seed URL
- searchdata.py: Provides access to crawled data and computed metrics
- search.py: Implements search functionality using vector space model

Files Included:
- crawler.py: Main crawling module
- searchdata.py: Data access module
- search.py: Search module
- matmult.py: Matrix operations for PageRank calculations
- webdev.py: HTML fetching utility (provided)
- analysis_report.md: Implementation analysis and complexity report
- README.txt: This file

How to Run:

1. Web Crawling:
   python3 crawler.py
   Note: The crawler.crawl() function is typically called from test files

2. Testing:
   Run the provided test files to verify functionality:
   - python3 tinyfruits-all-test.py
   - python3 fruits25-all-test.py
   - python3 fruits50-all-test.py
   - python3 fruits100-all-test.py

3. Manual Testing:
   Start crawling from any of the provided seed URLs:
   - https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html
   - https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
   - https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
   - https://people.scs.carleton.ca/~avamckenney/fruits100/N-0.html

Implementation Notes:
- The crawler performs preprocessing during crawl to optimize search performance
- All data is stored in JSON files for efficient access
- PageRank uses alpha=0.1 and converges when Euclidean distance < 0.0001
- Search uses TF-IDF weighting with cosine similarity
- Optional PageRank boosting available for search results

Technical Details:
- Python 3.x required
- Only uses allowed modules: os, json, math, and webdev.py
- No regular expressions used for parsing
- Handles both absolute and relative URLs
- Processes only content within <p> tags for word extraction
