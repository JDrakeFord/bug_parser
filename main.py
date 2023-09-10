import json
from collections import OrderedDict
from bs4 import BeautifulSoup

bug_info_dict = OrderedDict()

json_list = []

for i in range(1, 200):
    try:
        with open(str(i) + ".html") as fp:
            soup = BeautifulSoup(fp, 'html.parser')
        try:
            roots = soup.find('div', {'class': 'bgpage-roots'})
            for root in roots.select('a'):
                if root.has_attr('title'):
                    tag_title = root['title']
                    tag_title = tag_title.replace(u'\xa0', u' ')
                    contents = root.text
                    contents = contents.replace(u'\xa0', u' ')
                    bug_info_dict[tag_title.encode('utf-8')] = contents.encode('utf-8')

            image = soup.find('img', {'class': 'bgimage-image'})['src']
            bug_info_dict['image_url'] = image
            json_list.append(bug_info_dict)
        except:
            continue
    except:
        continue
with open('info.json', 'w') as outfile:
    outfile.write(json.dumps(json_list, indent=4))
