import os
import json
import math
import matmult

# Global variables to cache loaded data
_pages_data = None
_incoming_links = None
_outgoing_links = None
_page_rank_cache = None
_idf_cache = None
_tf_cache = None

def _load_pages_data():
    """Load pages data from JSON file"""
    global _pages_data
    if _pages_data is None and os.path.exists('pages_data.json'):
        with open('pages_data.json', 'r') as f:
            _pages_data = json.load(f)
    return _pages_data or {}


def _load_incoming_links():
    """Load incoming links data from JSON file"""
    global _incoming_links
    if _incoming_links is None and os.path.exists('incoming_links.json'):
        with open('incoming_links.json', 'r') as f:
            _incoming_links = json.load(f)
    return _incoming_links or {}


def _load_outgoing_links():
    """Load outgoing links data from JSON file"""
    global _outgoing_links
    if _outgoing_links is None and os.path.exists('outgoing_links.json'):
        with open('outgoing_links.json', 'r') as f:
            _outgoing_links = json.load(f)
    return _outgoing_links or {}


def get_outgoing_links(URL):
    """
    Returns a list of URLs that the page with the given URL links to.
    Returns absolute URLs, or None if URL not found.

    Args:
        URL (str): The URL to get outgoing links for

    Returns:
        list or None: List of absolute URLs or None if not found
    """
    outgoing = _load_outgoing_links()
    return outgoing.get(URL)


def get_incoming_links(URL):
    """
    Returns a list of URLs that link to the page with the given URL.
    Returns absolute URLs, or None if URL not found.

    Args:
        URL (str): The URL to get incoming links for

    Returns:
        list or None: List of absolute URLs or None if not found
    """
    incoming = _load_incoming_links()
    return incoming.get(URL)


def get_page_rank(URL):
    """
    Returns the PageRank value for the given URL using alpha=0.1.
    Returns -1 if URL not found.

    Args:
        URL (str): The URL to get PageRank for

    Returns:
        float: PageRank value or -1 if not found
    """
    global _page_rank_cache

    # Load cached PageRank data if available
    if _page_rank_cache is None:
        if os.path.exists('page_rank.json'):
            with open('page_rank.json', 'r') as f:
                _page_rank_cache = json.load(f)
        else:
            # Compute PageRank for all pages
            _page_rank_cache = _compute_page_ranks()
            # Save for future use
            with open('page_rank.json', 'w') as f:
                json.dump(_page_rank_cache, f)

    return _page_rank_cache.get(URL, -1)


def _compute_page_ranks():
    """
    Compute PageRank for all pages using the PageRank algorithm.
    Uses alpha=0.1 and stops when Euclidean distance < 0.0001.

    Returns:
        dict: URL -> PageRank value mapping
    """
    pages_data = _load_pages_data()
    outgoing_links = _load_outgoing_links()

    if not pages_data:
        return {}

    # Create URL to index mapping for matrix operations
    urls = list(pages_data.keys())
    url_to_idx = {url: i for i, url in enumerate(urls)}
    n = len(urls)

    # Build adjacency matrix (transition matrix)
    # M[i][j] = 1/outdegree(i) if i links to j, else 0
    M = [[0.0 for _ in range(n)] for _ in range(n)]

    for i, url_i in enumerate(urls):
        out_links = outgoing_links.get(url_i, [])
        out_degree = len(out_links)

        if out_degree == 0:
            # Dangling node - distribute equally to all pages
            for j in range(n):
                M[j][i] = 1.0 / n
        else:
            for url_j in out_links:
                if url_j in url_to_idx:
                    j = url_to_idx[url_j]
                    M[j][i] = 1.0 / out_degree

    # PageRank parameters
    alpha = 0.1
    epsilon = 0.0001

    # Initialize PageRank vector (equal probability for all pages)
    pr_old = [1.0 / n] * n
    pr_new = [0.0] * n

    # Iterate until convergence
    while True:
        # pr_new = alpha * (1/n * ones) + (1-alpha) * M * pr_old
        # This is equivalent to: pr_new = alpha/n + (1-alpha) * M * pr_old

        # Compute M * pr_old
        m_pr = matmult.matvecmult(M, pr_old)

        # Apply PageRank formula
        for i in range(n):
            pr_new[i] = alpha / n + (1 - alpha) * m_pr[i]

        # Check convergence (Euclidean distance)
        diff_sum = sum((pr_new[i] - pr_old[i]) ** 2 for i in range(n))
        distance = math.sqrt(diff_sum)

        if distance < epsilon:
            break

        # Swap for next iteration
        pr_old, pr_new = pr_new, pr_old

    # Return as dictionary
    return {urls[i]: pr_new[i] for i in range(n)}


def get_idf(word):
    """
    Returns the inverse document frequency of the word.
    IDF = log(Total # Documents / (1 + (# of documents w appears in)))

    Args:
        word (str): The word to get IDF for

    Returns:
        float: IDF value (minimum 0)
    """
    global _idf_cache

    # Load cached IDF data if available
    if _idf_cache is None:
        if os.path.exists('idf_data.json'):
            with open('idf_data.json', 'r') as f:
                _idf_cache = json.load(f)
        else:
            # Compute IDF for all words
            _idf_cache = _compute_idf_values()
            # Save for future use
            with open('idf_data.json', 'w') as f:
                json.dump(_idf_cache, f)

    return _idf_cache.get(word, 0.0)


def _compute_idf_values():
    """
    Compute IDF values for all words in the corpus.

    Returns:
        dict: word -> IDF value mapping
    """
    pages_data = _load_pages_data()

    if not pages_data:
        return {}

    # Count total documents and documents containing each word
    total_docs = len(pages_data)
    word_doc_count = {}

    for url, data in pages_data.items():
        words = data.get('words', [])
        unique_words = set(words)  # Only count once per document

        for word in unique_words:
            word_doc_count[word] = word_doc_count.get(word, 0) + 1

    # Compute IDF for each word
    idf_values = {}
    for word, doc_count in word_doc_count.items():
        idf = math.log(total_docs / (1 + doc_count), 2)  # log base 2
        idf_values[word] = max(0, idf)  # Ensure non-negative

    return idf_values


def get_tf(URL, word):
    """
    Returns the term frequency of the word in the given URL.
    TF = # occurrences of word in document / total # words in document

    Args:
        URL (str): The URL of the document
        word (str): The word to get TF for

    Returns:
        float: TF value or 0 if word not in document or URL not found
    """
    pages_data = _load_pages_data()

    if URL not in pages_data:
        return 0.0

    words = pages_data[URL].get('words', [])
    if not words:
        return 0.0

    word_count = words.count(word)
    total_words = len(words)

    return word_count / total_words


def get_tf_idf(URL, word):
    """
    Returns the TF-IDF weight for the word in the given URL.
    TF-IDF = log(1 + TF) * IDF

    Args:
        URL (str): The URL of the document
        word (str): The word to get TF-IDF for

    Returns:
        float: TF-IDF weight
    """
    tf = get_tf(URL, word)
    idf = get_idf(word)

    return math.log(1 + tf, 2) * idf  # log base 2
