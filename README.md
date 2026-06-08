# WordStock(単語帳 × 辞書アプリ)

---

## アプリ概要
単語と意味を登録して自分だけの単語帳兼辞書を作ることができる。<br>
ジャンルごとに単語、意味、具体例を登録してすぐに調べることが可能。<br>
単語の新規登録・編集・削除機能を搭載。

---

## 開発環境
- 使用言語：python
    - フレームワークにDjangoを採用
    - DBSとしてSQLiteを採用

- githubでソース管理


## データベースの構造（モデル名: Word）
- id: 自動連番（主キー）
- word: 文字列（登録する単語・言葉）
- meaning: テキスト（単語の意味・定義）
- example: テキスト（具体例や例文）
- created_at: 日時（登録日時、自動生成）

---

## 初期作成コマンド

最初から作る場合は、以下の流れに沿う。

```powershell
mkdir WordStock-application
cd WordStock-application
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install django
django-admin startproject wordstock_project .
py manage.py startapp words
```
Python ランチャー `py` が使えない環境では、`py` を `python` に置き換えてください。


## このプロジェクトの起動手順

```powershell
cd WordStock-application
py -m venv .venv
.venv\Scripts\activateps1
py -m pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

powershellではなく、cmdで起動する場合、.venv\Scripts\activateと入力してください。

ブラウザで以下を開きます。

- アプリ: http://127.0.0.1:8000/
- 管理画面: http://127.0.0.1:8000/admin/


## サーバーの起動方法

```
python manage.py runserver
```