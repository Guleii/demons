# -*- coding: utf-8 -*-

"""HTMLTestRunner 截图版示例 appium版"""
import sys
from config import GlobalConfig as gl
from appium import webdriver
import unittest
# from HTMLTestRunner_cn import HTMLTestRunner
from general.HTMLTestRunner_cn import HTMLTestRunner
from general.AppLog import *
from general import KeyCodeSentUtils, Utils, BaseUnittest
from general.BaseEmail import start_send_email
from general.HtmlReportUtils import HtmlReport
from moudle import HomeTabUtils, InputManagerUtils
from src.pages.LauncherTabPage import *


skip_case = True
skip_reason = "调试"


class case_01(BaseUnittest.BaseTestCase):
    currentActivity = ""

    """
        Launcher:更多模块测试
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_launcher_more(self):
        Utils.Logging.error("当前界面：test_case1:  " + self.driver.current_activity)
        self.currentActivity = self.driver.current_activity


        # HomeTabUtils.TabUtils.click_tab_five(self.driver, before_wait_time=5)
        # HomeTabUtils.TabUtils.click_tab_two(self.driver, before_wait_time=5)

        KeyCodeSentUtils.KeyCode.touch_left(self.driver, 4)
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 首页专题
        self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 1, 6)

        # 视频应用
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 1)

        # 主题影院
        self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 1, 2)

        # 剧集分类
        self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 1, 2)

        # 综艺show
        self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 1, 2)

        # 少儿天地
        # self.enterDetail()
        # Key_code_touch.KeyCode.touch_back(self.driver, 2)
        #
        # Key_code_touch.KeyCode.touch_down(self.driver, 2, 2)

        # 电影票房榜
        # self.enterDetail()
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)

    """
         Launcher:我的模块测试
     """

    @unittest.skipIf(skip_case, skip_reason)
    def test_b_launcher_user(self):

        HomeTabUtils.TabUtils.click_tab_three(self.driver, before_wait_time=2)

        # 防止上一个用例执行失败，返回Tab栏
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2)

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        # 我的顶部专题
        self.enterDetail()

        time.sleep(3)
        # closeLog()
        time.sleep(30)
        return

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 2)

        # 我的精选，第一次如果未安装，则点击安装，然后等待6秒后重试
        # self.enter_load_retry()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 观影历史
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 今天值得观看，第一次如果未安装，则点击安装，然后等待6秒后重试
        # self.enter_load_retry()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 为你推荐
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 系统设置
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 豆瓣佳片推荐，欢乐好时光
        # self.enterDetail()
        # Key_code_touch.KeyCode.touch_back(self.driver, 2)

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 今日热播，大家都在看
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 2)

        # 最新上线
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 精选专区
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)

        # 重磅推荐：精选好句看不停
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 2)

        # 电影：精选大片看到爽
        # self.enterDetail()

        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 2)

        # 精彩不容错过
        self.enterDetail()
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 2, 1)
        # Key_code_touch.KeyCode.touch_down(self.driver, 2, 2)
        KeyCodeSentUtils.KeyCode.touch_center(self.driver, wait_time=2)

        # Key_code_touch.KeyCode.touch_down(self.driver, 2)

        # 古装言情剧
        # self.enterDetail()

        # Key_code_touch.KeyCode.touch_down(self.driver, 2)

        # 爱情喜剧电影
        # self.enterDetail()

    """
         Launcher:VIP模块测试
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_c_launcher_vip(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_four(self.driver, before_wait_time=2)
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2)

        # 专题-2
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 3)
        self.enterDetail()

    """
        Launcher:电影模块测试
     """
    @unittest.skipIf(skip_case, skip_reason)
    def test_d_launcher_movie(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_five(self.driver, before_wait_time=2)
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2, 2)

        # 专题 -2
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 2)
        self.enterDetail()

        # 贴心影向标
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 5)
        self.enterDetail()

        # 周末放映室
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 2)
        self.enterDetail()

        # 精选专题底部
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 7)
        self.enterDetail()

    """
         Launcher:少儿 模块测试
     """

    @unittest.skipIf(skip_case, skip_reason)
    def test_e_launcher_children(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_six(self.driver, before_wait_time=2)
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2, 3)

        # 专题
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        KeyCodeSentUtils.KeyCode.touch_left(self.driver, 2)
        self.enterDetail()

        # 长图标
        # Key_code_touch.KeyCode.touch_down(self.driver, 2, 6)
        # self.enterDetail()

        # 中间的
        # Key_code_touch.KeyCode.touch_down(self.driver, 2, 31)
        # self.enterDetail()

    """
        Launcher:电视剧 模块测试
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_f_launcher_tv_series(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_seven(self.driver, before_wait_time=2)
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2, 4)

        # 专题
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 4)
        self.enterDetail()

    """
         Launcher:综艺 模块测试
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_g_launcher_variety(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_eight(self.driver, before_wait_time=2)
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2, 5)

        # 专题-2
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 2)
        self.enterDetail()

        # 卫视综艺 -卫视
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 7)
        self.enterDetail()

    """
        Launcher:体育 模块测试
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_h_launcher_sport(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_nine(self.driver, before_wait_time=2)
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2, 6)

        # 专题-2
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()

        # 最热赛事
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()

        # WWE
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2, 8)
        self.enterDetail()

        # UFC
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()

    """
         Launcher:4K 模块测试
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_i_launcher_4k(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_ten(self.driver, before_wait_time=2)
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2, 7)

        # 专题
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()

        # 4K免费试看区
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()

    """
        Launcher:应用 模块测试
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_j_launcher_app(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_eleven(self.driver, before_wait_time=2)
        # Key_code_touch.KeyCode.touch_back(self.driver, 4)
        # Key_code_touch.KeyCode.touch_right(self.driver, 2, 8)

        # 顶部
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()
        KeyCodeSentUtils.KeyCode.touch_right(self.driver, 2)
        self.enterDetail()

        # 应用
        KeyCodeSentUtils.KeyCode.touch_down(self.driver, 2)
        self.enterDetail()
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 0)
        KeyCodeSentUtils.KeyCode.touch_left(self.driver, 2)
        self.enterDetail()
        # Key_code_touch.KeyCode.touch_right(self.driver, 3)
        # self.enterDetail()

    """
         Launcher:搜索 模块测试
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_k_launcher_search(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        HomeTabUtils.TabUtils.click_tab_one(self.driver, before_wait_time=2)
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        KeyCodeSentUtils.KeyCode.touch_left(self.driver, 2, 2)
        InputManagerUtils.InputManager.input_x(self.driver)
        InputManagerUtils.InputManager.input_i(self.driver)
        InputManagerUtils.InputManager.input_a(self.driver)
        InputManagerUtils.InputManager.input_o(self.driver)
        # InputManagerUtils.InputManager.input_m(self.driver)
        # InputManagerUtils.InputManager.input_i(self.driver)
        InputManagerUtils.InputManager.input_nine(self.driver)
        InputManagerUtils.InputManager.input_delete(self.driver, after_wait_time=3)
        InputManagerUtils.InputManager.input_clear(self.driver)
        time.sleep(3)
        time.sleep(9)

    """
            Launcher:tab测试
    """

    @unittest.skipIf( 3>24, skip_reason)
    def test_l_launcher_tab(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        launcher_tab = LauncherTab(self.driver)
        launcher_tab.click_from_left_to_right()
        # log()
        # HomeTabUtils.TabUtils.click_tab_one(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_two(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_three(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_four(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_five(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_six(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_seven(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_eight(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_nine(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_ten(self.driver, before_wait_time=2)
        # HomeTabUtils.TabUtils.click_tab_eleven(self.driver, before_wait_time=2)
        time.sleep(3)

    def enter_load_retry(self):
        KeyCodeSentUtils.KeyCode.touch_center(self.driver, 0, 2)
        enter_activity = self.driver.current_activity
        try:
            self.assertNotEqual(self.currentActivity, enter_activity)
            KeyCodeSentUtils.KeyCode.touch_back(self.driver, 2)
        except Exception as e:
            self.add_img()
            time.sleep(6)
            self.enterDetail()

    def enterDetail(self):
        KeyCodeSentUtils.KeyCode.touch_center(self.driver, 0, 2)
        enter_activity = self.driver.current_activity
        try:
            self.assertNotEqual(self.currentActivity, enter_activity)
        except Exception as e:
            self.add_img()
            raise e

        Utils.Logging.error("当前界面：test_case111:   " + self.driver.current_activity)
        # Key_code_touch.KeyCode.touch_down(self.driver, 2)
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 2)


# class case_02(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '6.0'
#         desired_caps['deviceName'] = 'Android Emulator'
#         desired_caps['app'] = 'com.xgimi.instruction30'
#         desired_caps['appActivity'] = 'com.xgimi.instruction30.net_instruction.ui.SplashActivity'
#         cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
#     @classmethod
#     def tearDownClass(cls):
#
#         cls.driver.quit()
#         # closeLog()
#
#     def add_img(self):
#         # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
#         self.imgs.append(self.driver.get_screenshot_as_base64())
#         return True
#
#     def setUp(self):
#         self.imgs = []
#         self.addCleanup(self.cleanup)
#
#     def cleanup(self):
#         pass
#
#     def test_case1(self):
#         """ 手机QQ截图"""
#         pass
#         # self.driver.get
#         # self.add_img()
#         # self.add_img()
#         # self.add_img()
#         # self.add_img()
#         # self.add_img()
#         # browser=self.browser
#         # browser.get(self.base_url+'/')
#         # u"""百度云登录"""
#         # browser.find_element_by_name("userName").clear()
#         # username=browser.find_element_by_name("userName")
#         # username.send_keys("alu***")
#         # username.send_keys(Keys.TAB)
#         # time.sleep(2)
#         # password=browser.find_element_by_name("password")
#         # password.send_keys("***")
#         # password.send_keys(Keys.ENTER)
#         # time.sleep(3)
#         # browser.close()
#
#     def test_case2(self):
#         """ 手机QQ截图"""
#         Utils.Logging.error("纸飞机反击反击减肥减肥22222")
#         log(filename="case222--—-")
#         title = self.driver.find_element_by_id("com.xgimi.instruction30:id/tv2")
#         title.click()
#         # self.driver.get
#         # self.add_img()
#         # self.add_img()
#         # self.add_img()
#         # self.add_img()
#         # self.add_img()
#         # browser=self.browser
#         # browser.get(self.base_url+'/')
#         # u"""百度云登录"""
#         # browser.find_element_by_name("userName").clear()
#         # username=browser.find_element_by_name("userName")
#         # username.send_keys("alu***")
#         # username.send_keys(Keys.TAB)
#         # time.sleep(2)
#         # password=browser.find_element_by_name("password")
#         # password.send_keys("***")
#         # password.send_keys(Keys.ENTER)
#         # time.sleep(3)
#         # browser.close()
# # 仿佛附近


if __name__ == "__main__":
    # dir = os.path.abspath(os.path.join(os.path.dirname('TestReport3.py'),os.path.pardir))+""
    # testdir = r''+dir
    # testdir = r'D:\other\jenkins\workspace\AppiumTest'

    Utils.Logging.error("纸飞机反击反击减肥减肥111")


    # testdir = r'D:\Android_AutoTest\TestCode\Module\LaucherTest\report'
    # # now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    # # logcatname = testdir + "\\" + now + "报告.html"
    # logcatname = testdir + "\\" + gl.report_name


    suiteAll = unittest.TestSuite()
    test1 = unittest.TestLoader().loadTestsFromTestCase(case_01)
    # test2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    suiteAll.addTest(test1)
    # suiteAll.addTest(test2)
    # runer = HTMLTestRunner(title="带截图的测试报告", description="测试描述", stream=open(logcatname, "wb"), verbosity=2, retry=0, save_last_try=True)
    runner = HtmlReport.get_generate_report_object()
    runner.run(suiteAll)

    # 发送邮件
    # start_send_email()



