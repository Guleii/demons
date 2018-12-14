import time

from general.ImageContrastUtils import ImageContrast
from config import GlobalConfig as gl
from general.KeyCodeSentUtils import KeyCode


class ImageUtil:
    first_screen_shot_name = "first_screen_shot"  # 第一张截图的默认名称
    second_screen_shot_name = "second_screen_shot"  # 第二张截图的默认名称
    perform_first_screen_shot_wait_time = 10  # 第一张截图执行前默认等待的时间
    perform_second_screen_shot_wait_time = 10  # 第二张截图执行前默认等待的时间
    image_contrast_percent = 10  # 图片默认对比是否一致的百分比
    picture_format = ".png"  # 图片格式
    screen_width = 1920  # 要测量的设备的宽
    screen_height = 1080  # 要测量的设备的高
    screen_shot_left_up_x = 0
    screen_shot_left_up_y = 0
    screen_shot_right_down_x = screen_width
    screen_shot_right_down_y = screen_height
    err_message = "第三方视频无法播放"  # 要测量的设备的高

    @staticmethod
    def check_video_has_playing_normal(driver, perform_first_screen_shot_wait_time=perform_first_screen_shot_wait_time,
                                       perform_second_screen_shot_wait_time=perform_second_screen_shot_wait_time,
                                       first_screen_shot_name=first_screen_shot_name,
                                       second_screen_shot_name=second_screen_shot_name,
                                       image_contrast_percent=image_contrast_percent,
                                       screen_shot_left_up_x=screen_shot_left_up_x,
                                       screen_shot_left_up_y=screen_shot_left_up_y,
                                       screen_shot_right_down_x=screen_shot_right_down_x,
                                       screen_shot_right_down_y=screen_shot_right_down_y,
                                       err_message=err_message,neet_enter_center=False):
        image_contrast = ImageContrast(driver)

        time.sleep(perform_first_screen_shot_wait_time)
        image_contrast.get_screen_shot_by_custom_size(screen_shot_left_up_x, screen_shot_left_up_y,
                                                      screen_shot_right_down_x, screen_shot_right_down_y).write_to_file(gl.screen_shot_path, first_screen_shot_name)

        if neet_enter_center: # 是否需要进入
            KeyCode.touch_center(driver)

        time.sleep(perform_second_screen_shot_wait_time)
        image_contrast.get_screen_shot_by_custom_size(screen_shot_left_up_x, screen_shot_left_up_y,
                                                      screen_shot_right_down_x, screen_shot_right_down_y).write_to_file(gl.screen_shot_path, second_screen_shot_name)
        # result = imageContrast.get_screen_shot_by_element(element)
        mode_image = gl.screen_shot_path + first_screen_shot_name + gl.screen_shot_picture_format
        now_image = gl.screen_shot_path + second_screen_shot_name + gl.screen_shot_picture_format
        return image_contrast.same_as(mode_image, now_image, image_contrast_percent, err_message=err_message)

