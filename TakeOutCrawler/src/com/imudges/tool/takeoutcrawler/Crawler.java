package com.imudges.tool.takeoutcrawler;

/**
 * 爬虫的基础类
 * User-Agent: Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; 2014813 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.85 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.1.3
 * http://waimai.baidu.com/mobile/waimai?qt=shoplist&address=%E5%91%BC%E5%92%8C%E6%B5%A9%E7%89%B9%E5%B8%82%E8%B5%9B%E7%BD%95%E5%8C%BA%E6%BB%A1%E9%83%BD%E6%B5%B7%E8%A5%BF%E5%B7%B7&lat=4957096.6083937&lng=12433896.720059
 * */
public interface Crawler {

	
	/**
	 * 初始化
	 * */
	public Crawler initial(String lat,String lng);
	
	/**
	 * 
	 * */
	public void print();
	
}

