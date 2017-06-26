def check_encoding(filename):
    import chardet
    with open(filename, 'rb') as file:
        data = file.read()
        code_type = chardet.detect(data)
    return(code_type["encoding"])


def read_json_file(filename, code_type):
    import json
    with open(filename, encoding=code_type) as file:
        news = json.load(file)
    return news


def count_top_words(news):
    return sorted(list(set(news)), key=lambda elem: news.count(elem) if len(elem) > 6 else 0, reverse=True)[0:10]


def head_func():
    files_to_read = ["newsafr.json", "newscy.json", "newsfr.json", "newsit.json"]
    for filename in files_to_read:
        news_block = []
        enc = check_encoding(filename)
        for news in read_json_file(filename, enc)["rss"]["channel"]["items"]:
            news_block += news["description"].split()
        top_list = count_top_words(news_block)
        print(top_list)

if __name__ == '__main__':
    head_func()

    # print(news_desc)