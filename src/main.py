# ref: https://qiita.com/hiroki_okuhata_int/items/7102bab7d96eb2574e7d

import os
import shutil

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader

# 自民党AIの進化と実装に関するプロジェクトチーム ホワイトペーパー https://note.com/akihisa_shiozaki/n/n4c126c27fd3d
target_pdf = (
    "https://note.com/api/v2/attachments/download/0c61c5696cd01694c4693164b8f54dc0"
)
# 環境省 令和4年版 環境・循環型社会・生物多様性白書（PDF版） https://www.env.go.jp/policy/hakusyo/r04/pdf.html
# target_pdf = "https://www.env.go.jp/policy/hakusyo/r04/pdf/full.pdf"

print("🔖 PDF Load: START")
loader = PyPDFLoader(target_pdf)

pages = loader.load_and_split()
# content = pages[0].page_content

# APIキーが必要(DevContainerにより.envから取得される)
print("🔖 Initialize Model: START")
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
# llm = ChatOpenAI(temperature=0, model_name="gpt-4")

# OpenAI提供のembeddingを使用
embeddings = OpenAIEmbeddings()

# ベクターストアはOSSのChromaを使用
db_directory = "./chromadb/"
if os.path.exists(db_directory):
    shutil.rmtree(db_directory)

print("🔖 Stored in ChromaDB: START")
vectordb = Chroma.from_documents(
    pages, embedding=embeddings, persist_directory=db_directory
)
vectordb.persist()  # 永続化

print("🔖 Query: START")
pdf_qa = ConversationalRetrievalChain.from_llm(
    llm, vectordb.as_retriever(), return_source_documents=True
)

queries = [
    "このホワイトペーパーは何を主張していますか？300文字程度を目安に回答してください。 Please in Japanese.",
    "このホワイトペーパーにより我々が行動すべきことはありますか？ Please in Japanese.",
]
chat_history = []

for query in queries:
    result = pdf_qa({"question": query, "chat_history": chat_history})

    print(f"💡 Q: {query}")
    print(f"🚩 A: {result['answer']}")

    sources = result["source_documents"]
    print(f"🚀 source: {len(sources)} 件 🚀")
    for s in sources:
        print(f" 🐞 page: {s.metadata['page']} / {s.page_content}")

    print("")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("")

    chat_history = [(query, result["answer"])]

pass
