---
title: "Enhancing Fine-Tuning Based Backdoor Defense with Sharpness-Aware Minimization"
collection: publications
permalink: /publication/FT_SAM
# excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2023-07-13
venue: '2023 International Conference on Computer Vision'
paperurl: 'https://arxiv.org/pdf/2304.11823'
citation: 'Zhu, Mingli, et al. "Enhancing Fine-Tuning Based Backdoor Defense with Sharpness-Aware Minimization." 2023 International Conference on Computer Vision"'
---

Backdoor defense, which aims to detect or mitigate the effect of malicious triggers introduced by attackers, is becoming increasingly critical for machine learning security and integrity. Fine-tuning based on benign data is a natural defense to erase the backdoor effect in a backdoored model. However, recent studies show that, given limited benign data, vanilla fine-tuning has poor defense performance. In this work, we provide a deep study of fine-tuning the backdoored model from the neuron perspective and find that backdoorrelated neurons fail to escape the local minimum in the fine-tuning process. Inspired by observing that the backdoorrelated neurons often have larger norms, we propose FTSAM, a novel backdoor defense paradigm that aims to shrink the norms of backdoor-related neurons by incorporating sharpness-aware minimization with fine-tuning. We demonstrate the effectiveness of our method on several benchmark datasets and network architectures, where it achieves state-of-the-art defense performance. Overall, our work provides a promising avenue for improving the robustness of machine learning models against backdoor attacks.

<div class="img-hover-zoom">
        <img src="/images/iccv2023_FT_SAM.png" height="455" width="808" class="article-banner" alt="Enhancing Fine-Tuning Based Backdoor Defense with Sharpness-Aware Minimization" loading="lazy">
</div>