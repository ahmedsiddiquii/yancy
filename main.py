"""
Download all ClassDojo photos and videos in your timeline.
by kecebongsoft
How it works:
1. Fetch list of items in the timeline, if there are multiple pages,
   it will fetch for all pages.
2. Collect list of URLs for the attachment for each item
3. Download the files into local temporary directory, and also save
   the timeline activity as a json file.
How to use:
1. Modify the session cookie in this script, check your session cookie
   by opening classdojo in browser and copy the following cookies:
   dojo_log_session_id, dojo_login.sid, and dojo_home_login.sid
2. Run this script and wait for it to finish.
If error happens:
1. I ran this script in windows, make sure your path is correct if you
   are on linux
2. Make sure "classdojo_output" directory exists in the same folder as
   this script
3. Make sure you have a correct session cookies set in this script.
4. Make sure you can open the FEED_URL listed in this script from
   within your browser (assuming you can open ClassDojo website)
"""

import requests
import json
import os
import tempfile

FEED_URL = 'https://home.classdojo.com/api/storyFeed?includePrivate=true'
DESTINATION = tempfile.mkdtemp(dir='classdojo_output') #make sure this directory exists in the same place as this script.
SESSION_COOKIES = {
    'dojo_log_session_id': 'f1b8f575-2a00-435b-a694-f2812ebec778',
    'dojo_login.sid': 's%3A5NOyFXb9NMTlI3_alOQbVzGtH3AQ2xBO.mxgqKh%2FFdk%2B4bFszbSc6EE8n54ysjHwLybKJjjdEOx8',
    'dojo_home_login.sid': 's:5NOyFXb9NMTlI3_alOQbVzGtH3AQ2xBO.mxgqKh/Fdk+4bFszbSc6EE8n54ysjHwLybKJjjdEOx8',
}
NOT_BEFORE = '0000-00-00'  # '2020-08-22'

def get_items(feed_url):
    print('Fetching items: %s ...' % feed_url)
    resp = requests.get(feed_url, cookies=SESSION_COOKIES)
    data = resp.json()
    prev = data.get('_links', {}).get('prev', {}).get('href')

    return data['_items'], prev


def get_contents(feed_url):
    items, prev = get_items(feed_url)
    count=0
    while prev and feed_url != prev:
        prev_urls, prev = get_items(prev)
        items.extend(prev_urls)
        count+=1
        if count==5:
            break

    # Save the JSON data for later/inspection.
    with open(os.path.join(DESTINATION, 'data.json'), 'w') as fd:
        fd.write(json.dumps(items, indent=4))

    contents = []
    total = 0
    for item in items:
        data = item['contents']
        entry = {
            'description': data.get('body'),
            'base_name': None,
            'day': None,
            'attachments': [],
        }
        attachments = data.get('attachments', {})
        if not attachments:
            continue

        for attachment in attachments:
            parts = attachment['path'].split('/')
            day = parts[-3]
            if parts[3] == 'api' or day < NOT_BEFORE:
                continue
            total += 1
            if not entry['base_name']:
                entry['base_name'] = parts[-4]
                entry['day'] = day
            entry['attachments'].append({'name': '_'.join(parts[-2:]),
                                         'url': attachment['path']})

        if entry['base_name']:
            contents.append(entry)

    return contents, total


def download_contents(contents, total):
    index = 0
    highest_day = contents[0]['day']
    for entry in contents:
        description_name = '{}_{}_description.txt'.format(entry['day'],
                                                          entry['base_name'])
        with open(os.path.join(DESTINATION, description_name), 'wt') as fd:
            fd.write(entry['description'])
        for item in entry['attachments']:
            index += 1
            day = entry['day']
            if day > highest_day:
                highest_day = day
            url = item['url']
            filename = os.path.join(DESTINATION,
                                    '{}_{}_{}'.format(entry['day'],
                                                      entry['base_name'],
                                                      item['name']))
            if os.path.exists(filename):
                continue
            print('Downloading {}/{} on {}: {}'
                  .format(index, total, day, item['name']))
            with open(filename, 'wb') as fd:
                resp = requests.get(url, cookies=SESSION_COOKIES)
                fd.write(resp.content)
    print('Last day of data download: {}'.format(highest_day))
    print('Done!')


if __name__ == '__main__':
    print('Starting')
    contents, total = get_contents(FEED_URL)
    download_contents(contents, total)