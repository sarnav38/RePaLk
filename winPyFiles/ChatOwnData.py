import os, openai
from dotenv import load_dotenv, find_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from winPyFiles.query import mySpeak

# TODO openai key:
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']


def queryData(dataFile):
    if dataFile.endswith('.pdf'):
        loader = PyPDFLoader(dataFile)
        pages = loader.load()
    else:
        loader = loader = TextLoader(dataFile)
        pages = loader.load()

    text_spliter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=800,
                                                  chunk_overlap=200, length_function=len)
    text_doc = text_spliter.split_documents(pages)
    embeddings = OpenAIEmbeddings()
    chromeVs = Chroma.from_documents(text_doc, embeddings)
    chain = load_qa_chain(OpenAI(), chain_type='stuff')
    return chromeVs, chain


def query(vectorDb, prompt_chain, q):
    content = vectorDb.similarity_search(query=q, k=2)
    doc_page = content[0].metadata['page'] + 1
    res = prompt_chain.run(input_documents=content, question=q)
    mySpeak("Searching prompt")
    mySpeak("According to ChatBot")
    return res, doc_page
