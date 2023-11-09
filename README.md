# OptiGuide: Large Language Models for Scheduling

> Scheduling is a key problem and here's an effort to use OptiGuide which is used to solve the Operations Ressearch or Optimization problems in scheduling context.


This repository includes the following material to open source the OptiGuide project:
- Research code base for the OptiGuide framework in the [optiguide/optiguide.py](optiguide/optiguide.py) file.
- A demo notebook of the OptiGuide framework [notebook/optiguide_example.ipynb](notebook/optiguide_example.ipynb)
- Benchmarks (dataset) in [benchmark/](benchmark/) for evaluating language models for supply chain applications
- [ ] Benchmark utils for future evaluation.
- [ ] Create a GitHub release for the benchmark.

**Reference**
Please cite the paper if you use this code in your own work:
```latex
@article{li2023large,
  title={Large Language Models for Supply Chain Optimization},
  author={Li, Beibin and Mellou, Konstantina and Zhang, Bo and Pathuri, Jeevan and Menache, Ishai},
  journal={arXiv preprint arXiv:2307.03875},
  year={2023}
}
```

## Setup for the OptiGuide Code

### Installation
Once Python is installed, just run `pip install optiguide` to install OptiGuide.

Here is the [Pypi page](https://pypi.org/project/OptiGuide/) for more information.

### Tutorial Option 1: Run from Colab Directly
1. Check the Colab Notebook:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13eMJOcy79mhyEUYicSmbEm63KS7mzi33?usp=sharing)
2. Create a `OAI_CONFIG_LIST` file inside the Colab environment, so that it can connect to the OpenAI service.
  ```json
  [
      {
          "model": "gpt-4",
          "api_key": "Your API Key Comes Here",
          "api_type": "azure",
          "api_base": "The API base URL",
          "api_version": "2023-03-15-preview"
      }
  ]
  ```
1. Now, you can run the Colab Code.

### Tutorial Option 2: Run Locally
1. Install Python and Python packages `pip install optiguide`
2. Install and setup "Gurobi Optimizer" from [Gurobi's official website](https://www.gurobi.com/downloads/gurobi-software/), and you can get a trial license for academic use. Make sure the license is setup correctly.
3. Run OptiGuide example, you can setup the OpenAI API (key and secret) and then test the code with Jupyter notebook [example](`notebook/optiguide_example.ipynb`).
  Example `notebook/OAI_CONFIG_LIST` file
  ```json
  [
      {
          "model": "gpt-4",
          "api_key": "Your API Key Comes Here",
          "api_type": "azure",
          "api_base": "The API base URL",
          "api_version": "2023-03-15-preview"
      }
  ]
  ```


## Implementation
### OptiGuide Implementation
We re-implemented OptiGuide for research purposes using [autogen](https://github.com/microsoft/autogen), a framework that enables the development of LLM applications with multiple agents that can converse with each other to solve tasks.

### Evaluation Implementation
We simplified the evaluation process by using Gurobi and Gurobi examples, as detailed below.

## Benchmark Dataset
Subsequently, we manually crafted questions and provided the ground truth answer code for each question. These labeled questions and answers can be found in the [benchmark/macro](benchmark/macro/) folder.

Additionally, we developed a Scheduling application to showcase the OptiGuide framework as described in our paper.


**We acknowledge that both human and machine may contain errors while generating this benchmark. If you identify any inaccuracies, feel free to open an issue or submit a pull request for correction.**

