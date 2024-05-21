import gradio as gr
inputs = [
    gr.Dropdown(choices=X.columns.tolist(), label="Location"),
    gr.Number(label="Square Footage (sqft)"),
    gr.Number(label="Bathrooms"),
    gr.Number(label="Bedrooms (BHK)")
]


iface=gr.Interface(fn=predict_price,inputs=inputs,outputs='text',title="Banglore House Price Predictor",
    live=True,
    theme="light").launch()