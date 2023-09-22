import json
import logging
import os
import textwrap
from pathlib import Path
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


# set API configuration
with open(Path('config/api-config.json')) as json_file:
    conf = json.load(json_file)
    API_VERSION = conf['API_VERSION']
    MODEL_NAME = conf['MODEL_NAME']
    PROMPT_TEMPLATE = conf['PROMPT_TEMPLATE']

# set my personal temporary API key for the sake of this technical test
with open(Path('config/openai-config.json')) as json_file:
    os.environ['OPENAI_API_KEY'] = json.load(json_file)['OPENAI_API_KEY']

logger = logging.getLogger('api')


# load and process the text files

loader = DirectoryLoader('./data/text/', glob="./*.txt", loader_cls=TextLoader)
documents = loader.load()
logger.debug('Loaded documents')

# splitting text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)
logger.debug('Split into chunks completed.')

# download emgeddings from OpenAI
embeddings = OpenAIEmbeddings()

# embed and store the texts
# supplying a presist_dictectory will store the embeddings on disk
presist_directory = './data/db'

# here the new embeddings being used
embeddings = embeddings
vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=presist_directory)
logger.debug('Embeddings calculated and stored.')

# set retreiver
retriever = vectordb.as_retriever()

# create the chain to answer quetions
llm = ChatOpenAI(temperature=0.0) # temperature is 0 to avoid irrelevant responses
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
logger.debug('Chain initialized.')

# set custom WeLoop prompt template
qa_chain.combine_documents_chain.llm_chain.prompt.messages[0].prompt.template = PROMPT_TEMPLATE
logger.debug('Prompt template loaded.')


# cite sources
def wrap_text_preserve_newlines(text, width=110):
    # split the input text into lines based on newline characters
    lines = text.split('\n')

    # wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text

def process_query(request):
    """
    Receives a query string and returns the response from the loaded LLM model.

    Parameters:
        request (str): query string

    Returns:
        response (dict): API response (see readme) containing history, inputs and response.
    """

    # process
    query = request['query']
    response = qa_chain(query)
    sources = []
    for source in response['source_documents']:
        sources.append(source.metadata['source'])
    sources = list(set(sources))

    return {
        "answer": response['result'],
        "source": sources,
        "metadata": {
            "model_version": MODEL_NAME,
            "api_version": API_VERSION
        }
    }
