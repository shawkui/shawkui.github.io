---
title: "Neural Polarizer: A Lightweight and Effective Backdoor Defense via Purifying Poisoned Features"
collection: publications
permalink: /publication/NPD
# excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2023-09-22
venue: 'Conference on Neural Information Processing Systems'
venue_short: 'NeurIPS'
thumbnail: 'npd.png'
authors: ['Mingli Zhu', 'Shaokui Wei', 'Hongyuan Zha', 'Baoyuan Wu']
codeurl: 'https://github.com/SCLBD/BackdoorBench/blob/main/defense/npd.py'
paperurl: 'https://arxiv.org/pdf/2306.16697'
citation: 'Zhu, Mingli, Shaokui Wei (co-first author), et al. "Neural Polarizer: A Lightweight and Effective Backdoor Defense via Purifying Poisoned Features." Thirty-seventh Conference on Neural Information Processing Systems. NeurIPS 2023.'
---

Recent studies have demonstrated the susceptibility of deep neural networks to backdoor attacks. Given a backdoored model, its prediction of a poisoned sample with trigger will be dominated by the trigger information, though trigger information and benign information coexist. Inspired by the mechanism of the optical polarizer that a polarizer could pass light waves with particular polarizations while filtering light waves with other polarizations, we propose a novel backdoor defense method by inserting a learnable neural polarizer into the backdoored model as an intermediate layer, in order to purify the poisoned sample via filtering trigger information while maintaining benign information. The neural polarizer is instantiated as one lightweight linear transformation layer, which is learned through solving a well designed bi-level optimization problem, based on a limited clean dataset. Compared to other fine-tuning-based defense methods which often adjust all parameters of the backdoored model, the proposed method only needs to learn one additional layer, such that it is more efficient and requires less clean data. Extensive experiments demonstrate the effectiveness and efficiency of our method in removing backdoors across various neural network architectures and datasets, especially in the case of very limited clean data.
