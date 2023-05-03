# LangChainTest

## 概要

Qiitaの以下ページを参考に実装してみたものです。

話題の ChatGPT + LangChain で、膨大な PDF ドキュメントの内容を爆速で把握する  
https://qiita.com/hiroki_okuhata_int/items/7102bab7d96eb2574e7d

VSCode + DevContainerで使用する想定です。  
あとTorch依存なのでGPUを使えないとたぶん動かないです。

## APIキー

ルートディレクトリに`.env`ファイルを置いて、その中にAPIキー情報を書いてください。  
OpenAIに登録してAPIキーを発行しておく必要あります。

サンプルとして`.env.example`を入れてあります。

```
OPENAI_API_KEY=your_api_key
```
