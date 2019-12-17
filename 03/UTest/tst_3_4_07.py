import unittest
from ex_3_4_07 import Sites
from unittest.mock import patch


# import sys


class TestCase_3_4_07(unittest.TestCase):
    def setUp(self):
        # print('Current path: ', sys.path)
        self._fileName = '../src/ex_3_4_07_sites_01.txt'
        self._urlPastebin = 'http://pastebin.com/raw/7543p0ns'

    # def test_getList(self):
    #     Expected = ['mail.ru',
    #                 'neerc.ifmo.ru',
    #                 'stepic.org',
    #                 'www.ya.ru',
    #                 'ya.ru', ]
    #     Actual = Sites.getList(self._fileName)
    #     self.assertListEqual(Actual, Expected)

    # def test_getUrls(self):
    #     _inputs = r'<a href="http://stepic.org/courses">' \
    #                r"<a href='https://stepic.org'>" \
    #                r"<a href='http://neerc.ifmo.ru:1345'>" \
    #                r'<a href="ftp://mail.ru/distib" >' \
    #                r'<a href="ya.ru">' \
    #                r'<a href="www.ya.ru">' \
    #                r'<a href="../skip_relative_links">'
    #     Expected = [r'http://stepic.org/courses',
    #                 r"https://stepic.org",
    #                 r"http://neerc.ifmo.ru:1345",
    #                 r'ftp://mail.ru/distib',
    #                 r'ya.ru',
    #                 r'www.ya.ru',
    #                 r'../skip_relative_links']
    #     Actual = Sites.getUrls(_inputs)
    #     self.assertListEqual(Actual, Expected)

    def test_stripHttp(self):
        _inputs = [r'http://stepic.org/courses',
                   r"https://stepic.org",
                   r"http://neerc.ifmo.ru:1345",
                   r'ftp://mail.ru/distib',
                   r'ya.ru',
                   r'www.ya.ru',
                   r'../skip_relative_links']
        Expected = [r'stepic.org/courses',
                    r"stepic.org",
                    r"neerc.ifmo.ru:1345",
                    r'mail.ru/distib',
                    r'ya.ru',
                    r'www.ya.ru',
                    r'../skip_relative_links']
        Actual = []
        for _raw in _inputs:
            Actual.append(Sites.stripHttp(_raw))
        self.assertListEqual(Actual, Expected)

    def test_skipRelative(self):
        _inputs = [r'stepic.org/courses',
                   r"stepic.org",
                   r"neerc.ifmo.ru:1345",
                   r'mail.ru/distib',
                   r'ya.ru',
                   r'www.ya.ru',
                   r'../skip_relative_links',
                   r'../',
                   r'..']
        Expected = [r'stepic.org/courses',
                    r"stepic.org",
                    r"neerc.ifmo.ru:1345",
                    r'mail.ru/distib',
                    r'ya.ru',
                    r'www.ya.ru']
        Actual = []
        for _raw in _inputs:
            if not Sites.skipRelative(_raw):
                Actual.append(_raw)
        self.assertListEqual(Actual, Expected)

    def test_stripWww(self):
        _inputs = [r'stepic.org/courses',
                   r"stepic.org",
                   r"neerc.ifmo.ru:1345",
                   r'mail.ru/distib',
                   r'ya.ru',
                   r'www.ya.ru',
                   r'ta.rbc.ru/',
                   r'../skip_relative_links']
        Expected = [r'stepic.org/courses',
                    r"stepic.org",
                    r"neerc.ifmo.ru:1345",
                    r'mail.ru/distib',
                    r'ya.ru',
                    r'ya.ru',
                    r'ta.rbc.ru/',
                    r'../skip_relative_links']
        Actual = []
        for _raw in _inputs:
            Actual.append(Sites.stripWww(_raw))
        self.assertListEqual(Actual, Expected)

    def test_stripPort(self):
        _inputs = [r'stepic.org/courses',
                   r"neerc.ifmo.ru:1345",
                   r'mail.ru:15487777/distib']
        Expected = [r'stepic.org/courses',
                    r"neerc.ifmo.ru",
                    r'mail.ru/distib']
        Actual = []
        for _raw in _inputs:
            Actual.append(Sites.stripPort(_raw))
        self.assertListEqual(Actual, Expected)

    def test_stripPath(self):
        _inputs = [r'stepic.org/courses',
                   r"stepic.org",
                   r"neerc.ifmo.ru:1345",
                   r'mail.ru/distib',
                   r'ya.ru',
                   r'www.ya.ru',
                   r'adworker.ru/',
                   r'ta.rbc.ru/">',
                   r'../skip_relative_links']
        Expected = [r'stepic.org',
                    r"stepic.org",
                    r"neerc.ifmo.ru:1345",
                    r'mail.ru',
                    r'ya.ru',
                    r'www.ya.ru',
                    r'adworker.ru',
                    r'ta.rbc.ru',
                    r'..']
        Actual = []
        for _raw in _inputs:
            Actual.append(Sites.stripPath(_raw))
        self.assertListEqual(Actual, Expected)

    def test_getFileContent(self):
        Actual = Sites.getFileContent(self._fileName)
        Expected = [r'<a href="http://stepic.org/courses">',
                    r"<a href='https://stepic.org'>",
                    r"<a href='http://neerc.ifmo.ru:1345'>",
                    r'<a href="ftp://mail.ru/distib" >',
                    r'<a href="ya.ru">',
                    r'<a href="www.ya.ru">',
                    r'<a href="../skip_relative_links">']

        self.assertListEqual(Actual, Expected)

    def test_Build(self):
        Expected = ['adworker.ru',
                    'banner.rbc.ru',
                    'biztorg.ru',
                    'blogi.rbc.ru',
                    'cnews.ru',
                    'consensus.rbc.ru',
                    'conv.rbc.ru',
                    'credit.rbc.ru',
                    'data.rbc.ru',
                    'dict.rbc.ru',
                    'drinktime.ru',
                    'events.cnews.ru',
                    'export.rbc.ru',
                    'finolymp.ru',
                    'gift.cnews.ru',
                    'graph.rbc.ru',
                    'magazine.rbc.ru',
                    'map.rbc.ru',
                    'marketing.rbc.ru',
                    'memori.ru',
                    'otc-pif.rbc.ru',
                    'otc-stock.rbc.ru',
                    'pda.rbc.ru',
                    'pogoda.rbc.ru',
                    'portfolio.rbc.ru',
                    'quote-otc.rbc.ru',
                    'quote.ru',
                    'raiting.rbc.ru',
                    'rating.rbc.ru',
                    'realty.rbc.ru',
                    'redir.rbc.ru',
                    'rss.rbc.ru',
                    'seminar.rbc.ru',
                    'spb.rbc.ru',
                    'sport.rbc.ru',
                    'static.feed.rbc.ru',
                    'stock.rbc.ru',
                    'style.rbc.ru',
                    'ta.rbc.ru',
                    'tata.ru',
                    'top.rbc.ru',
                    'top100.rambler.ru',
                    'turbo.ru',
                    'tv.rbc.ru',
                    'ug.rbc.ru',
                    'ulov-umov.ru',
                    'videoarchive.rbc.ru',
                    'www.5ballov.ru',
                    'www.armd.ru',
                    'www.autonews.ru',
                    'www.biztorg.ru',
                    'www.cnews.ru',
                    'www.conf.rbc.ru',
                    'www.event.rbc.ru',
                    'www.iglobe.ru',
                    'www.informer.ru',
                    'www.ivd.ru',
                    'www.liveinternet.ru',
                    'www.m-2.ru',
                    'www.nashidengi.ru',
                    'www.pochta.ru',
                    'www.quote.ru',
                    'www.quoterate.ru',
                    'www.quotetotal.ru',
                    'www.rbc.ru',
                    'www.rbc.ua',
                    'www.rbcdaily.ru',
                    'www.rbcinfosystems.com',
                    'www.rbcnews.com',
                    'www.rbctv.ru',
                    'www.refunder.ru',
                    'www.salon.ru',
                    'www.seminar.rbc.ru',
                    'www.top.rbc.ru',
                    'www.turbo.ru',
                    'www.turist.ru',
                    'www.utro.ru',
                    'www.worldclass.ru',
                    'zoom.cnews.ru﻿', ]
        _user_input = [r'http://pastebin.com/raw/7543p0ns']
        with patch('builtins.input', side_effect=_user_input):
            Actual = Sites.Build()
        self.assertListEqual(Actual, Expected)

    def test_my(self):
        _input = ['http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbc.ru/mainnews.rss',
                  'http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbc.ru/newsline.rss',
                  'http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbcdaily.ru/mainnews.rss',
                  'http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/sport.rbc.ru/newsline.rss',
                  'http://pics.rbc.ru/img/skin/fp_v3/layout_34.css', 'http://pics.rbc.ru/img/skin/fp_v3/skin_34.css',
                  'http://pics.rbc.ru/img/skin/fp_v3/index_34.css',
                  'http://banner.rbc.ru/banredir.cgi?lid=firstpage_spec',
                  'http://www.rbc.ru/je/h9blj5yvau/go?sid=firstpage_end.20090330102319.92601&lid=firstpage_end&id=92601&code=!http%3A%2F%2Fwww.su155.ru%2Fru%2Fservice%2Freg_otd',
                  'http://www.rbc.ru/je/h9blj5yvau/go?sid=firstpage_end.20090330102319.92601&lid=firstpage_end&id=92601&code=!http%3A%2F%2Fwww.su155.ru%2Fru%2Fservice%2Freg_otd',
                  'http://www.rbc.ru/een9ttjayyuag/go?sid=firstpage_top.20090325151427.100154&lid=firstpage_top&id=100154&code=!http%3A%2F%2Fwww.juravli.ru%2F',
                  'http://www.rbcnews.com/', 'http://pda.rbc.ru/', 'http://rss.rbc.ru/', 'http://www.rbc.ru/wap/',
                  'http://memori.ru/link/', 'http://memori.ru/link/?sm=1&u_data[url]=', 'http://www.rbc.ru/home/',
                  'http://www.rbc.ru/advert/rub/', 'http://banner.rbc.ru/banredir.cgi?lid=firstpage_spec_p1',
                  'http://www.pochta.ru', 'http://marketing.rbc.ru', 'http://ulov-umov.ru/?from=rbc',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/', 'http://pogoda.rbc.ru/',
                  'http://www.informer.ru/', 'http://tv.rbc.ru/', 'http://rating.rbc.ru/', 'http://realty.rbc.ru/',
                  'http://www.m-2.ru/', 'http://seminar.rbc.ru/', 'http://www.turist.ru/', 'http://style.rbc.ru/',
                  'http://www.top.rbc.ru', 'http://top.rbc.ru/economics/', 'http://top.rbc.ru/incidents/',
                  'http://top.rbc.ru/politics/', 'http://top.rbc.ru/society/', 'http://top.rbc.ru/retail/',
                  'http://sport.rbc.ru/', 'http://banner.rbc.ru/banredir.cgi?lid=firstpage_left',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.cnews.ru', 'http://www.rbctv.ru/live/',
                  'http://blogi.rbc.ru/', 'http://top.rbc.ru/moscow/', 'http://spb.rbc.ru/', 'http://ug.rbc.ru/',
                  'http://www.rbc.ua/', 'http://www.rbc.ru/fnews.frame/',
                  'http://www.rbc.ru/info/tek/info_rbc_tek_rbc.shtml', 'http://www.rbc.ru/rbcnews.frame/',
                  'http://www.rbc.ru/fondnews.frame/', 'http://www.rbc.ru/digest/',
                  'http://www.quote.ru/analitics/comments/index.shtml?list_all', 'http://www.rbc.ru/consultant/',
                  'http://www.rbc.ru/cur_lnd.shtml', 'http://www.rbc.ru/garantnews/', 'http://www.rbc.ru/calendar/',
                  'http://www.rbc.ru/eel9c/jd2yzmanq/to?sid=firstpage_left2.20090323114212.99996&lid=firstpage_left2&id=99996&code=!http%3A%2F%2Fwww.livemontenegro.ru%2F%3Fid%3Drbc',
                  'http://www.rbc.ru/eel9c/jd2yzmanq/to?sid=firstpage_left2.20090323114212.99996&lid=firstpage_left2&id=99996&code=!http%3A%2F%2Fwww.livemontenegro.ru%2F%3Fid%3Drbc',
                  'http://www.rbc.ru/cur/', 'http://stock.rbc.ru/demo/cb.0/intraday/',
                  'http://stock.rbc.ru/demo/forex.9/intraday/index.rus.shtml', 'http://consensus.rbc.ru/forex/',
                  'http://www.rbc.ru/cash', 'http://www.rbc.ru//info/info_mbkonline_pressr.shtml',
                  'http://credit.rbc.ru/', 'http://www.quote.ru/', 'http://www.quote.ru/', 'http://www.quote.ru/mf/',
                  'http://quote.ru/bonds/', 'http://www.quote.ru/exchanges/',
                  'http://stock.rbc.ru/online/rusindex.0/intraday/index.rus.shtml', 'http://www.quote.ru/weekly/',
                  'http://www.quote.ru/stocks/base_emitent.shtml', 'http://www.quote.ru/research/',
                  'http://www.rbc.ru/cur/macro.shtml', 'http://www.quote.ru/fa/',
                  'http://www.quote.ru/research/comments/index.shtml?list_all', 'http://www.rbc.ru/reviews/',
                  'http://www.rbc.ru/services/', 'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://map.rbc.ru',
                  'http://export.rbc.ru/', 'http://conv.rbc.ru/', 'http://www.quote.ru/commodities/',
                  'http://www.biztorg.ru/', 'http://www.biztorg.ru/search.shtml?cfg=biztorg&type=S',
                  'http://biztorg.ru/franchise.shtml', 'http://biztorg.ru:80/main_services_new.shtml',
                  'http://realty.rbc.ru/', 'http://realty.rbc.ru/', 'http://realty.rbc.ru/msk/business/map/',
                  'http://realty.rbc.ru/foreign/', 'http://www.rbcdaily.ru/', 'http://magazine.rbc.ru/',
                  'http://www.nashidengi.ru/', 'http://www.m-2.ru/', 'http://www.autonews.ru/magazine/',
                  'http://www.salon.ru/', 'http://www.ivd.ru/',
                  'http://banner.rbc.ru/banredir.cgi?lid=firstpage_spec_2',
                  'http://top.rbc.ru/society/30/03/2009/290885.shtml',
                  'http://top.rbc.ru/society/30/03/2009/290885.shtml',
                  'http://top.rbc.ru/society/30/03/2009/290885.shtml',
                  'http://top.rbc.ru/society/30/03/2009/290997.shtml',
                  'http://top.rbc.ru/economics/30/03/2009/290964.shtml',
                  'http://top.rbc.ru/economics/30/03/2009/290922.shtml',
                  'http://top.rbc.ru/economics/30/03/2009/290917.shtml',
                  'http://top.rbc.ru/politics/30/03/2009/290910.shtml',
                  'http://top.rbc.ru/politics/30/03/2009/290864.shtml',
                  'http://top.rbc.ru/incidents/30/03/2009/290856.shtml',
                  'http://top.rbc.ru/economics/30/03/2009/290847.shtml',
                  'http://top.rbc.ru/society/30/03/2009/290845.shtml',
                  'http://top.rbc.ru/incidents/30/03/2009/290835.shtml', 'http://magazine.rbc.ru/economist/',
                  'http://turbo.ru', 'http://raiting.rbc.ru', 'http://top.rbc.ru/',
                  'http://top.rbc.ru/finances/30/03/2009/290951.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290939.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290911.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290890.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290873.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290841.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290830.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290799.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290793.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290790.shtml', 'http://top.rbc.ru/finances/',
                  'http://top.rbc.ru/politics/30/03/2009/290779.shtml',
                  'http://top.rbc.ru/politics/30/03/2009/290663.shtml',
                  'http://top.rbc.ru/politics/30/03/2009/290654.shtml',
                  'http://top.rbc.ru/politics/30/03/2009/290655.shtml',
                  'http://top.rbc.ru/politics/29/03/2009/290573.shtml',
                  'http://top.rbc.ru/politics/29/03/2009/290553.shtml',
                  'http://top.rbc.ru/politics/29/03/2009/290535.shtml',
                  'http://top.rbc.ru/politics/29/03/2009/290533.shtml',
                  'http://top.rbc.ru/politics/29/03/2009/290515.shtml', 'http://top.rbc.ru/politics/',
                  'http://top.rbc.ru/society/30/03/2009/290885.shtml',
                  'http://top.rbc.ru/society/30/03/2009/290885.shtml',
                  'http://top.rbc.ru/society/30/03/2009/290885.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290967.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290967.shtml',
                  'http://top.rbc.ru/finances/30/03/2009/290967.shtml',
                  'http://top.rbc.ru/politics/30/03/2009/290825.shtml',
                  'http://top.rbc.ru/politics/30/03/2009/290825.shtml',
                  'http://top.rbc.ru/politics/30/03/2009/290825.shtml',
                  'http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbcdaily.ru/mainnews.rss',
                  'http://www.rbcdaily.ru/', 'http://www.rbcdaily.ru/', 'http://www.rbcdaily.ru/',
                  'http://www.rbcdaily.ru/index2.html?2009/03/30/focus/408195',
                  'http://www.rbcdaily.ru/index3.html?2009/03/30/focus/408192',
                  'http://www.rbcdaily.ru/index4.html?2009/03/30/focus/408198',
                  'http://www.rbcdaily.ru/index5.html?2009/03/30/lifestyle/408229',
                  'http://www.rbcdaily.ru/index6.html?2009/03/30/media/408188',
                  'http://www.rbc.ru/info/press_20090331.shtml', 'http://quote.ru/',
                  'http://www.rbc.ru/cgi-bin/redirect.cgi?http://video.rbc.ru/top/rinki.wmv', 'http://www.utro.ru/',
                  'http://www.quote.ru/price/price_main.shtml?0', 'http://www.quote.ru/price/price_main.shtml?0',
                  'http://www.quote.ru/price/price_main.shtml?0', 'http://www.rbc.ru/news_fp2.shtml',
                  'http://www.rbc.ru/6ev9q3j/yiga9b/go?sid=firstpage_graph2.20090327192926.100374&lid=firstpage_graph2&id=100374&code=!http%3A%2F%2F9338000.ru%2Fspecial',
                  'http://www.rbc.ru/6ev9q3j/yiga9b/go?sid=firstpage_graph2.20090327192926.100374&lid=firstpage_graph2&id=100374&code=!http%3A%2F%2F9338000.ru%2Fspecial',
                  'http://banner.rbc.ru/banredir.cgi?lid=firstpage_spec_p2', 'http://pogoda.rbc.ru',
                  'http://pogoda.rbc.ru/weather/moscow', 'http://data.rbc.ru/cgi-bin/mk_custom_table.cgi',
                  'http://www.rbc.ru/jehh9b/jujy7ha/0/go?sid=firstpage_graph.default.20090119165909.97005&lid=firstpage_graph&id=97005&code=!http%3A%2F%2Ftionline.ru%2F%3Ffrom%3Dm1',
                  'http://www.rbc.ru/jehh9b/jujy7ha/0/go?sid=firstpage_graph.default.20090119165909.97005&lid=firstpage_graph&id=97005&code=!http%3A%2F%2Ftionline.ru%2F%3Ffrom%3Dm1',
                  'http://www.rbc.ru/kegx9g4jzy9a8/go?sid=focus_fpreg.default.20081009150003.91916&lid=focus_fpreg&id=91916&code=!http%3A%2F%2Fwww.drinktime.ru%2F',
                  'http://www.rbc.ru/kegx9g4jzy9a8/go?sid=focus_fpreg.default.20081009150003.91916&lid=focus_fpreg&id=91916&code=!http%3A%2F%2Fwww.drinktime.ru%2F',
                  'http://www.pochta.ru/?rid=RBC', 'http://www.pochta.ru/regform.php?rid=RBC',
                  'http://marketing.rbc.ru', 'http://marketing.rbc.ru/research/562949956961726.shtml',
                  'http://marketing.rbc.ru/research/562949956961696.shtml',
                  'http://marketing.rbc.ru/research/562949957121077.shtml', 'http://www.armd.ru/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.armd.ru/ru/about_group/new_products_and_services/uslugi/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.armd.ru/ru/about_group/new_products_and_services/po/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.armd.ru/ru/about_group/new_products_and_services/ap/',
                  'http://www.armd.ru/ru/about_group/new_products_and_services/new_upravlenie/',
                  'http://www.seminar.rbc.ru', 'http://seminar.rbc.ru/business/events.shtml?2007/12/13/f98796_03042009',
                  'http://seminar.rbc.ru/business/events.shtml?2008/02/19/f104200_07042009',
                  'http://seminar.rbc.ru/business/events.shtml?2009/02/11/f142778_10042009', 'http://www.event.rbc.ru',
                  'http://www.event.rbc.ru/', 'http://www.conf.rbc.ru', 'http://finolymp.ru/',
                  'http://top.rbc.ru/economics/', 'http://top.rbc.ru/economics/',
                  'http://top.rbc.ru/economics/30/03/2009/290952.shtml',
                  'http://top.rbc.ru/economics/30/03/2009/290952.shtml',
                  'http://top.rbc.ru/economics/30/03/2009/290829.shtml',
                  'http://videoarchive.rbc.ru/archive/2009/03/30/vmz_bz_avtovaz_1500.wmv',
                  'http://top.rbc.ru/economics/30/03/2009/290800.shtml',
                  'http://top.rbc.ru/economics/30/03/2009/290798.shtml',
                  'http://top.rbc.ru/economics/30/03/2009/290791.shtml', 'http://top.rbc.ru/incidents/',
                  'http://top.rbc.ru/incidents/', 'http://top.rbc.ru/incidents/30/03/2009/290824.shtml',
                  'http://top.rbc.ru/incidents/30/03/2009/290824.shtml',
                  'http://videoarchive.rbc.ru/archive/2009/03/30/vmz_bz_gibel_1530.wmv',
                  'http://top.rbc.ru/incidents/30/03/2009/290662.shtml',
                  'http://top.rbc.ru/incidents/29/03/2009/290595.shtml',
                  'http://top.rbc.ru/incidents/29/03/2009/290593.shtml',
                  'http://top.rbc.ru/incidents/29/03/2009/290557.shtml', 'http://sport.rbc.ru/', 'http://sport.rbc.ru',
                  'http://sport.rbc.ru/', 'http://sport.rbc.ru/',
                  'http://sport.rbc.ru/football/article/30/03/2009/229083.shtml',
                  'http://sport.rbc.ru/football/article/30/03/2009/229064.shtml',
                  'http://sport.rbc.ru/football/article/30/03/2009/229063.shtml',
                  'http://sport.rbc.ru/formula/article/29/03/2009/229043.shtml', 'http://www.rbctv.ru/live/',
                  'http://www.rbctv.ru/', 'http://www.rbc.ru/img/flash/mediaplayer.shtml?u10460626dfe',
                  'http://www.rbc.ru/img/flash/mediaplayer.shtml?u10460626dfe',
                  'http://www.rbc.ru/img/flash/mediaplayer.shtml?u10460626dfe',
                  'http://www.rbc.ru/img/flash/mediaplayer.shtml?u1045951bbcb',
                  'http://www.rbc.ru/img/flash/mediaplayer.shtml?u1045951bbcb',
                  'http://www.rbc.ru/img/flash/mediaplayer.shtml?u1045951bbcb',
                  'http://www.rbc.ru/6e4k9qj6vywjaj2/go?sid=firstpage_news.20090327174441.100343&lid=firstpage_news&id=100343&code=!http%3A%2F%2Fhc.ru%2Fcounter%2Freferrer%3Frefgrp%3Drbcmir',
                  'http://www.quote.ru/', 'http://www.quote.ru/', 'http://www.quote.ru/stocks/fond/today_free.shtml',
                  'http://www.quote.ru/stocks/comments/index.shtml?shares',
                  'http://www.quote.ru/stocks/base_emitent.shtml', 'http://www.rbc.ru/info/info_globus.shtml',
                  'http://otc-stock.rbc.ru/targets/index.jsp?skin=newquote&web=1',
                  'http://www.quote.ru/market_leaders.shtml?QUOTE_SHARES_LEADERS_TODAY',
                  'http://www.quote.ru/stocks/ipo/', 'http://www.quote.ru/stocks/merge/', 'http://www.quote.ru/bonds/',
                  'http://www.quote.ru/bonds/oblig_news/', 'http://www.quote.ru/bonds/comments/index.shtml?obligations',
                  'http://www.quote.ru/bonds/calendar/',
                  'http://www.quote.ru/market_leaders.shtml?QUOTE_BONDS_LEADERS_TODAY',
                  'http://www.quote.ru/commodities/', 'http://www.quote.ru/research/', 'http://www.quote.ru/exchanges/',
                  'http://stock.rbc.ru/demo/index.0/intraday/index.rus.shtml',
                  'http://stock.rbc.ru/online/rusindex.0/intraday/index.rus.shtml', 'http://www.quote.ru/mf/',
                  'http://quote-otc.rbc.ru/pif/index.jsp?web=1&skin=quote',
                  'http://quote-otc.rbc.ru/149/index.jsp?skin=quote&web=1',
                  'http://otc-pif.rbc.ru/pif_calculator/calculator.jsp', 'http://www.refunder.ru/',
                  'http://www.quote.ru/conf/', 'http://www.nashidengi.ru', 'http://www.quote.ru/',
                  'http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/quote.ru/mainnews.rss', 'http://www.quote.ru/',
                  'http://www.quote.ru/', 'http://www.quote.ru/bonds/',
                  'http://www.quote.ru/bonds/news.shtml?2009/03/30/32351600', 'http://www.quote.ru/commodities/',
                  'http://www.quote.ru/commodities/news.shtml?2009/03/30/32351265', 'http://www.quote.ru/research/',
                  'http://www.quote.ru/research/news.shtml?2009/03/30/32351413',
                  'http://www.rbc.ru/info/info_rbcdaily-2009.shtml', 'http://www.quote.ru/stocks/fond/',
                  'http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/quote.ru/fondnewsline.rss',
                  'http://www.quote.ru/stocks/fond/index.shtml?2009/03/30/32351594',
                  'http://www.quote.ru/stocks/fond/index.shtml?2009/03/30/32351584',
                  'http://www.quote.ru/stocks/fond/index.shtml?2009/03/30/32351572',
                  'http://www.quote.ru/stocks/fond/index.shtml?2009/03/30/32351553',
                  'http://www.quote.ru/stocks/fond/index.shtml?2009/03/30/32351554',
                  'http://www.quote.ru/stocks/fond/free.shtml',
                  'http://www.quote.ru/stocks/comments/index.shtml?list_all',
                  'http://www.quote.ru/stocks/comments/2009/03/30/32351422.shtml',
                  'http://www.quote.ru/stocks/comments/2009/03/30/32351364.shtml',
                  'http://www.quote.ru/stocks/comments/2009/03/30/32351339.shtml',
                  'http://www.quote.ru/stocks/comments/2009/03/30/32351251.shtml',
                  'http://www.quote.ru/stocks/comments/?list_all_free', 'http://www.quote.ru/price/',
                  'http://credit.rbc.ru/', 'http://credit.rbc.ru/recommendation/potreb/2009/03/30/70820.shtml',
                  'http://credit.rbc.ru/news/other/2009/03/30/70781.shtml',
                  'http://credit.rbc.ru/recommendation/auto/2009/03/26/70657.shtml', 'http://www.rbc.ru/services/',
                  'http://graph.rbc.ru/', 'http://portfolio.rbc.ru/', 'http://export.rbc.ru/', 'http://conv.rbc.ru/',
                  'http://map.rbc.ru/', 'http://ta.rbc.ru/', 'http://www.quotetotal.ru/', 'http://www.quoterate.ru/',
                  'http://map.rbc.ru/', 'http://www.informer.ru/',
                  'http://www.rbc.ru/ie1s9hjqyeday/to?sid=rbc_cnews.20090313163516.99696&lid=rbc_cnews&id=99696&code=!https%3A%2F%2Frbkmoney.ru%2F',
                  'http://www.rbc.ru/ie1s9hjqyeday/to?sid=rbc_cnews.20090313163516.99696&lid=rbc_cnews&id=99696&code=!https%3A%2F%2Frbkmoney.ru%2F',
                  'http://www.cnews.ru/', 'http://www.cnews.ru/cgi-bin/redirect.cgi?http://cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://telecom.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://corp.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://internet.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://safe.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://safe.cnews.ru/bugtrack/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://cnews.ru/reviews/free/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://www.cnews.ru/reviews/rating/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://pr.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://www.cnews.ru/reviews/lib/face/a-b.shtml',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://events.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://zoom.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://gift.cnews.ru',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://rnd.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://tv.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://www.cnews.ru/mag/',
                  'http://cnews.ru/cgi-bin/redirect.cgi?http://cnews.ru/mag/2009/01/', 'http://www.cnews.ru/news/',
                  'http://cnews.ru/rss/', 'http://cnews.ru/podcasts/index.shtml?2009/03/29/342341',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://cnews.ru',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://cnews.ru',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://cnews.ru',
                  'http://www.cnews.ru/news/top/index.shtml?2009/03/30/342412',
                  'http://cnews.ru/news/top/index.shtml?2009/03/30/342401',
                  'http://cnews.ru/news/top/index.shtml?2009/03/30/342383', 'http://www.cnews.ru/reviews/',
                  'http://www.cnews.ru/reviews/index.shtml?2009/03/30/342448',
                  'http://www.cnews.ru/reviews/free/infrastructure2008/articles/ib_system.shtml',
                  'http://www.cnews.ru/reviews/index.shtml?2009/03/27/342223',
                  'http://www.cnews.ru/reviews/free/infrastructure2008/',
                  'http://events.cnews.ru/events/02_04_09.shtml', 'http://zoom.cnews.ru',
                  'http://zoom.cnews.ru/publication/item/16860', 'http://zoom.cnews.ru/publication/item/16840',
                  'http://zoom.cnews.ru/publication/item/16800', 'http://www.cnews.ru/news/',
                  'http://cnews.ru/news/line/index.shtml?2009/03/30/342414',
                  'http://cnews.ru/news/line/index.shtml?2009/03/30/342409',
                  'http://cnews.ru/news/line/index.shtml?2009/03/30/342362', 'http://www.cnews.ru/',
                  'http://zoom.cnews.ru/',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://zoom.cnews.ru/category/item/253',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://zoom.cnews.ru/category/item/208',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://zoom.cnews.ru/category/item/212',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://zoom.cnews.ru/category/item/220',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://zoom.cnews.ru/category/item/216',
                  'http://www.cnews.ru/cgi-bin/redirect.cgi?http://zoom.cnews.ru/category/item/224',
                  'http://zoom.cnews.ru/blog/#9029', 'http://zoom.cnews.ru/blog/', 'http://zoom.cnews.ru/blog/#9029',
                  'http://gift.cnews.ru', 'http://gift.cnews.ru/winter_2009/player/article_3.shtml',
                  'http://gift.cnews.ru/winter_2009/photo/article_1.shtml',
                  'http://gift.cnews.ru/winter_2009/kpk/article_1.shtml',
                  'http://www.rbc.ru/yeh9djjvyd/a5/go?sid=firstpage_cnews.default.20090212123046.98382&lid=firstpage_cnews&id=98382&code=!http%3A%2F%2Fwww.cnews.ru%2Fnews%2Ftop%2Findex.shtml%3F2008%2F12%2F24%2F333185',
                  'http://banner.rbc.ru/banredir.cgi?lid=rbc_intel',
                  'http://banner.rbc.ru/banredir.cgi?lid=rbc_autonews', 'http://www.autonews.ru/sell/index.shtml?new=Y',
                  'http://www.autonews.ru/sell/index.shtml?new=N', 'http://www.autonews.ru/sell/add_sell_offer.shtml',
                  'http://www.autonews.ru/index.shtml', 'http://www.autonews.ru/test_drive/',
                  'http://www.autonews.ru/autobusiness/', 'http://www.autonews.ru/first_look/',
                  'http://www.autonews.ru/luxury_cars/', 'http://www.autonews.ru/events/',
                  'http://www.autonews.ru/catalog/', 'http://www.autonews.ru/models_opinions/',
                  'http://www.autonews.ru/compare/', 'http://www.autonews.ru/salones/index.shtml?ftype=1',
                  'http://www.autonews.ru/salones/index.shtml?ftype=2',
                  'http://www.autonews.ru/salones/index.shtml?servs=10002',
                  'http://www.autonews.ru/salones/index.shtml?servs=10004',
                  'http://www.autonews.ru/salones/index.shtml?servs=10007', 'http://www.turbo.ru/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949957353426.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949957353426.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949956801257.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949956801257.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949956566838.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949956566838.shtml',
                  'http://banner.rbc.ru/banredir.cgi?lid=firstpage_autonews_left', 'http://www.autonews.ru/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/', 'http://www.autonews.ru/',
                  'http://www.autonews.ru/rss/auto_news.xml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459494',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459452',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459434',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonissan.ru/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.nissan-avtogrand.ru/news/news.php?id=40',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.lexusnm.ru/',
                  'http://www.autonews.ru/automarket_news/', 'http://www.autonews.ru/rss/auto_news.xml',
                  'http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459674',
                  'http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459672',
                  'http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459662',
                  'http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459657',
                  'http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459654',
                  'http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459643',
                  'http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459595',
                  'http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459615', 'http://www.autonews.ru',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949953866020.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949953866020.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949955004758.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turbo.ru/legend/562949955004758.shtml',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turist.ru/goods/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turist.ru/goods/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turist.ru/goods/',
                  'http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turist.ru/goods/',
                  'http://banner.rbc.ru/banredir.cgi?lid=firstpage', 'http://www.worldclass.ru/', 'http://turbo.ru/',
                  'http://drinktime.ru', 'http://www.m-2.ru', 'http://tata.ru', 'http://magazine.rbc.ru/',
                  'http://adworker.ru/', 'http://www.5ballov.ru/', 'http://www.iglobe.ru/', 'http://dict.rbc.ru/',
                  'http://banner.rbc.ru/banredir.cgi?lid=firstpage_bot', 'http://www.quote.ru/price/',
                  'http://www.rbcinfosystems.com/', 'http://www.rbc.ru/dow_jones.shtml',
                  'http://www.rbc.ru/reuters.shtml', 'http://www.rbc.ru/ap.shtml', 'http://www.rbc.ru/comstock.shtml',
                  'http://www.rbc.ru/privacy.shtml', 'http://www.rbc.ru/advert/',
                  'http://top100.rambler.ru/top100/All/rate21.0.shtml.ru', 'http://www.liveinternet.ru/click']


def create_suite(classes, unit_tests_to_run):
    suite = unittest.TestSuite()
    for _class in classes:
        _object = _class()
        for _method in unit_tests_to_run:
            suite.addTest(_class(_method))
    return suite

    # unit_tests_to_run_count = len(unit_tests_to_run)
    # for _class in classes:
    #     _object = _class()
    #     for function_name in dir( _object ):
    #         if function_name.lower().startswith( "test" ):
    #             if unit_tests_to_run_count > 0 \
    #                     and function_name not in unit_tests_to_run:
    #                 continue
    #             suite.addTest( _class( function_name ) )
    # return suite


def run_unit_tests():
    runner = unittest.TextTestRunner()
    classes = ['TestCase_3_4_07']
    methods = ['test_getFileContent']
    runner.run(create_suite(classes, methods))


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(TestCase_3_4_07.test_getFileContent())
# suite = unittest.TestSuite()
# suite.addTest(TestCase_3_4_07('test_getFileContent'))
# unittest.TestSuite.run(suite)

# if __name__ == "__main__":
#     print("\n\n")
#     run_unit_tests()