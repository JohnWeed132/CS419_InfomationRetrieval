from llama_index.llms.gemini import Gemini
from prompt import classifier_promptemp, rag_promptemp, social_promptemp
from retrieval import retrieval


llm = Gemini(
    model="models/gemini-1.5-flash",
    api_key="",
)

classifier_prompt = classifier_promptemp()
qa_prompt = rag_promptemp()
social_prompt = social_promptemp()


def get_domain_status(query: str):
    return llm.complete(classifier_prompt.format(question=query))


def rag(query: str):

    aws = retrieval(query)
    docs = [
        "*"
        + i.metadata["document"]
        + " "
        + i.metadata["article"]
        + "* "
        + i.text.replace("\n", " ")
        for i in aws
    ]
    qa_format = qa_prompt.format(
        query=query,
        doc1=docs[0],
        doc2=docs[1],
        doc3=docs[2],
        doc4=docs[3],
        doc5=docs[4],
        doc6=docs[5],
        doc7=docs[6],
        doc8=docs[7],
        doc9=docs[8],
        doc10=docs[9],
    )
    print(docs)
    return llm.complete(qa_format)


def social(query: str):
    return llm.complete(social_prompt.format(question=query))
