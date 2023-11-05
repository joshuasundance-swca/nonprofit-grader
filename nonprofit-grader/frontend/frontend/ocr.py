import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from langchain.document_loaders.pdf import DocumentIntelligenceLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch

OCR_ENDPOINT = os.environ["OCR_ENDPOINT"]
OCR_API_KEY = os.environ["OCR_API_KEY"]

document_analysis_client = DocumentAnalysisClient(
    endpoint=OCR_ENDPOINT,
    credential=AzureKeyCredential(OCR_API_KEY)
)

loader = DocumentIntelligenceLoader(
    "<Local_filename>", client=document_analysis_client, model="prebuilt-read"
)  # e.g. prebuilt-document

documents = loader.load()



# insert the documents in MongoDB Atlas with their embedding
vector_search = MongoDBAtlasVectorSearch.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(disallowed_special=()),
    collection=MONGODB_COLLECTION,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
)