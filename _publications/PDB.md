---
title: "Mitigating Backdoor Attack by Injecting Proactive Defensive Backdoor"
collection: publications
permalink: /publication/PDB
# excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2024-09-26
venue: 'Thirty-eighth Conference on Neural Information Processing Systems. NeurIPS 2024.'
paperurl: 'https://arxiv.org/pdf/2405.16112'
citation: 'Wei, Shaokui, et al. "Mitigating Backdoor Attack by Injecting Proactive Defensive Backdoor." Thirty-eighth Conference on Neural Information Processing Systems. NeurIPS 2024.'
---

Data-poisoning backdoor attacks are serious security threats to machine learning models, where an adversary can manipulate the training dataset to inject backdoors into models. In this paper, we focus on in-training backdoor defense, aiming to train a clean model even when the dataset may be potentially poisoned. Unlike most existing methods that primarily detect and remove/unlearn suspicious samples to mitigate malicious backdoor attacks, we propose a novel defense approach called PDB (Proactive Defensive Backdoor). Specifically, PDB leverages the "home field" advantage of defenders by proactively injecting a defensive backdoor into the model during training. Taking advantage of controlling the training process, the defensive backdoor is designed to suppress the malicious backdoor effectively while remaining secret to attackers. In addition, we introduce a reversible mapping to determine the defensive target label. During inference, PDB embeds a defensive trigger in the inputs and reverses the model's prediction, suppressing malicious backdoor and ensuring the model's utility on the original task. Experimental results across various datasets and models demonstrate that our approach achieves state-of-the-art defense performance against a wide range of backdoor attacks.

<div class="img-hover-zoom">
        <img src="/images/pdb.png" height="455" width="808" class="article-banner" alt="Backdoor Mitigation by Unlearning Shared Adversarial Examples" loading="lazy">
</div>