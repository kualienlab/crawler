from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
keywords = ['cat','dog','person','chair','table','fish','orange','apple','happy','sad','festivals']

for keyword in keywords:
    # google search
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': keyword+'/google'})
    filters = dict(
        type='photo',
        license='commercial,modify')
    google_crawler.crawl(keyword=keyword, language="ús", filters=filters, max_num=1000, file_idx_offset=0)

    # bing search
    bing_crawler = BingImageCrawler(
        downloader_threads=4,
        storage={'root_dir': keyword+'/bing'})
    bingFilters = dict(
        type='photo'
    )
    bing_crawler.crawl(keyword=keyword, filters=bingFilters, offset=0, max_num=1000)

    # baidu search
    baiduFilters = dict(
        type='photo'
    )
    baidu_crawler = BaiduImageCrawler(storage={'root_dir': keyword+'/baidu' })
    baidu_crawler.crawl(keyword=keyword, offset=0, max_num=1000,
                    min_size=(200,200), max_size=None)
