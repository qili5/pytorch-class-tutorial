<p align="center">
  <img src="pytorch-logo-dark.png" width="520" alt="PyTorch">
</p>

# PyTorch Class Tutorial

Teaching material for an introductory PyTorch course. Each file is a small,
self-contained script that runs on its own and prints its output, so it can be
walked through one slide at a time in class.

---

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python setup.py          # prints the PyTorch version and whether CUDA is available
```

---

## 1. Tensor fundamentals — [`tensor_fundamental/`](tensor_fundamental/)

The core PyTorch material, in teaching order.

**Creating tensors**

| File | Topic |
|---|---|
| [`create_tensor.py`](tensor_fundamental/create_tensor.py) | The simplest possible tensor |
| [`tensors.py`](tensor_fundamental/tensors.py) | Building tensors from Python lists |
| [`scalar_dim.py`](tensor_fundamental/scalar_dim.py) | Scalars, `ndim` and `shape` |
| [`vectors.py`](tensor_fundamental/vectors.py) | 1-D tensors |
| [`matrixs.py`](tensor_fundamental/matrixs.py) | 2-D tensors |
| [`zeros_ones.py`](tensor_fundamental/zeros_ones.py) | `torch.zeros()` and `torch.ones()` |
| [`range_like.py`](tensor_fundamental/range_like.py) | `torch.arange()`, `zeros_like()`, `ones_like()` |
| [`random_tensors.py`](tensor_fundamental/random_tensors.py) | `torch.rand()` |

**Operations**

| File | Topic |
|---|---|
| [`addition_subtraction.py`](tensor_fundamental/addition_subtraction.py) | Adding and subtracting |
| [`division_elementwise_multiplication.py`](tensor_fundamental/division_elementwise_multiplication.py) | Element-wise maths |
| [`matrix_multiplication.py`](tensor_fundamental/matrix_multiplication.py) | `torch.matmul()` |
| [`shape_errors.py`](tensor_fundamental/shape_errors.py) | Why shapes must line up |
| [`transpose.py`](tensor_fundamental/transpose.py) | Fixing shapes with `.T` |

**Aggregation**

| File | Topic |
|---|---|
| [`aggregation.py`](tensor_fundamental/aggregation.py) | `min()`, `max()`, `sum()`, `mean()` |
| [`mean_error.py`](tensor_fundamental/mean_error.py) | Why `mean()` fails on an integer tensor |
| [`mean_fix.py`](tensor_fundamental/mean_fix.py) | The fix: convert to `float32` |
| [`positional_min_max.py`](tensor_fundamental/positional_min_max.py) | `argmax()` and `argmin()` |

**Datatypes and devices**

| File | Topic |
|---|---|
| [`datatypes.py`](tensor_fundamental/datatypes.py) | `float16` / `float32` / `float64` / `int8`, memory and precision |
| [`datatype_error.py`](tensor_fundamental/datatype_error.py) | Dtype mismatch errors |
| [`datatype_error_fix.py`](tensor_fundamental/datatype_error_fix.py) | Fixing them with `.type()` |
| [`device_mismatch.py`](tensor_fundamental/device_mismatch.py) | CPU vs GPU tensors |

---

## 2. Working with APIs — [`api_tutorial/`](api_tutorial/)

Calling real web APIs with `requests`. Every API used here is free and needs no
key, so the scripts run as-is. Each one pairs a raw call with a structured
version.

| API | Raw call | Structured | What it teaches |
|---|---|---|---|
| arXiv | [`simple_api_call.py`](api_tutorial/simple_api_call.py) | [`arxiv_search.py`](api_tutorial/arxiv_search.py) | Parsing XML responses |
| Open-Meteo | [`simple_weather_call.py`](api_tutorial/simple_weather_call.py) | [`weather_app.py`](api_tutorial/weather_app.py) | JSON, and chaining two endpoints together |
| Iowa Environmental Mesonet | [`simple_iem_call.py`](api_tutorial/simple_iem_call.py) | [`iem_weather.py`](api_tutorial/iem_weather.py) | Table-shaped JSON, sparse fields, real observations |
| PokeAPI | — | [`pokemon.py`](api_tutorial/pokemon.py) | Nested JSON |
| Open Trivia DB | — | [`quiz_test.py`](api_tutorial/quiz_test.py) | Query parameters |

Running the weather scripts side by side makes a useful point: Open-Meteo
returns a computer model's **forecast**, while IEM (hosted by Iowa State)
returns **actual observations** from Iowa airport weather stations. They
disagree, and both are correct.

**Not web APIs** — these two use the Hugging Face *library* API and run models
locally:

- [`pipeline_basics.py`](api_tutorial/pipeline_basics.py) — `pipeline()` for sentiment analysis
- [`tokenizer_and_model.py`](api_tutorial/tokenizer_and_model.py) — the same work done manually, showing it is all PyTorch underneath

---

## 3. Hugging Face models — [`HF_project/`](HF_project/)

Loading pretrained transformer models and running them.

| File | Topic |
|---|---|
| [`loading_model.py`](HF_project/loading_model.py) | Downloading a checkpoint |
| [`tokenize_tensor.py`](HF_project/tokenize_tensor.py) | Text becomes tensors |
| [`translate_with_mt0.py`](HF_project/translate_with_mt0.py) | Translation with mT0 |
| [`summarize_with_t5.py`](HF_project/summarize_with_t5.py) | Summarisation with T5 |

---

## Requirements

`torch`, `transformers`, `sentencepiece`, `protobuf`, `requests` — see
[`requirements.txt`](requirements.txt).

A GPU is optional. Scripts that use one check `torch.cuda.is_available()` first
and fall back to the CPU.
