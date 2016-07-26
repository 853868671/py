# william

## spider 基金代码测试

	    spider = Spider("http://fund.eastmoney.com/f10/jjzh_001494.html")
	    html= spider.getHtml();

	    reg1 = r'<tbody>(.*?)</tbody>'
	    content = spider.getMatch(html,reg1)
	    reg2 = r'<a\s+href="(http://fund.eastmoney.com)\/(\d+)\.html">\d+</a>'
	    con = spider.getMatchAll(content,reg2)
	    spider.csvWrite('001494',['url','coding'],con)


