import urllib.request
import json


def get_items(uri):
    items = []
    request = urllib.request.Request(uri)
    request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36")
    request.add_header("Host", "www.smzdm.com")
    entries = json.load(urllib.request.urlopen(request))
    category_str = ""
    for it in entries:
        try:
            channel = it.get('article_channel', '')
            price = it.get('article_price', '无价格')
            category = it['article_category']
            if isinstance(category, dict):
                category_str = category.get('title', '')
            if isinstance(category, list):
                category_str = ",".join(category)

            tags = ', '.join([tag['name'] for tag in it['article_tese_tags'] if tag['name'] != category_str])
            items.append({
                'uid'           : str(it['article_id']),
                'title'         : "%s: %s" % (channel, it['article_title']), 
                'subtitle'      : "%s【%s, %s】" % (price, category_str, tags),
                'arg'           : it['article_url'], 
                'description'   : "test",
                'icon'          : 'icon.png',
            })
        except:
            pass

    return json.dumps({"items": items})

#if __name__ == '__main__':
#    print(get_items("http://www.smzdm.com/json_more?timesort=120212735313"))
