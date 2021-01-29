# coding: utf-8
'''
@Author: cA7dEm0n
@Blog: http://www.a-cat.cn
@Since: 2020-05-22 23:18:10
@Motto: 欲目千里，更上一层
@message: X剪切板
'''

import os
import sys
from queue import Queue
from threading import Timer

import plugins

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from lib.utils import logging

XCOPY_MAX_JOB = os.environ.get("XCOPY_MAX_JOB", 1)


PLUGINS_LIST = {
    _: getattr(plugins, _) for _ in dir(plugins) if "Plugins" in _
}


def runPluginsJob(q):
    '''
    description: 执行插件任务
    '''
    while not q.empty():
        _run_job_func = q.get()
        try:
            _run_job_func.main()
        except Exception as error:
            logging.info(error)
        q.task_done()


def putPluginsJob(job, **kwargs):
    '''
    description: 生成插件任务
    '''    
    _log = kwargs.get('log', False)
    for i,k in PLUGINS_LIST.items():
        if _log:
            logging.info("[.] Push [%s] job"%(i))
        job.put(k)


if __name__ == "__main__":
    from random import randint

    for _ in PLUGINS_LIST:
        logging.info("[.] Load [%s] Plugins." % _ )

    # 队列列表
    jobs = Queue(maxsize=XCOPY_MAX_JOB)

    while True:
        # 生成任务
        _log = randint(0, 100) == 100
        putPluginsJob(jobs, log=_log)

        # 执行任务
        worker = Timer(1, runPluginsJob, args=(jobs, ))
        worker.start()
        worker.join()
   
