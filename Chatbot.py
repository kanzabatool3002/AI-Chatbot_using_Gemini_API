
import google.generativeai as genai 
import tkinter as tk 
from tkinter import scrolledtext, PhotoImage

GENAI_API_KEY = "Your API Key"
genai.configure(api_key=GENAI_API_KEY)

def generate_response(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query, generation_config=genai.GenerationConfig(
            
            temperature=0.1,))
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

def send_message():
    """Handle sending the user input and displaying AI response."""
    user_input = input_box.get().strip()  
    if user_input:
        user_input_with_instruction = f"{user_input} (give me a short response)"
        conversation_area.image_create(tk.END, image=user_icon)  
        conversation_area.insert(tk.END, f"  {user_input}\n", "user")  
        conversation_area.see(tk.END)

        response = generate_response(user_input_with_instruction) 
        conversation_area.image_create(tk.END, image=ai_icon)  
        conversation_area.insert(tk.END, f"  {response}\n", "ai")  
        conversation_area.see(tk.END)

        input_box.delete(0, tk.END) 
        root.update()  

def start_conversation():
    """Start the conversation with an initial AI greeting."""
    conversation_area.image_create(tk.END, image=ai_icon)  
    conversation_area.insert(tk.END, "  Hi, How can I assist you today?\n\n", "ai")
    conversation_area.see(tk.END)

root = tk.Tk()
root.title("AI Chatbot")

conversation_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30, background="black", font=("Arial", 16))
conversation_area.pack(padx=10, pady=10)

ai_icon = PhotoImage(file="ai-icon.png")  
ai_icon = ai_icon.subsample(20, 20)
user_icon = PhotoImage(file="user-icon.png")  
user_icon = user_icon.subsample(20, 16)

conversation_area.tag_configure("ai", foreground="green", background="black")
conversation_area.tag_configure("user", foreground="yellow", background="black")

input_box = tk.Entry(root, width=70, font=("Arial", 18))
input_box.pack(padx=10, pady=10, side=tk.LEFT)

send_icon = PhotoImage(file="sendIcon.png")  
send_icon = send_icon.subsample(14, 14)
send_button = tk.Button(root, image=send_icon, command=send_message, borderwidth=0, relief="flat")
send_button.pack(padx=5, pady=5, side=tk.LEFT)

start_conversation()

root.mainloop()

