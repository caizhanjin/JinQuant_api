# 项目说明

```
pip install -r requirements.txt

python server.py
```

## 学习文档

+ [tornado](https://www.osgeo.cn/tornado/index.html)
+ [peewee](http://docs.peewee-orm.com/en/latest/index.html)
    
## 项目结构
### tornado项目实践方案
其中包括：应用url路由分发、cx_Oracle再封装和引入、sqlalchemy ORM引入、loging配置引入、restful风格编写示例

```
│  README.md                      # 项目说明
│  requirements.txt               # 所需依赖库
│  server.py                      # 运行入口
│  settings.py                    # 配置
│  urls.py                        # 项目路由设置
│
├─apps                            # app应用文件
│  ├─base                         # 处理基类
│  └─resful                       # 具体应用，resful为应用名
│         handler.py              # 处理逻辑，C控制层
│         model.py                # M模型层，包括：数据库、文件系统、第三放服务
│         tasks.py                # 定时任务
│         tests.py                # 测试方法
│         urls.py                 # 路由映射
├─configs                         # 项目配置
│         log_config.py           # log配置
├─docs                            # 项目文档/说明
├─libs                            # 库文件，中间层的封装（解耦合）
│  └─db                           # 数据库相关中间层
│          base.py
│          oracle.py
├─logs                            # 日志文件存放
├─media                           # 一些媒体资源
├─templates                       # 模板，放html页面
├─static                          # 静态文件，存放js 、css 、html、img
└─utils                           # 工具类，比如：验证码生成、IP地址转换
```

## 其他
+ Author : [caizhanjin](https://github.com/caizhanjin)
+ Email : caizhanjin@qq.com
