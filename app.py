import gradio as gr
from transformers import pipeline

# 🔥 Load Hugging Face model (no API key needed)
generator = pipeline("text-generation", model="distilgpt2")

def explain_code(code, mode):
    if not code.strip():
        return "⚠️ Enter code."

    try:
        prompt = f"Explain this code:\n{code}\nExplanation:"

        result = generator(
            prompt,
            max_length=200,
            num_return_sequences=1
        )

        return result[0]["generated_text"]

    except Exception as e:
        return f"Error: {str(e)}"

# 🎨 UI
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# 💻 AI Code Explainer 🚀")
    gr.Markdown("Now powered by Hugging Face 🤗 (No API issues!)")

    with gr.Row():
        with gr.Column():
            code_input = gr.Textbox(lines=12, label="Paste Code")
            mode = gr.Radio(
                ["Beginner", "Detailed", "ELI5", "With Complexity"],
                value="Beginner"
            )
            btn = gr.Button("Explain ⚡")

        with gr.Column():
            output = gr.Textbox(lines=15, label="Explanation")

    btn.click(explain_code, inputs=[code_input, mode], outputs=output)

app.launch()
