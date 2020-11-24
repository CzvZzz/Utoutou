import os
import time
import functions as ft
import random
import shutil

def run_app(size, *houzhui):

    old_dirsize = []
    base_disklist = []
    new_disklist = []
    if houzhui:
        houzhui = houzhui[0]

    #size = 10
    #houzhui = '.txt'

    base_disklist = ft.get_disklist()
    # print(base_disklist)

    while(1):
        new_disklist = ft.get_disklist()
        # print(new_disklist)
        if len(new_disklist) > len(base_disklist):
            for usb in new_disklist[len(base_disklist):]:
                file_save = 'C:\\file_save-' + str(random.randint(0, 1000))  # 保存目录
                # print('检测到U盘')
                new_dirsize = ft.get_dirsize((usb + '\\'))
                # print(new_dirsize)
                if new_dirsize not in old_dirsize:
                    print('开始复制......')
                    ft.usb_copy((usb + '\\'), file_save, size, *houzhui)
                    old_dirsize.append(new_dirsize)
                    print('复制完成')
                else:
                    print('U盘无变化')
        else:
            print('暂时没U盘')
        time.sleep(3)

if __name__ == "__main__":
    run_app()