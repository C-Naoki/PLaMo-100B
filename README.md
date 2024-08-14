# PLaMo-100B
- [ℹ️ About](#ℹ️-about)
- [🧐 What is PLaMo-100B?](#-what-is-plamo-100b)
  - [What is the post-training process?](#what-is-the-post-training-process)
- [🙏 Acknowledgement](#-acknowledgement)
- [🙋‍♂️ Support](#️-support)
- [📗 References](#-references)

## ℹ️ About
This repository is an unofficial Python implementation to demonstrate PLaMo-100B.
If you want to quickly try its demo, let's visit the [website](https://plamo100b-demo.streamlit.app/)! (Please note that the trial API for the website is available for a limited time only. After the trial period ends, access to the API will no longer be available. I appreciate your understanding.)

## 🧐 What is PLaMo-100B?
PLaMo-100B is the Large Language Model developed in-house by [Preferred Elements](https://www.preferred.jp/en/) (a subsidiary of [Preferred Networks](https://www.preferred.jp/en/)).
This model has been developed since Februrary 2024, and the post-training process has just been completed on August 7, 2024.
The 100B in the model name stands for the number of parameters, namely <u>**100 billion**</u>.

PLaMo-100B-Instruct, where the model post-training is completed, outperformed the GPT-4 model on [Jaster](https://github.com/llm-jp/llm-jp-eval/tree/g-leaderboard). Note that Jaster is a benchmark dataset for Japanese language models. Additionally, PLaMo-100B-Instruct also achieved a higher score than the GPT-4 model on [Rakuda benchmark](https://github.com/yuzu-ai/japanese-llm-ranking), which is used to evaluate how well models can handle insights into the nuances of Japanese language.

### What is the post-training process?
The post-training process is a process to further train the model using a large amount of data after the initial training. The post-training process is used to improve the performance of the model on specific tasks or datasets.

## 🙏 Acknowledgement
I appreciate that Preferred Networks offered the trial API to access PLaMo-100B model.

## 🙋‍♂️ Support
💙 If you like this app, give it a ⭐ and share it with friends!

## 📗 References
[1] [1,000億パラメータの独自LLM「PLaMo-100B」の事後学習が完了](https://tech.preferred.jp/ja/blog/plamo-100b-post-training/) \
[2] [PFEが開発する大規模言語モデルPLaMo β版の無料トライアルの申込受付を開始](https://www.preferred.jp/ja/news/pr20240807/)
