# アプリケーション名

ラボログ

# アプリについて
神戸大学の研究室を対象にユーザーがアンケート形式で評価するwebアプリです。評価をしてもらって、その結果を表示してくれます。
研究室情報が少ないという問題を解決するために開発しました。

# システムについて
・pythonのフレームワークであるDjangoを使用（バージョン3.2.13）  
・データベースはMySQL  
・一応、redisもインストールする必要がある。  

# 機能一覧や説明
## ホーム画面
ラボログのホーム画面が以下になっています。  
学部と学科を選択すると研究室一覧に遷移する。下のほうには、興味で追加したredisを使ったチャットと簡単な掲示板へのリンク  
<img width="960" alt="image" src="https://github.com/d505/labo/assets/58736165/357efbd6-6c79-481c-8013-60318b99ac6e">

### プロファイル  
一般的なユーザーの削除やユーザー情報の変更の機能がある。  
<img width="163" alt="image" src="https://github.com/d505/labo/assets/58736165/7f54a31b-6c75-44e5-ac72-00d496c72c4f">


## 研究室一覧  
研究室のホームページのリンク、教授名、アンケート結果、アンケートページのリンクがそれぞれの研究室ごとに表示  
<img width="947" alt="スクリーンショット 2023-04-22 021741" src="https://user-images.githubusercontent.com/58736165/233697400-ef28c771-8afd-4269-a5e5-5b5ff16442c4.png">

## 簡単なアンケート　　
以下が簡単なアンケート内容  
<img width="719" alt="image" src="https://github.com/d505/labo/assets/58736165/f9722fc8-9329-44ae-a4ee-ae27eb2aa344">


## アンケート結果表示
評価結果は以下のようになる。
<img width="943" alt="スクリーンショット 2023-04-22 021816" src="https://user-images.githubusercontent.com/58736165/233697474-2a53bdb5-a1bd-43d3-a556-922aa66c3d27.png">

## redis  
簡単なredisを活用したチャット  
<img width="859" alt="image" src="https://github.com/d505/labo/assets/58736165/61d2e161-82b8-4f60-a59f-8dfffce01959">

## 掲示板 
簡単な掲示板(MySQLにテキストなどは保存している。）
<img width="841" alt="image" src="https://github.com/d505/labo/assets/58736165/8d665e3c-ec84-41f6-b97e-65b80be5e47f">





