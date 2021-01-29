# coding: utf-8
'''
Author: cA7dEm0n
Blog: http://www.a-cat.cn
Since: 2021-01-28 14:28:29
Motto: 欲目千里，更上一层
message: Gif图片处理
'''
import imghdr
import os
import shutil
import tempfile
from time import sleep

from AppKit import (NSURL, NSArray, NSFilenamesPboardType, NSPasteboard,
                    NSPasteboardTypeURL)
from lib.utils import (logging, md5Calc, notify, readJsonFromFile,
                       writeJsonToFile)

GIF_TEMP_PATH = "/tmp/gif"
GIF_DATA_PATH = "/tmp/gif/.data.json"


def _writeObject(p, obj):
    '''
    description: 剪切板写入数据
    '''
    _result = p.writeObjects_(
        NSArray.arrayWithObject_(
            obj
        )
    )
    logging.info(
        "[.] write object %s ... \t[ok]" % (
            str(obj)[:100]
        ) if _result else "[!] write object ... %s \t[fail]" % (
            str(obj)[:100]
        )
    )
    return _result


def upPbURLData(p, url):
    '''
    description: 修复链接
    '''
    p.declareTypes_owner_(
        [NSPasteboardTypeURL],
        None
    )
    _result = False
    try:
        _result = _writeObject(p, url)
    except Exception as error:
        logging.error("upPbURLData error: %s" % error)

    # 不要太快
    sleep(0.5)
    notify("GIF链接修复", "复制成功!")
    return _result


def run():
    '''
    description: 执行
    '''
    pb = NSPasteboard.generalPasteboard()
    _type = pb.types()
    try:
        _file_url = pb.stringForType_("public.file-url")
        if not _file_url:
            logging.info("not found [public.file-url].")
            return None

        if ".gif" in _file_url:
            if "TencentAttributeStringType" not in _type:
                return None

    except Exception as err:
        logging.info("can't get url, error: %s" % err)
        return None

    if NSFilenamesPboardType in _type:
        if not os.path.exists(GIF_TEMP_PATH):
            os.makedirs(GIF_TEMP_PATH)

        img_path = pb.propertyListForType_(NSFilenamesPboardType)[0]
        img_md5 = md5Calc(img_path)
        gif_data = readJsonFromFile(GIF_DATA_PATH)
        cache_path = gif_data.get(img_md5, None)
        if cache_path:
            new_url = NSURL.fileURLWithPath_(cache_path)
            upPbURLData(pb, new_url)
            return

        img_type = imghdr.what(img_path)
        if not img_type or img_type != "gif":
            return None

        _tmp_file = tempfile.NamedTemporaryFile(
            suffix=".gif",
            delete=False,
            dir=GIF_TEMP_PATH
        )
        shutil.copy(img_path, _tmp_file.name)

        new_url = NSURL.fileURLWithPath_(_tmp_file.name)
        _tmp_file.close()

        upPbURLData(pb, new_url)
        gif_data[img_md5] = _tmp_file.name
        writeJsonToFile(gif_data, GIF_DATA_PATH)
        return


def main(*args, **kwargs):
    '''
    description: 运行主程
    '''
    run()
