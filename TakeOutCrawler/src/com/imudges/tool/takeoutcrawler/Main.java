package com.imudges.tool.takeoutcrawler;

import java.util.Properties;

/**
 * ≤‚ ‘¿‡
 * */
public class Main {
	public static void main(String[] args) {
		//new BaiduCrawler().initial("4957096.6083937", "12433896.720059").print();
		String url = "http://client.waimai.baidu.com/shopui/na/v1/cliententry";
		String param = "resid=1001&from=na-android&os=5.1.1&sv=3.9.1&cuid=E8E7DA5EEF8BD6A7BEE5918C36C96DDD%7C273344620823668&model=2014813&screen=720*1280&channel=com.xiaomi&loc_lat=4957500.020675&loc_lng=1.2434008580618E7&city_id=&aoi_id=&address=&net_type=wifi&isp=46007&request_time=1469611552152";
		String string = HttpRequest.sendPost(url +"?" + param, "lat=0.0&lng=0.0&count=20&page=1&bduss=NA&stoken=bdwm&sortby=&taste=&city_id=&promotion=&return_type=launch");
		
	}
}
