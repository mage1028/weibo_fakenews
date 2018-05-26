

agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',

    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",]
    # "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    # "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    # "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    # "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)", ]

from http.cookies import SimpleCookie

str = 'SINAGLOBAL=6052291904347.267.1523584854735; _T_WM=911f60d2fb13c20fc5a50bb11bd447af; YF-Page-G0=b98b45d9bba85e843a07e69c0880151a; YF-V5-G0=3717816620d23c89a2402129ebf80935; _s_tentry=login.sina.com.cn; Apache=786278590073.033.1526887445919; ULV=1526887445971:12:5:1:786278590073.033.1526887445919:1526030864851; YF-Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; WBtopGlobal_register_version=18ecda104816e044; login_sid_t=4277cf0483a3f4f501fc10fe1b6eb7a7; cross_origin_proto=SSL; UOR=www.shangyang.me,widget.weibo.com,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW98Vb6BMxbNWLW24e2R0L55JpX5K2hUgL.FoeNS0nX1K2fSKz2dJLoI0qLxKnLBKzLB-zLxK.L1KBLBKBLxKqL1K.L1K-LxKML1-2L1hBLxK-LBo5L12qLxK.LBonLBK2t; ALF=1558787098; SSOLoginState=1527251099; SCF=AkPjrDiALONXUrpuUXCYEzbwjBowDuhhYFDr5HbhlmcEJSrxZXU6LJkD-zY1dKQoQTZbwPdvHeOg4XJmsRP32ec.; SUB=_2A252DHDMDeRhGeVJ7FoV-S_Jzj6IHXVVeOUErDV8PUNbmtBeLVbskW9NT8RAC5QHxjqmwggVVzQkpkkWvjGVewfv; SUHB=0WGs7C3caTLg2o; un=18066635323; wvr=6'
cookie = SimpleCookie(str)
y = [{i.key: i.value for i in cookie.values()}]
# str2 = 'SINAGLOBAL=6052291904347.267.1523584854735; _T_WM=911f60d2fb13c20fc5a50bb11bd447af; UOR=www.shangyang.me,widget.weibo.com,login.sina.com.cn; _s_tentry=service.account.weibo.com; Apache=5726147549537.581.1526030864769; ULV=1526030864851:11:4:2:5726147549537.581.1526030864769:1525933126469; login_sid_t=f3587bfad48d7997d66596731cc30036; cross_origin_proto=SSL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SwGBuUPQWgY6vLYFjNsLz5JpX5K2hUgL.Foqfe0McSo5pSoB2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcSKeNSoq7eKqX; ALF=1557767927; SSOLoginState=1526231928; SCF=AkPjrDiALONXUrpuUXCYEzbwjBowDuhhYFDr5HbhlmcEa1MmKXF0GtMXwpN-BCdtSjqveVGfLsSctFenBzADO5g.; SUB=_2A253_AMoDeRhGeBL6FUX9i7NzTiIHXVUiHPgrDV8PUNbmtBeLXf9kW9NRw-Y2B_Hbc_nGhXBArSXAVbKv8ylDKO5; SUHB=0h15_17Kiy9Swf; un=13859991449; wvr=6'
# cookie = SimpleCookie(str2)
# z = [{i.key: i.value for i in cookie.values()}]
# cookies={'ALC': 'ac%3D0%26bt%3D1526215237%26cv%3D5.0%26et%3D1557751237%26ic%3D1863639441%26scf%3D%26uid%3D3778491552%26vf%3D0%26vs%3D0%26vt%3D0%26es%3Dd666b15915478b020b6c7a540bf46a0b', 'LT': '1526215237', 'tgc': 'TGT-Mzc3ODQ5MTU1Mg==-1526215237-yf-BF56EBFC1014765C1A73E3E92C36035D-1', 'ALF': '1557751237', 'SCF': 'AkncMef-WFGsIsJewZPQ9dJCvmqE7WsFP5Y0K_6l_4PdLmyOIQDipXcEtt82WUeo8V1ldGYUBtYzu8Sk5mwDrLM.', 'SUB': '_2A253_EIVDeRhGeVJ7FoV-S_Jzj6IHXVUiDTdrDV_PUNbm9ANLVSnkW9NT8RAC1n-DsVlo5jk-E_mt79ZZt-CSgh0', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WW98Vb6BMxbNWLW24e2R0L55NHD95Q0S0MRSh.pSK-EWs4Dqcjci--Ri-2Ei-8Fi--4iK.Xi-2Xi--ciK.4iK.fi--NiKLWiKnXi--fi-z7iKysi--4i-zRi-2p', 'sso_info': 'v02m6alo5qztKWRk6ClkJOIpZCUiKWRk6SljpOQpZCTkKWRk5iljpOkpY6TlKWRk5yljpSEpY6DkKWRk5SlkKOApY6EmKWRk6SlkKOgpZCThKadlqWkj5OMt42zoLSOk4S1jZOIwA==', 'SSO-DBL': '219e4a0617d3288012618552eb672f75'}
