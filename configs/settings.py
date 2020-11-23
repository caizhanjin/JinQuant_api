# encoding: utf-8
import os

# from sqlalchemy import create_engine
from tornado.options import define, options
from libs.db.oracle import DbOracle
from configs import initialize_logging

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# 编码设置
os.environ["NLS_LANG"] = "SIMPLIFIED CHINESE_CHINA.UTF8"

# 定义一些在命令行中传递的参数和类型
# 启动项目示例：python server.py --config="test"
define("config", default="test", help="Which environ config?")
define("port", default=8000, help="Run server on a specific port", type=int)
define("host", default="localhost", help="Run server on a specific host")
define("debug", default=True, help="Is debug?", type=bool)
define("database", default="test", help="Which database?")

# 获取options，全局只有一个options
options.parse_command_line()  # 从url中获取参数
evn_cfg_path = os.path.join(ROOT_PATH, "configs/cfg", options.config + ".cfg")  # 从配置文件中获取参数
options.parse_config_file(os.path.join(ROOT_PATH, evn_cfg_path))  # 从配置文件中获取参数

# the application settings
STATIC_PATH = os.path.join(ROOT_PATH, "static")
TEMPLATE_PATH = os.path.join(ROOT_PATH, "templates")

if not os.path.isdir(STATIC_PATH):
    os.mkdir(STATIC_PATH)


settings = {
    "debug": options.debug,
    "static_path": STATIC_PATH,
    "template_loader": TEMPLATE_PATH,
    "cookie_secret": "xhIBBR2lSp2Pfpx4iiIyX/X6K9j7VUB9oNeA+YdS+ng=",
    # "xsrf_cookies": True,
}

# 日志初始化
LOG_BASE_PATH = os.path.join(ROOT_PATH, "logs")
initialize_logging(LOG_BASE_PATH)

# data_base
DATABASES = {
    "test": {
        "USER": "",
        "PASSWORD": "",
        "NAME": "",
        "HOST": "",
        "PORT": "",
        "charset": "utf8"
    },
    "official": {
        "USER": "",
        "PASSWORD": "",
        "NAME": "",
        "HOST": "",
        "PORT": "",
        "charset": "utf8"
    },
}

DB_ORACLE = DATABASES[options.database]

ORACLE_ENGINE = DbOracle(
    DB_ORACLE["USER"],
    DB_ORACLE["PASSWORD"],
    DB_ORACLE["NAME"],
    DB_ORACLE["HOST"],
    DB_ORACLE["PORT"],
)

ORM_URL = "oracle://{}:{}@{}:{}/?service_name={}".format(
    DB_ORACLE['USER'],
    DB_ORACLE['PASSWORD'],
    DB_ORACLE['HOST'],
    DB_ORACLE['PORT'],
    DB_ORACLE['NAME']
)
# ORM_ENGINE = create_engine(ORM_URL, echo=True)
