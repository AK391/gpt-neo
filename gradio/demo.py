import gradio as gr

title = "GPT-Neo Demo"
description = "demo for GPT-Neo by EleutherAI for text generation. To use it, simply add your text, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='http://github.com/eleutherai/gpt-neo'>GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow</a></p>"
examples = [
    ['The tower is 324 metres (1,063 ft) tall,'],
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"]
]

gr.Interface.load("huggingface/EleutherAI/gpt-neo-2.7B", inputs=gr.inputs.Textbox(lines=5, label="Input Text"),title=title,description=description,article=article, examples=examples).launch()