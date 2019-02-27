import os

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # 每次请求结束后，自动提交数据库中的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 管理员邮箱
    NICEBLOG_ADMIN = '1287265008@qq.com'

    PER_PAGE_10 = 10
    PER_PAGE_5 = 5
    PER_PAGE_20 = 20

    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    # 发送验证的邮箱信息
    MAIL_USERNAME = '544642279@qq.com'
    MAIL_PASSWORD = '授权登录密码'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    # 发件人
    NICEBLOG_MAIL_SENDER = 'NiceBlog<544642279@qq.com>'
    # 邮件主题前缀
    NICEBLOG_MAIL_SUBJECT_PREFIX = '[NiceBlog]'


# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    # 数据库URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@134.175.80.121:3306/work'


# 测试环境的配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'niceblog_test.sqlite')


# 生产环境的配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/niceblog'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
