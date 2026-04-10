from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

response = llm.invoke("Hello! your last trianing date ? ")
print(response)

























# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app=FastAPI()
# @app.get('/health')
# def get_data():
#     return {'message':'Hi I am working'}
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )




# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)