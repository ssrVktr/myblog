"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os,re
from .base_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@nm8)z+w06b*5l(qbmgf2vkjav1p#4yq#erc(7z2u^-=ijos3t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'read_statistics',
    'comment',
    'ckeditor',
    'ckeditor_uploader',
    'user',
    'likes',
    'imagekit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'user.context_processors.login_modal_form',
                'read_statistics.context_processors.week_hot_blogs',
                'read_statistics.context_processors.month_hot_blogs',
                'blog.context_processors.blog_types',
                'blog.context_processors.blog_dates',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# 配置静态文件地址
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]
#media 配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
#ckeditor
CKEDITOR_UPLOAD_PATH = 'upload/'

# ckeditor 配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
            ['div','Source','-','Save','NewPage','Preview','-','Templates'],
            ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'],
            ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
            ['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'],
            ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['Link','Unlink','Anchor'],
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
            ['Styles','Format','Font','FontSize'],
            ['TextColor','BGColor'],
            ['Maximize','ShowBlocks','-','About', 'pbckcode'],
        ),
        'width':'auto',
        'height':'180',
        'tabSpaces':'4',
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    },
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript','Image'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'width': '100%',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}

# 每页多少条数据
CONTENT_OF_EACH_PAGE = 7

# session 配置
#session不仅可以保存在数据库里，
#数据库（默认）
#缓存（memchache、redis）
#文件
#缓存+数据库
#加密cookie

#SESSION_ENGINE = 'django.contrib.sessions.backends.file'  # 引擎
#SESSION_FILE_PATH = 文件路径  # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
#如：/var/folders/d3/j9tj0gz93dg06bmwxmhh6_xm0000gn/T
#SESSION_COOKIE_NAME="SSSSSSSID"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
#SESSION_COOKIE_PATH="/"  # Session的cookie保存的路径
#SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名
#SESSION_COOKIE_SECURE = False  # 是否Https传输cookie
#SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输
SESSION_COOKIE_AGE = 86400  # Session的cookie失效日期（24小时） 默认1209600秒（两周）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使Session过期,和上面一条不能共存
SESSION_SAVE_EVERY_REQUEST = True
#如果你设置了session的过期时间为30分钟，30分钟后session准时失效
#如果该参数设置为True，在30分钟期间有请求服务端，就不会过期！（为什么逛一晚上淘宝，也不会登出，但是浏览器不刷新了就会自动登出）

#下面这个方法不是在settings中用的

#request.session.set_expiry(value)

#你可以传递四种不同的值给它：

# * 如果value是个整数，session会在秒数后失效（适用于整个Django框架，即这个数值时效时整个页面都会session失效）。

#* 如果value是个datatime或timedelta，session就会在这个时间后失效。

#* 如果value是0,用户关闭浏览器session就会失效。

# * 如果value是None,session会依赖全局session失效策略。

