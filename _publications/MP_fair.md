---
title: "Mean Parity Fair Regression in RKHS"
collection: publications
permalink: /publication/MP_fair
# excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2023-01-20
venue: 'AISTATS 2023'
paperurl: 'https://proceedings.mlr.press/v206/wei23a/wei23a.pdf'
citation: 'Wei, Shaokui, et al. "Mean Parity Fair Regression in RKHS" AISTATS 2023.'
---

  We study the fair regression problem under the notion of Mean Parity (MP) fairness, which requires the conditional mean of the learned function output to be constant with respect to the sensitive attributes. We address this problem by leveraging reproducing kernel Hilbert space (RKHS) to construct the functional space whose members are guaranteed to satisfy the fairness constraints. The proposed functional space suggests a closed-form solution for the fair regression problem that is naturally compatible with multiple sensitive attributes. Furthermore, by formulating the fairness-accuracy tradeoff as a relaxed fair regression problem, we derive a corresponding regression function that can be implemented efficiently and provides interpretable tradeoffs. More importantly, under some mild assumptions, the proposed method can be applied to regression problems with a covariance-based notion of fairness.  Experimental results on benchmark datasets show the proposed methods achieve competitive and even superior performance compared with several state-of-the-art methods.  Codes are publicly available at <a href="https://github.com/shawkui/MP_Fair_Regression"><u>https://github.com/shawkui/MP_Fair_Regression</u></a>.

<div class="img-hover-zoom">
        <img src="/images/MP_demo.png" height="455" width="808" class="article-banner" alt="Mean Parity Fair Regression in RKHS" loading="lazy">
</div>
