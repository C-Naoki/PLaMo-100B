# PLaMo-100B
- [About](#about)
- [What is PLaMo-100B?](#what-is-plamo-100b)
  - [What is the post-training process?](#what-is-the-post-training-process)
- [Acknowledgement](#acknowledgement)
- [References](#references)

## About
This repository is unofficial Python implementation to demonstrate PLaMo-100B.

## What is PLaMo-100B?
PLaMo-100B is the Large Language Model developed in-house by [Preferred Elements](https://www.preferred.jp/en/) (a subsidiary of [Preferred Networks](https://www.preferred.jp/en/)).
This model has been developed since Februrary 2024, and the post-training process has just been completed on August 7, 2024.
The 100B in the model name stands for the number of parameters, namely <u>**100 billion**</u>.

The PLaMo-100B-Instruct, where the model post-training is completed, outperformed the GPT-4 model on [Jaster](https://github.com/llm-jp/llm-jp-eval/tree/g-leaderboard). Note that Jaster is a benchmark dataset for Japanese language models. Additionally, the PLaMo-100B-Instruct also achieved a higher score than the GPT-4 model on [Rakuda benchmark](https://github.com/yuzu-ai/japanese-llm-ranking), which is used to evaluate how well models can handle insights into the nuances of Japanese language.

### What is the post-training process?
The post-training process is a process to further train the model using a large amount of data after the initial training. The post-training process is used to improve the performance of the model on specific tasks or datasets.

## Acknowledgement
We appreciate that the Preferred Networks offered the API to access the PLaMo-100B model.

## References
[1] [1,000億パラメータの独自LLM「PLaMo-100B」の事後学習が完了](https://tech.preferred.jp/ja/blog/plamo-100b-post-training/) \
[2] [PFEが開発する大規模言語モデルPLaMo β版の無料トライアルの申込受付を開始](https://www.preferred.jp/ja/news/pr20240807/)
