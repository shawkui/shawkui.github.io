---
title: "Unveiling and Mitigating Backdoor Vulnerabilities based on Unlearning Weight Changes and Backdoor Activeness"
collection: publications
permalink: /publication/TSBD
# excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2024-09-26
venue: 'Thirty-eighth Conference on Neural Information Processing Systems. NeurIPS 2024.'
paperurl: 'https://arxiv.org/pdf/2405.20291'
citation: 'Lin, Weilin, et al. "Unveiling and Mitigating Backdoor Vulnerabilities based on Unlearning Weight Changes and Backdoor Activeness." Thirty-eighth Conference on Neural Information Processing Systems. NeurIPS 2024.'
---

The security threat of backdoor attacks is a central concern for deep neural networks (DNNs). Recently, without poisoned data, unlearning models with clean data and then learning a pruning mask have contributed to backdoor defense. Additionally, vanilla fine-tuning with those clean data can help recover the lost clean accuracy. However, the behavior of clean unlearning is still under-explored, and vanilla fine-tuning unintentionally induces back the backdoor effect. In this work, we first investigate model unlearning from the perspective of weight changes and gradient norms, and find two interesting observations in the backdoored model: 1) the weight changes between poison and clean unlearning are positively correlated, making it possible for us to identify the backdoored-related neurons without using poisoned data; 2) the neurons of the backdoored model are more active (i.e., larger changes in gradient norm) than those in the clean model, suggesting the need to suppress the gradient norm during fine-tuning. Then, we propose an effective two-stage defense method. In the first stage, an efficient Neuron Weight Change (NWC)-based Backdoor Reinitialization is proposed based on observation 1). In the second stage, based on observation 2), we design an Activeness-Aware Fine-Tuning to replace the vanilla fine-tuning. Extensive experiments, involving eight backdoor attacks on three benchmark datasets, demonstrate the superior performance of our proposed method compared to recent state-of-the-art backdoor defense approaches.

<div class="img-hover-zoom">
        <img src="/images/tsbd.png" height="455" width="808" class="article-banner" alt="Backdoor Mitigation by Unlearning Shared Adversarial Examples" loading="lazy">
</div>