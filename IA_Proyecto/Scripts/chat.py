import google.generativeai as genai

genai.configure(api_key= "AIzaSyAIX6cpg4U-2daYAamAAh0TQZZw_W0sBRk")
model = genai.GenerativeModel('gemini-pro')
history = []

while(True):
    question = input("Enter a prompt: ")
    if question.lower == "salir":
        break
    history.append({'role':'user','content':question})
    response = model.generate_content(question)
    history.append({'role':'assistant','content':response})
    print(response.text)
    

