# 2029 KAKAO BLIND
# 6. 매칭 점수
# https://programmers.co.kr/learn/courses/30/lessons/42893

import re
def solution(word, pages):
    n = len(pages)
    websites = {}
    meta_parser = re.compile('<meta (.+?)>')
    title_parser = re.compile('content="https://(.+?)"')
    for i in range(n):
        page = pages[i]
        meta_tags = meta_parser.findall(page)
        for meta_tag in meta_tags:
            titles = title_parser.findall(meta_tag)
            for title in titles:
                websites[title] = {'id': i, 'get_linked': []}

    a_parser = re.compile('<a (.+?)>')
    link_parser = re.compile('href="https://(.+?)"')
    for title in websites.keys():
        website = websites[title]
        page = pages[website['id']]
        a_tags = a_parser.findall(page)
        website['link_number'] = len(a_tags)
        for a_tag in a_tags:
            link = link_parser.findall(a_tag)[0]
            # print(link)
            if link in websites.keys():
                linked_site = websites[link]
                linked_site['get_linked'].append(title)

        word = word.lower()
        page = page.lower()
        website['basic_score'] = re.sub('[^a-z]+', '.', page).split('.').count(word)

    scores = [0] * n
    for title in websites.keys():
        website = websites[title]
        idx = website['id']
        basic_score = website['basic_score']
        linked_score = 0
        if website['get_linked']:
            for site in website['get_linked']:
                linked_score += websites[site]['basic_score'] / websites[site]['link_number']
        scores[idx] = basic_score + linked_score

    max_score = 0
    max_idx = 0
    for i in range(n):
        if scores[i] > max_score:
            max_score = scores[i]
            max_idx = i
    return max_idx

#
#
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution('blind', pages))