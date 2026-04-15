#!/usr/bin/env python3
"""
小红书工具集 - 清禾出品
功能：浏览器自动化操作小红书
"""
import sys
import json
from playwright.sync_api import sync_playwright

class XHSTool:
    def __init__(self, cookies_path="~/.xiaohongshu-mcp/cookies.json"):
        self.cookies_path = cookies_path.replace("~", "/Users/yilinzhao")
        self.browser = None
        self.context = None
        self.page = None
        
    def load_cookies(self):
        with open(self.cookies_path) as f:
            return json.load(f)
    
    def init_browser(self, headless=True):
        self.browser = sync_playwright().start().chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.context.add_cookies(self.load_cookies())
        self.page = self.context.new_page()
        
    def close(self):
        if self.browser:
            self.browser.close()
            
    def check_login(self):
        self.init_browser()
        self.page.goto("https://www.xiaohongshu.com/creator/home", timeout=15000)
        self.page.wait_for_timeout(3000)
        url = self.page.url
        self.close()
        return "登录" not in url
    
    def get_creator_data(self):
        self.init_browser()
        self.page.goto("https://www.xiaohongshu.com/creator/home", timeout=15000)
        self.page.wait_for_timeout(3000)
        html = self.page.inner_text("body")
        self.close()
        return html

if __name__ == "__main__":
    tool = XHSTool()
    if sys.argv[1] == "check":
        print(f"登录状态: {tool.check_login()}")
    elif sys.argv[1] == "data":
        print(tool.get_creator_data())
