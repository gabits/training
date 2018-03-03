def domain_name(url):
    url = [url[:i] for i in range(len(url) + 1) if url[i:i+4] == '.com'][0]
    url = url.replace('.', '|') if '.' in url  else url.replace('//', '|').replace('/', '|')
    if '|' in url:
        url = [url[(len(url) - url[::-1].index(i)):] for i in url[::-1] if (i == '|')][0]
    return url

domain_name('https://github.com')