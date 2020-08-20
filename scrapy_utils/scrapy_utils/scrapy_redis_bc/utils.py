import six


def bytes_to_str(s, encoding='utf-8'):
    """Returns a str if a bytes object is given."""
    if six.PY3 and isinstance(s, bytes):
        return s.decode(encoding)
    return s

# def default_config(crawler, key, value, priority):
#     crawler.settings.set(key, value, priority)
#
#
# def redis_config(crawler, key, value, priority):
#     redis_host = value.get("redis_host")
#     del crawler.settings['REDIS_Config']
#     if value.get("mode") == "REDIS_MASTER_NODES":
#         crawler.settings.set("REDIS_MASTER_NODES", redis_host, priority)
#     else:
#         host = redis_host[0].get("host")
#         port = redis_host[0].get("port")
#         index = redis_host[0].get("index")
#         crawler.settings.set("REDIS_URL", f"redis://{host}:{port}/{index}", priority)
#
#
# setting = {
#     "REDIS_Config": redis_config
# }
#
#
# def settings_configure(crawler):
#     settings_dict = crawler.settings.copy_to_dict()
#     for key, item in settings_dict.items():
#         value = eval(item) if isinstance(item, str) and "{" in item else item
#         priority = crawler.settings.getpriority(key)
#         setting.get(key, default_config)(crawler, key, value, priority)
#     return crawler.settings
