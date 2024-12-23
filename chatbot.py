from sentence_transformers import SentenceTransformer
import faiss
from groq import Groq

class Chatbot:
    def __init__(self):
        self.client = Groq(api_key='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')
        self.model, self.index, self.texts = self.initialize_resources()

    def initialize_resources(self):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        index = faiss.read_index('combined_index.index')
        
        with open('combined_texts.txt', 'r', encoding='utf-8') as f:
            texts = f.readlines()

        return model, index, texts

    def retrieve_context(self, user_query, k=3):
        query_embedding = self.model.encode([user_query])
        D, I = self.index.search(query_embedding, k)
        retrieved_text = "\n".join([self.texts[i].strip() for i in I[0]])
        return retrieved_text

    def generate_response(self, query, k=3):
        context = self.retrieve_context(query, k)
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a supportive and knowledgeable assistant focused on providing accurate, empathetic, and concise answers about HIV. "
                        "Your goal is to empower users with reliable information while being non-judgmental and sensitive. "
                        "Only answer questions related to HIV, and always base your responses on the provided context. "
                        "If the question is unrelated to HIV, politely indicate that you can only assist with HIV-related topics. "
                        "Keep your responses clear, short, and precise."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Answer the following question based on the provided context. "
                        f"Keep your response brief, clear, and precise. "
                        f"If the question is not related to HIV, respond: 'I'm sorry, but I can only provide assistance with HIV-related questions. Please let me know if you have any questions about HIV.'\n\n"
                        f"Context:\n{context}\n\n"
                        f"Question: {query}\nAnswer:"
                    )
                }
            ],
            model="llama3-8b-8192",
            temperature=0,
            top_p=1,
            stop=None,
            stream=False,
        )

        return chat_completion.choices[0].message.content

    def generate_follow_up_questions(self, query):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an assistant designed to generate relevant follow-up questions about HIV. "
                        "Provide exactly 3 clear and focused follow-up questions based on the user's query. "
                        "Each question should be on a new line, and the response should not include any extra text or numbering. "
                        "Ensure the questions are directly related to the topic."
                    )
                },
                {
                    "role": "user",
                    "content": f"Based on this question: '{query}', generate 3 relevant follow-up questions that user might want to ask."
                }
            ],
            model="llama3-8b-8192",
            temperature=0.7,
            top_p=1,
            stop=None,
            stream=False,
        )
        
        response = chat_completion.choices[0].message.content
        questions = [q.strip() for q in response.split('\n') if q.strip()]
        return questions[:3]