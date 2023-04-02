import requests
import hashlib
import random
import json
from read_connfig import data_config

# 百度翻译API的应用ID和密钥
class use_api_idkey:
    def __init__(self):
        data_config.get_data_config()
        self.app_id = data_config.config_dict.get("app_id")
        self.secret_key = data_config.config_dict.get("secret_key")
use_api = use_api_idkey()
global app_id,secret_key
app_id =use_api.app_id
secret_key = use_api.secret_key


# 定义翻译函数
def translate(q, from_lang, to_lang):
    # 定义百度翻译API的请求URL和参数
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = hashlib.md5((app_id + q + str(salt) + secret_key).encode('utf-8')).hexdigest()
    params = {
        'q': q,
        'from': from_lang,
        'to': to_lang,
        'appid': app_id,
        'salt': salt,
        'sign': sign
    }
    # 发送GET请求并解析响应结果
    response = requests.get(url, params=params)
    result = json.loads(response.content)
    if 'error_code' in result:
        # 如果出现错误，打印错误信息
        result='翻译失败，错误码：{}，错误信息：{}'.format(result['error_code'], result['error_msg'])
        return result
    else:
        # 如果翻译成功，返回翻译结果
        result_tanslate=result['trans_result'][0]['dst']
        return result_tanslate

