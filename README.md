<h3>アプリ名</h3><br>
文系エンジニアコミュニティ「SandBox」<br>
<hr>
<h3>概要</h3><br>
私が文系の学部に属していることもあり、もともとITエンジニアという職業は情報系学部の人じゃなきゃ厳しい世界だと思っていました<br>
自分が過去に難しい、厳しいと考えていたので文系の人は情報系の人のことを知らない分挑戦する前にエンジニアを諦める人や無理な世界と決めつけてしまう人が多いのではないかと考えました<br>
なので文系エンジニアコミュニティというアプリを作ることで文系からエンジニアになること自体が普通のことなのだと印象付けることができたり、文系学部からエンジニアを目指す人の力になれると思いました<br>
自分自身最初にたくさんのブログをみたりyoutubeをみたり情報をとにかくかき集めてエンジニアのレベル感だったり、文系の人がどこまでエンジニアとしてしっかり働けるのかなどをかなり調べました<br>
無意識にそのような行動をするくらい不安でしたし、文系学部からこの道に決断することへの恐怖がかなりありました<br>
だかろこそ自分がその時に助けられた情報をアプリを通して次は伝える側になりたいと思い、このアプリを作成しました<br>
<hr>
<h3>デプロイ先URL</h3><br>
https://sandbox-rx2xib6pca-an.a.run.app/<br>
<hr>
<h3>使用技術</h3><br>
<h5>Frontend</h5><br>
html, bootstrap(cssフレームワーク)<br>
<h5>Backend</h5><br>
python(flask)<br>
<h5>Database</h5><br>
MySQL(SQLALCHEMYを使用<br>
<h5>SourceCodeManagement</h5><br>
Git/Github
<h5>CI/CD</h5><br>
CloudRun（githubと連携）<br>
→ 現在CloudRunでのエラーによりデプロイが出来ておらず、URLがつながりません
<hr>
<h3>主な機能</h3><br>
<h5>ユーザー</h5><br>
・新規ユーザー登録機能<br>
・ログイン機能<br>
・マイページ（profile(ユーザー情報編集可能、ログアウト）)<br>
・ユーザー一覧機能<br>
・（ユーザー削除機能は管理者ユーザーのみ）
<h5>ブログ</h5><br>
・ブログ投稿機能<br>
・ブログ閲覧機能（アプリ内のブログ、他サイトのブログ）<br>
・ブログ検索機能（アプリ内のブログ、他サイトのブログ）<br>
・ブログお気に入り機能（追加、削除、一覧）<br>
・ブログコメント機能（投稿、削除）<br>
・ブログカテゴリ機能（追加、削除、カテゴリ検索）<br>
<h5>チャット</h5><br>
・チャットメッセージ機能（メッセージ送信、削除）<br>
・チャットチャンネル選択機能（チャンネル追加機能未実装→全体のチャットのみ実装）<br>
<h5>イベント</h5><br>
・イベント閲覧機能（ハッカソン情報、就活情報、イベント情報追加は管理者ユーザーのみ）<br>
・イベント検索機能（ハッカソン情報、就活情報）<br>
