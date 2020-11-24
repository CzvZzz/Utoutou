from os.path import join, getsize
import os
import string

def usb_copy(src, dst, size, *houzhui):
    if houzhui:
        houzhui = houzhui[0]
    size = size
    names = os.listdir(src)
    os.makedirs(dst)
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        if os.path.isdir(srcname):
            usb_copy(srcname, dstname, size, *houzhui)
        else:
            copy(srcname, dstname, size, *houzhui)

def copy(srcname, dstname, size, *allhouzhui):
    if allhouzhui:
        allhouzhui = allhouzhui[0]
    allhouzhui = allhouzhui.split(',')
    houzhui = os.path.splitext(srcname)
    if allhouzhui:
        if os.path.getsize(srcname) / 1024 / 1024 < size and houzhui[1] in allhouzhui:
            os.system('copy %s %s' % (srcname, dstname))  # 拷贝文件
    else:
        if os.path.getsize(srcname) / 1024 / 1024 < size:
            os.system('copy %s %s' % (srcname, dstname))  # 拷贝文件

def get_dirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum(getsize(join(root, name)) for name in files)
    return size

def get_disklist():
  disk_list = []
  for c in string.ascii_uppercase:
    disk = c + ':'
    if os.path.isdir(disk):
      disk_list.append(disk)
  return disk_list

