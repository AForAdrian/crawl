import math
import searchdata

def search(phrase, boost):
    """
    Perform search using vector space model and cosine similarity.
    Returns top 10 results sorted by score (descending).

    Args:
        phrase (str): Search query (space-separated words)
        boost (bool): Whether to boost content score by PageRank

    Returns:
        list: Top 10 search results, each as dict with 'url', 'title', 'score'
    """
    # Parse query into words
    query_words = phrase.split()

    if not query_words:
        return []

    # Get all crawled pages
    pages_data = _load_pages_data()
    if not pages_data:
        return []

    urls = list(pages_data.keys())

    # Build query vector (TF-IDF weights for unique words)
    query_vector, unique_query_words = _build_query_vector(query_words)

    # Compute scores for each document
    results = []
    for url in urls:
        # Get document vector (TF-IDF weights for unique query words)
        doc_vector = [searchdata.get_tf_idf(url, word) for word in unique_query_words]

        # Compute cosine similarity
        similarity = _cosine_similarity(query_vector, doc_vector)

        # Apply PageRank boost if requested
        if boost:
            page_rank = searchdata.get_page_rank(url)
            if page_rank == -1:  # URL not found
                page_rank = 0
            similarity *= page_rank

        # Get page title
        title = pages_data[url].get('title', '')

        results.append({
            'url': url,
            'title': title,
            'score': similarity
        })

    # Sort by score descending and return top 10
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:10]


def _load_pages_data():
    """Load pages data (similar to searchdata internal function)"""
    import os
    import json

    if os.path.exists('pages_data.json'):
        with open('pages_data.json', 'r') as f:
            return json.load(f)
    return {}


def _build_query_vector(query_words):
    """
    Build TF-IDF vector for the query.

    For query vector in vector space model:
    - TF = frequency of word in query
    - IDF = same as document IDF
    - Weight = log(1 + TF) * IDF

    Args:
        query_words (list): List of words in query

    Returns:
        tuple: (vector, unique_words)
    """
    if not query_words:
        return [], []

    # Count TF for query
    query_tf = {}
    for word in query_words:
        query_tf[word] = query_tf.get(word, 0) + 1

    # Get unique words in order
    unique_words = list(query_tf.keys())

    # Build TF-IDF vector
    vector = []
    for word in unique_words:
        tf = query_tf[word]
        idf = searchdata.get_idf(word)
        tf_idf = math.log(1 + tf, 2) * idf  # Same formula as documents
        vector.append(tf_idf)

    return vector, unique_words


def _cosine_similarity(vec1, vec2):
    """
    Compute cosine similarity between two vectors.

    Args:
        vec1 (list): First vector
        vec2 (list): Second vector

    Returns:
        float: Cosine similarity (0 to 1)
    """
    if len(vec1) != len(vec2):
        return 0.0

    # Compute dot product
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    # Compute magnitudes
    mag1 = math.sqrt(sum(a * a for a in vec1))
    mag2 = math.sqrt(sum(b * b for b in vec2))

    # Handle zero magnitude vectors
    if mag1 == 0 or mag2 == 0:
        return 0.0

    return dot_product / (mag1 * mag2)
