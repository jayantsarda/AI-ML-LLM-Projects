from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from datasets import load_dataset
import sys
sys.path.insert(1, '/Users/jaysarda/Documents/AI-ML-LLM-Projects/AI-ML-LLM-Projects')
import Secrets
#import convertXmlToDataFrame

cloud_configs={
    'secure_connect_bundle':Secrets.ASTRA_DB_SECURE_BINDLE_PATH
}
auth_providerText = PlainTextAuthProvider(Secrets.ASTRA_DB_CLIENT_ID,Secrets.ASTRA_DB_CLIENT_SECRET)
print(auth_providerText)
cluster = Cluster(cloud=cloud_configs, auth_provider=auth_providerText)
astraSession = cluster.connect()
llm=OpenAI(openai_api_key = Secrets.OPENAI_API_KEY)
myEmbedding = OpenAIEmbeddings(openai_api_key = Secrets.OPENAI_API_KEY)
myCasssandraVStore = Cassandra(embedding=myEmbedding,session = astraSession,keyspace=Secrets.ATRA_DB_KEYSPACE,table_name="test_demo")

print("loading data")
#myDataset = load_dataset(convertXmlToDataFrame.df, split="train")
#tests = myDataset["text"]
##myCasssandraVStore.add_texts(convertXmlToDataFrame.df)
#print("Inserted %i tests.\n" % len(tests))

#myDataset = load_dataset("Biddls/Onion_News", split="train")
#headlines = myDataset["text"][:50]
#myCasssandraVStore.add_texts(headlines)
#print("Inserted %i healines.\n" % len(headlines))
vectorIndex  = VectorStoreIndexWrapper(vectorstore=myCasssandraVStore)

first_question = True
while True:
    if first_question:
        query_text = input('\nEnter your question or type quit to exit')
        first_question=False
    else:
        uery_text = input('\Whats your next question or type quit to exit')
    if query_text.lower=='quit':
        break
    print("Question: \"%s\"" % query_text)
    answer = vectorIndex.query(query_text, llm=llm).strip()
    print("ANSWER: \"%s\"\n" % answer)

    print('Tests Used')
    for doc, score in myCasssandraVStore.similarity_search_with_score(query_text, k=4):
        print("  %0.4f \"%s ...\"" % (score,doc.page_content[:60]))



# readme  - pip3 install cassio datasets langchain openai tiktoken