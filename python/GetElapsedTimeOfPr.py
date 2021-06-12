# GitHub APIを使用して、PRが作成されてからmergeされるまでの時間を計算します。
# 使い方
#   python3 GetElapsedTimeOfPr.py https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number} {token}
# 
#   第一引数：取得対象のURL
#     {owner}:GitHubのアカウント名
#     {repo}:リポジトリ名
#     {pull_number}:PR番号
#     参考：https://docs.github.com/ja/rest/reference/pulls#get-a-pull-request
#   第二引数：トークン
#     {token}:プライベートリポジトリの場合はトークンを設定してください。
#     参考：https://docs.github.com/ja/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token

import urllib.request
import json
import ssl
import datetime
import sys

argvs = sys.argv
url = argvs[1]
if len(argvs) > 2:
  token = argvs[2]
else:
  token = ''

ssl._create_default_https_context = ssl._create_unverified_context
req = urllib.request.Request(url)
if len(token) > 0:
  req.add_header('Authorization', 'token {}'.format(token))

with urllib.request.urlopen(req) as res:
  res_str = res.read().decode('utf-8')

json_str = json.loads(res_str)
KEY_TITLE = 'title'
KEY_CREATED_AT = 'created_at'
KEY_MERGED_AT = 'merged_at'
print('title:{}'.format(json_str[KEY_TITLE]))
print('created_at:{} '.format(json_str[KEY_CREATED_AT]))
print('merged_at:{}'.format(json_str[KEY_MERGED_AT]))

TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
created_dt = datetime.datetime.strptime(json_str[KEY_CREATED_AT], TIME_FORMAT)
merged_dt = datetime.datetime.strptime(json_str[KEY_MERGED_AT], TIME_FORMAT)
elapsed_time = merged_dt - created_dt
print('Elapsed time:{}h'.format(elapsed_time.total_seconds() // 60))
