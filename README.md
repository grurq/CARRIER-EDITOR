### CARRIER-EDITOR
([grurqApps](https://grurq.github.io/) 最終更新:2021-04-18)  
pythonによる簡易パズルゲーム[CARRIER](https://github.com/grurq/CARRIER)の面エディタです。  
作った面.datlevelは結合してステージファイル.crにすることができ、実際に遊ぶことができます。  
### 使い方
起動時にファイル結合をするかどうか訊かれます。  
面をエディットしたい人は、Enterを押してください。  
#### 面エディット
起動後、*「ファイルの結合作業を行いますか？」*の問いにyと答えないと、新規に面データを作成するか既存のファイルを開くか問われます。  
新規エディットの場合はenterを押し、既存ファイルをエディットしたい場合はファイル名またはパスを入力してください。  

操作方法は以下のとおりです。

|キー |操作　|
|:----|:------|
|0     |人	   |
|1     |壁 	　|
|2     |置き場|
|3　  |荷物　|
|方向 |移動　|
|esc  |終了　|

0～3のキーを押して、床にアイテムを設置してください。  
終了すると、自動で.datlevelファイルが生成されます。名前は日付と時刻から取られます。
#### ファイル結合
.datlevelがある場合、ファイルを結合して.crファイルを生成できます。  
起動後の問にyと答えると、ディレクトリ（フォルダ）を指定できます。指定ディレクトリの中のすべての.datlevelを結合して、.crファイルを生成します。  
**※最大面数は20面です。それを超えた数の面を結合すると、正常に動作しない可能性があります。**
### ファイル構造
.datlevelはテキストファイルであり、UTF-8形式でエンコードされています。.crはこれを連結したものです。
.datlevelは
```
XXYY|
ZZZZZZZZZZZ
ZZZZZZZZZZZ
ZZZZZZZZZZZ
..ZZZZZZZZZ|
```
という構造で記述されています。  
XXが横幅、YYが縦幅、Zがタイルデータです。  
Zの中身は以下のタイルを表します。   

|  数|意味	      |表示	|
|:---|:---------|:-----|
|   0|床	       |空白	|
|   1|置き場      |.	|
|   2|荷物         |$	|
|   3|置き荷      |*	|
|   4|床の人      |@	|
|   5|置き場の人|+	|
|   8|壁             |#	|

最大横幅は32,最大縦幅は24,最大面数は20です。

#### 著作権
このゲームはMITライセンスで頒布されます。

> The MIT License  
> Copyright (c) 2021 grurq  

> 以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も無制限に含まれます。  

> 上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載するものとします。
> <https://licenses.opensource.jp/>  
> <https://opensource.org/licenses/mit-license.php>  
