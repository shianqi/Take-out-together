package com.imudges.tool.takeoutcrawler;

public class BaiduCrawler implements Crawler{
	
	private String base = "http://waimai.baidu.com/mobile/waimai";
	private String param = "qt=shoplist&address=";
	
	@Override
	public Crawler initial(String lat, String lng) {
		param = param + "&lat=" + lat + "&lng=" + lng;

		return this;
	}
	
	public void print(){
		System.out.println("base:" + base);
		System.out.println("param:" + param);
		System.out.println(HttpRequest.sendGet(base,param));
	}
}
