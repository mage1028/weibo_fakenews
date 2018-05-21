

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
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)", ]

# from http.cookies import SimpleCookie
#
# str = 'SINAGLOBAL=172.16.118.85_1523584854.870596; SCF=AkPjrDiALONXUrpuUXCYEzbwjBowDuhhYFDr5HbhlmcEGi0780kkGJmk7YHpqEdhzIrIhZ47VVtGuXK-ssrHVOs.; UOR=www.cnblogs.com,v.t,; U_TRS1=00000003.a961350.5adedfa5.786fa820; ULV=1525246115812:1:1:1:117.33.59.151_1525244543.382706:; SGUID=1525246117194_32505117; lxlrttp=1524789408; Apache=111.20.225.134_1526030864.899115; ULOGIN_IMG=gz-9385de74e4e61370257d621911693e9a6032; SUB=_2A253_AQ1DeRhGeBL6FUS8irPyDyIHXVUiHL9rDV_PUNbm9BeLWf2kW9NRw-YvYDhMiWG4jLHEeaKFG7e_0ZqiSh3; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhcFM8z65heQghJJjGrxpm.5NHD95QcSKeNe0zXe0e7Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo-0S0eEShe0e5tt; ALF=1557768165; sso_info=v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLaNk4y3jLOItIyzjLCJp5WpmYO0to2TjLeMs4i0jLOMsA=='
# cookie = SimpleCookie(str)
# y = [{i.key: i.value for i in cookie.values()}]
# str2 = 'SINAGLOBAL=6052291904347.267.1523584854735; _T_WM=911f60d2fb13c20fc5a50bb11bd447af; UOR=www.shangyang.me,widget.weibo.com,login.sina.com.cn; _s_tentry=service.account.weibo.com; Apache=5726147549537.581.1526030864769; ULV=1526030864851:11:4:2:5726147549537.581.1526030864769:1525933126469; login_sid_t=f3587bfad48d7997d66596731cc30036; cross_origin_proto=SSL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SwGBuUPQWgY6vLYFjNsLz5JpX5K2hUgL.Foqfe0McSo5pSoB2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcSKeNSoq7eKqX; ALF=1557767927; SSOLoginState=1526231928; SCF=AkPjrDiALONXUrpuUXCYEzbwjBowDuhhYFDr5HbhlmcEa1MmKXF0GtMXwpN-BCdtSjqveVGfLsSctFenBzADO5g.; SUB=_2A253_AMoDeRhGeBL6FUX9i7NzTiIHXVUiHPgrDV8PUNbmtBeLXf9kW9NRw-Y2B_Hbc_nGhXBArSXAVbKv8ylDKO5; SUHB=0h15_17Kiy9Swf; un=13859991449; wvr=6'
# cookie = SimpleCookie(str2)
# z = [{i.key: i.value for i in cookie.values()}]
# cookies={'ALC': 'ac%3D0%26bt%3D1526215237%26cv%3D5.0%26et%3D1557751237%26ic%3D1863639441%26scf%3D%26uid%3D3778491552%26vf%3D0%26vs%3D0%26vt%3D0%26es%3Dd666b15915478b020b6c7a540bf46a0b', 'LT': '1526215237', 'tgc': 'TGT-Mzc3ODQ5MTU1Mg==-1526215237-yf-BF56EBFC1014765C1A73E3E92C36035D-1', 'ALF': '1557751237', 'SCF': 'AkncMef-WFGsIsJewZPQ9dJCvmqE7WsFP5Y0K_6l_4PdLmyOIQDipXcEtt82WUeo8V1ldGYUBtYzu8Sk5mwDrLM.', 'SUB': '_2A253_EIVDeRhGeVJ7FoV-S_Jzj6IHXVUiDTdrDV_PUNbm9ANLVSnkW9NT8RAC1n-DsVlo5jk-E_mt79ZZt-CSgh0', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WW98Vb6BMxbNWLW24e2R0L55NHD95Q0S0MRSh.pSK-EWs4Dqcjci--Ri-2Ei-8Fi--4iK.Xi-2Xi--ciK.4iK.fi--NiKLWiKnXi--fi-z7iKysi--4i-zRi-2p', 'sso_info': 'v02m6alo5qztKWRk6ClkJOIpZCUiKWRk6SljpOQpZCTkKWRk5iljpOkpY6TlKWRk5yljpSEpY6DkKWRk5SlkKOApY6EmKWRk6SlkKOgpZCThKadlqWkj5OMt42zoLSOk4S1jZOIwA==', 'SSO-DBL': '219e4a0617d3288012618552eb672f75'}
