from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests
import difflib
import heapq
import re

NOT_FRIENDLY_DOMAINS = [
    'soundcloud', 'bandcamp', 'imdb', 'cnn', 'bbc', 'nytimes', 'reuters', 'bloomberg', 'forbes', 'wikimedia', 'nvidia',
    'trello', 'paypal', 'stripe', 'shopify', 'ebay', 'aliexpress', 'amazon', 'netflix', 'spotify', 'twitch', 'vimeo',
    'pinterest', 'reddit', 'tumblr', 'quora', 'medium', 'meetup', 'google', 'apple', 'microsoft', 'amazon', 'adobe',
    'facebook', 'linkedin', 'instagram', 'discord', 'twitter', 'youtube', 'tiktok', 't.me', 'whatsapp', 'snapchat',
    'amd', 'intel', 'steam', 'epicgames', 'ea.com', 'ubisoft', 'aws.amazon', 'azure', 'cloudflare', 'digitalocean',
    'oracle', 'ibm', 'salesforce', 'zoom', 'github', 'gitlab', 'bitbucket', 'stackoverflow', 'jira', 'confluence',
    'heroku', 'office.com', 'gsuite', 'dropbox', 'box.com', 'evernote', 'notion.so', 'maps', 'map', 'ads', 'mail'
]

NOT_FRIENDLY_PATHS = [
    '/kontakt', '/support', '/help', '/faq', '/feedback', '/privacy', '/privacy-policy', '/terms', '/terms-of-service',
    '/gallery', '/portfolio', '/search', '/sitemap', '/rss', '/feed', '/api', '/developers', '/docs', '/documentation',
    '/subscribe', '/newsletter', '/campaign', '/promo', '/special-offer', '/discount', '/download', '/uploads', '/nas',
    '/registrace', '/klienty', '/pro-zakazniky', '/podpora', '/obchodni-podminky', '/ochrana-osobnich-udaju', 'reset',
    '/order', '/payment', '/shipping', '/delivery', '/post', '/article', '/blog', '/news', '/press', '/media', '/app',
    '/admin', '/dashboard', '/settings', '/preferences', '/share', '/print', '/mobile', '/widget', '/embed', '/o-nas',
    '/tos', '/legal', '/copyright', '/dmca', '/about-us', '/team', '/staff', '/company', '/corporate', '/our-story',
    '/history', '/mission', '/vision', '/ad', '/language', '/region', '/country', '/cart', '/checkout', '/basket',
    '/profile', '/password', '/kariera', '/forgot-password', '/verify', '/confirmation', '/contacts', '/contact',
    '/about', '/login', '/logout', '/signin', '/signout', '/register', '/registration', '/signup', '/account'
]

IGNORED_EXTENSIONS_RE = re.compile(
    r"\.(?:pdf|docx|xlsx|png|jpeg|gif|zip|rar|7z|tar|gz|exe|mp4|mp3|avi|mkv|html|php|aspx|htm)", re.IGNORECASE)

WEIGHTS = {
    'depth': -0.025, # Penalty for deep depth of links
    'external_link': 0.15, # Boost for external links
    'path': -0.05,  # Penalty for long path in link
    'tld_match': 0.2 # Boost for matching TLD
}

def is_friendly_domain(netloc):
    return not any(domain in netloc for domain in NOT_FRIENDLY_DOMAINS)


def is_ignored_file(url):
    return bool(IGNORED_EXTENSIONS_RE.search(url))


def clean_url(url):
    scheme, netloc, path, *_ = urlparse(url)

    path = path.rstrip('/')
    netloc = netloc.removeprefix('www.')

    if any(ending in path for ending in NOT_FRIENDLY_PATHS):
        path = ''

    return scheme, netloc, path


def url_similarity(current_url, target_url):
    current_domain = urlparse(current_url).netloc
    target_domain = urlparse(target_url).netloc
    return difflib.SequenceMatcher(None, current_domain, target_domain).ratio()


def calculate_priority(link, depth, current_tld, target_tld, start_tld, target_url):
    priority = 0.0

    if current_tld == target_tld:
        priority += WEIGHTS['tld_match']

    if current_tld != target_tld and current_tld != start_tld:
        priority += WEIGHTS['external_link']

    if current_tld == start_tld and current_tld != target_tld:
        priority -= WEIGHTS['tld_match'] / 2

    return (priority
            + (link.count('/') - 1) * WEIGHTS['path']
            + WEIGHTS['depth'] * depth
            + url_similarity(link, target_url))


def get_all_links(url, depth, target_url, target_domain, start_url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return False, []
        soup = BeautifulSoup(response.text, "lxml")
    except Exception as e:
        return False, []

    # Check language (should start with 'en' or 'cs')
    html_tag = soup.find('html')
    lang = html_tag.get('lang', '') if html_tag else ''
    if not lang.startswith(('en', 'cs')) and lang != '':
        return False, []

    links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']

        # Only process http and https links
        if href.startswith("http://") or href.startswith("https://"):
            scheme, netloc, path = clean_url(urljoin(url, href))

            if netloc == target_domain:
                print('Target found!')
                return True, [target_url]

            if is_friendly_domain(netloc) and not is_ignored_file(path):
                current_tld = netloc.split('.')[-1]
                target_tld = urlparse(target_url).netloc.split('.')[-1]
                start_tld = urlparse(start_url).netloc.split('.')[-1]
                link = f"http://{netloc}{path}"

                priority = calculate_priority(link, depth, current_tld, target_tld, start_tld, target_url)
                links.append((-priority, link))

    return False, links


def heuristic_search(start_url, target_url, target_domain, max_depth=20):
    priority_queue = []
    heapq.heappush(priority_queue, (-0, start_url, 0))

    visited = {start_url}
    parent_map = {}

    while priority_queue:
        # Get the next URL with the highest priority (lowest value)
        _, current_url, depth = heapq.heappop(priority_queue)

        if depth == max_depth:
            continue

        # Get all relevant links on the current page
        ret_val, links = get_all_links(current_url, depth, target_url, target_domain, start_url)

        if ret_val:
            # Target found, reconstruct the path
            path = [target_url, current_url]
            while current_url in parent_map:
                current_url = parent_map[current_url]
                path.append(current_url)

            path.reverse()
            print(" -> ".join(path))
            return

        for priority, link in links:
            if link not in visited:
                visited.add(link)
                heapq.heappush(priority_queue, (priority, link, depth + 1))
                parent_map[link] = current_url

    print("Target not found within the given links.")


def main():
    start = "https://www.fit.cvut.cz"
    target = "https://www.mit.edu"

    heuristic_search(
        start,
        target,
        urlparse(target).netloc.removeprefix('www.')
    )


if __name__ == "__main__":
    main()
