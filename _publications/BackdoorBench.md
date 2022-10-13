---
title: "BackdoorBench: A Comprehensive Benchmark of Backdoor Learning"
collection: publications
permalink: /publication/BackdoorBench
# excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2022-10-12
venue: 'NeurIPS 2022 Track Datasets and Benchmarks'
paperurl: 'https://openreview.net/forum?id=31_U7n18gM7'
citation: 'Wu, Baoyuan, et al. "BackdoorBench: A Comprehensive Benchmark of Backdoor Learning." NeurIPS 2022 Track Datasets and Benchmarks.'
---

<div class="img-hover-zoom">
        <img src="/images/nips2022_benchmakr.png" height="455" width="808" class="article-banner" alt="BackdoorBench: A Comprehensive Benchmark of Backdoor Learning" loading="lazy">
</div>

Backdoor learning is an emerging and vital topic for studying deep neural networks' vulnerability (DNNs). Many pioneering backdoor attack and defense methods are being proposed, successively or concurrently, in the status of a rapid arms race. However, we find that the evaluations of new methods are often unthorough to verify their claims and accurate performance, mainly due to the rapid development, diverse settings, and the difficulties of implementation and reproducibility.  Without thorough evaluations and comparisons, it is not easy to track the current progress and design the future development roadmap of the literature. To alleviate this dilemma, we build a comprehensive benchmark of backdoor learning called BackdoorBench. It consists of an extensible modular-based codebase (currently including implementations of 8 state-of-the-art (SOTA) attacks and 9 SOTA defense algorithms) and a standardized protocol of complete backdoor learning. We also provide comprehensive evaluations of every pair of 8 attacks against 9 defenses, with 5 poisoning ratios, based on 5 models and 4 datasets, thus 8,000 pairs of evaluations in total. We present abundant analysis from different perspectives about these 8,000 evaluations, studying the effects of different factors in backdoor learning.  All codes and evaluations of BackdoorBench are publicly available at <a href="https://backdoorbench.github.io"><u>https://backdoorbench.github.io</u></a>.

