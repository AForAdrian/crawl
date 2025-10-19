import os
import json
import webdev

def crawl(seed):
    """
    Performs web crawling starting from the seed URL.
    Finds all reachable pages, saves crawl data to files, and returns page count.

    Args:
        seed (str): The starting URL for the crawl

    Returns:
        int: Number of pages found during the crawl
    """
    # Reset any existing data by deleting previous crawl files
    _reset_crawl_data()

    # Initialize data structures
    pages_data = {}  # URL -> {'title': str, 'words': list, 'outgoing_links': list}
    visited = set()
    to_visit = [seed]
    incoming_links = {}  # URL -> list of URLs that link to it

    # Perform BFS crawl
    while to_visit:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        visited.add(current_url)

        # Fetch page content
        page_content = webdev.read_url(current_url)
        if not page_content:
            continue

        # Parse page content
        title, words, outgoing_links = _parse_page(page_content)

        # Convert relative links to absolute
        absolute_outgoing = []
        for link in outgoing_links:
            abs_link = _to_absolute_url(link, current_url)
            absolute_outgoing.append(abs_link)

            # Track incoming links
            if abs_link not in incoming_links:
                incoming_links[abs_link] = []
            if current_url not in incoming_links[abs_link]:
                incoming_links[abs_link].append(current_url)

        # Store page data
        pages_data[current_url] = {
            'title': title,
            'words': words,
            'outgoing_links': absolute_outgoing
        }

        # Add unvisited links to queue
        for link in absolute_outgoing:
            if link not in visited and link not in to_visit:
                to_visit.append(link)

    # Initialize incoming links for pages that have no incoming links
    for url in pages_data:
        if url not in incoming_links:
            incoming_links[url] = []

    # Save all data to files
    _save_crawl_data(pages_data, incoming_links)

    return len(pages_data)


def _reset_crawl_data():
    """Delete all previous crawl data files"""
    files_to_remove = [
        'pages_data.json',
        'incoming_links.json',
        'outgoing_links.json',
        'page_rank.json',
        'idf_data.json',
        'tf_data.json'
    ]

    for filename in files_to_remove:
        if os.path.exists(filename):
            os.remove(filename)


def _parse_page(content):
    """
    Parse HTML content to extract title, words from <p> tags, and outgoing links.

    Args:
        content (str): Raw HTML content

    Returns:
        tuple: (title, words_list, outgoing_links_list)
    """
    title = _extract_title(content)
    words = _extract_words(content)
    outgoing_links = _extract_links(content)

    return title, words, outgoing_links


def _extract_title(content):
    """Extract title from <title> tags"""
    start_tag = '<title>'
    end_tag = '</title>'

    start_idx = content.find(start_tag)
    if start_idx == -1:
        return ""

    start_idx += len(start_tag)
    end_idx = content.find(end_tag, start_idx)
    if end_idx == -1:
        return ""

    return content[start_idx:end_idx].strip()


def _extract_words(content):
    """Extract words from <p> tags"""
    words = []
    start_pos = 0

    while True:
        # Find next <p> tag
        p_start = content.find('<p>', start_pos)
        if p_start == -1:
            break

        p_start += 3  # Skip <p>

        # Find corresponding </p>
        p_end = content.find('</p>', p_start)
        if p_end == -1:
            break

        # Extract text between <p> and </p>
        p_content = content[p_start:p_end]

        # Split into words (by spaces and newlines)
        p_words = p_content.replace('\n', ' ').split()
        words.extend(p_words)

        start_pos = p_end + 4  # Skip </p>

    return words


def _extract_links(content):
    """Extract outgoing links from <a href="..."> tags"""
    links = []
    start_pos = 0

    while True:
        # Find next <a tag
        a_start = content.find('<a', start_pos)
        if a_start == -1:
            break

        # Find href="
        href_start = content.find('href="', a_start)
        if href_start == -1:
            start_pos = a_start + 2
            continue

        href_start += 6  # Skip href="

        # Find closing "
        href_end = content.find('"', href_start)
        if href_end == -1:
            start_pos = a_start + 2
            continue

        # Extract link
        link = content[href_start:href_end]
        links.append(link)

        start_pos = href_end + 1

    return links


def _to_absolute_url(link, base_url):
    """
    Convert relative URLs to absolute URLs.

    Args:
        link (str): The link to convert
        base_url (str): The base URL for relative links

    Returns:
        str: Absolute URL
    """
    if link.startswith('https://'):
        return link

    if not link.startswith('./'):
        # This shouldn't happen according to spec, but handle gracefully
        return link

    # Remove leading ./
    relative_path = link[2:]

    # Find the base URL up to the last /
    last_slash = base_url.rfind('/')
    if last_slash == -1:
        return base_url + '/' + relative_path

    base_path = base_url[:last_slash + 1]
    return base_path + relative_path


def _save_crawl_data(pages_data, incoming_links):
    """
    Save all crawl data to JSON files for use by searchdata.py

    Args:
        pages_data (dict): URL -> page data mapping
        incoming_links (dict): URL -> list of incoming URLs mapping
    """
    # Save pages data (titles, words, outgoing links)
    with open('pages_data.json', 'w') as f:
        json.dump(pages_data, f)

    # Save incoming links
    with open('incoming_links.json', 'w') as f:
        json.dump(incoming_links, f)

    # Create outgoing links mapping for convenience
    outgoing_links = {}
    for url, data in pages_data.items():
        outgoing_links[url] = data['outgoing_links']

    with open('outgoing_links.json', 'w') as f:
        json.dump(outgoing_links, f)
