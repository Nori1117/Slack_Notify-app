import urllib.request as url_req
from bs4 import BeautifulSoup
from config import config, update_recent_article
from slack_notification import slack_notify

first_view = url_req.urlopen(config['web_info']['url']).read()
soup = BeautifulSoup(first_view, "lxml")

def extract_pick_up(soup=soup):

    #最新記事を抜粋する
    columns = soup.find_all("table" class="propertyTable")
    return columns[0:13]

    def extract_url(column):
    #columns @params: コラム コラムのurlを取得する
    column_html = BeautifulSoup(str(column), "lxml")
    url = column_html.find("a").get("href")
    return url


def extract_title(column):
    #columns @params: コラム コラムのタイトルを取得する
    column_html = BeautifulSoup(str(column), "lxml")
    title = column_html.find("h2").string
    return title

def extract_update_article(columns):
    #更新された記事を抽出 更新前の最新の記事のindexはconfig.iniで管理
    ## 最新の記事番号を取得
    recent_article = config['web_info']['recent_article']
    # 更新された記事のurlを取得
    article_list = []
    update_start = False
    # 逆順に取得していき、最新記事の次からの記事のurlを取得
    for column in reversed(columns):
        url = extract_url(column)
        # 記事番号取得
        table_num = url.replace(config['web_info']['url']+"/", "")

        # タイトル取得
        title = extract_title(column)
        # 取得すべきurl
        if update_start:
            table_list.append([title, url])
            recent_table = table_num
            continue
        # 前回取得した最新の記事かどうか判定
        if recent_table == table_num:
            update_start = True

    # config更新
    update_recent_table(recent_table)
    if table_list == []:
        return [["更新記事はありません", "https://apartner-nakameguro.cbiz.co.jp/list_secret/index-invest.php"]]
    return table_list


if __name__ == "__main__":
    columns = extract_pick_up()
    url = extract_url(columns[0])
    table_list = extract_update_table(columns)
    slack_notify(text_="---投資物件最新記事---", list_=table_list)
