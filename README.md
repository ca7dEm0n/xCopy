# xCopy

[![Python3.x](https://img.shields.io/badge/Python-3.7-green.svg?style=plastic)](https://www.python.org/)

MacOS剪切板操作

初衷只是为了能够在有度上发GIF表情包...

# 基础使用


启动
```
./run.sh start
```

停止
```
./run.sh stop
```

# 功能使用与场景

## 有度GIF图床链接修复

支持来源:
    - 腾讯QQ出现的动态表情包复制
    - 有度其他客户端发送的动态表情包

使用方法:
    双击GIF图片, 全选复制, 等待0.5秒左右后即可粘贴到你想发的地方


# 已知BUG

> 已知, 但是不想修, 又不是不能用???

- 操作太过频繁导致卡死

```
    - 在处理程序未结束时，立刻粘贴会出现夯住情况. 
    - 重启大法可以解决
    - ./run.sh restart
```


