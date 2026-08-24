import plotly.graph_objects as go
from plotly.subplots import make_subplots
import textwrap

# ---- Sample paragraph (or read from file) ----
paragraph = "The quick brown fox jumps over the lazy dog. This is a classic pangram used to test fonts and typing skills. It contains every letter of the English alphabet at least once."

# ---- Define steps with descriptions and code snippets ----
steps = [
    {
        "label": "Input\nParagraph",
        "desc": "Raw text from file\nor user input.",
        "code": "paragraph = Path(__file__).parent / 'sample_paragraph.txt'\nparagraph = paragraph.read_text().strip()",
        "x": 0, "y": 0
    },
    {
        "label": "Add Prefix\n'summarize: '",
        "desc": "T5 requires a task prefix\nto know the operation.",
        "code": "prompt = 'summarize: ' + paragraph",
        "x": 1, "y": 0
    },
    {
        "label": "Tokenizer",
        "desc": "Convert text to\nPyTorch tensors on device.",
        "code": "inputs = tokenizer(prompt, return_tensors='pt', truncation=True)\ninputs = {k: v.to(device) for k, v in inputs.items()}",
        "x": 2, "y": 0
    },
    {
        "label": "T5 Model\n(Generate)",
        "desc": "Model generates token IDs\nwith `max_new_tokens=50`.",
        "code": "with torch.no_grad():\n    outputs = model.generate(**inputs, max_new_tokens=50)",
        "x": 3, "y": 0
    },
    {
        "label": "Decode",
        "desc": "Convert token IDs back\nto human-readable text.",
        "code": "summary = tokenizer.decode(outputs[0], skip_special_tokens=True)",
        "x": 4, "y": 0
    },
    {
        "label": "Summary\nOutput",
        "desc": "Final summarized text.",
        "code": "print(summary)",
        "x": 5, "y": 0
    }
]

# ---- Create figure ----
fig = go.Figure()

# Add nodes as scatter traces (one trace per node for individual hover)
for i, step in enumerate(steps):
    fig.add_trace(go.Scatter(
        x=[step["x"]],
        y=[step["y"]],
        mode="markers+text",
        marker=dict(size=40, color="lightblue", line=dict(color="black", width=2)),
        text=step["label"],
        textposition="middle center",
        textfont=dict(size=10, color="black"),
        hovertext=f"<b>{step['label'].replace('\n', ' ')}</b><br><br>"
                  f"<i>Description:</i><br>{step['desc']}<br><br>"
                  f"<i>Code snippet:</i><br>{step['code']}",
        hoverinfo="text",
        name=step["label"].replace("\n", " ")
    ))

# Add arrows between nodes
for i in range(len(steps) - 1):
    x0, y0 = steps[i]["x"], steps[i]["y"]
    x1, y1 = steps[i+1]["x"], steps[i+1]["y"]
    fig.add_annotation(
        x=(x0 + x1) / 2,
        y=(y0 + y1) / 2,
        ax=x0,
        ay=y0,
        xref="x", yref="y",
        axref="x", ayref="y",
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=2,
        arrowcolor="gray"
    )

# ---- Layout ----
fig.update_layout(
    title="T5 Summarization Pipeline (Interactive)",
    xaxis=dict(showgrid=False, zeroline=False, visible=False, range=[-0.5, 5.5]),
    yaxis=dict(showgrid=False, zeroline=False, visible=False, range=[-0.5, 0.5]),
    hoverlabel=dict(font_size=12, font_family="Courier New"),
    width=900,
    height=400,
    margin=dict(l=20, r=20, t=50, b=20)
)

# Show the figure
fig.show()

# Optionally save as HTML for sharing
# fig.write_html("t5_pipeline.html")