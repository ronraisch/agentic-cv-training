# Autoencoders, VAEs, ELBO, GANs and diffusion

[All training](index.md) · [Source coverage](sources.md)

## A plausible reconstruction may still invent a letter

A blurred crop might be consistent with either a P or an R. A generative model can produce a crisp version of one letter, but the visual improvement does not establish which letter the sensor originally observed.

![Sharper does not mean truer. Ambiguous input; Possible reconstruction A; Possible reconstruction B](assets/dl-generative-toy.svg)

The output reflects both the input and the model’s learned assumptions about plausible images. That is useful in synthesis and some restoration settings. In OCR, identification or remote-sensing measurement, the distinction between inferred detail and observed evidence may be essential.

Autoencoders, VAEs, GANs and diffusion models make different choices about how to learn and use such image distributions.

<details>
<summary>Jump to a concept</summary>

- [Learning to model observations](#learning-to-model-observations)

- [Autoencoders](#autoencoders)

- [Variational autoencoders and ELBO](#variational-autoencoders-and-elbo)

- [Generative adversarial networks](#generative-adversarial-networks)

- [Autoregressive and diffusion models](#autoregressive-and-diffusion-models)

- [Where this material fits](#where-this-material-fits)

</details>

## Learning to model observations

A generative model describes or samples an observation distribution. Useful applications include conditional image synthesis, restoration, simulation and representation learning. Realistic images alone do not establish that the model learned the target distribution or preserved an input's identity. A generated detail is a model hypothesis, not a measurement recovered from the sensor.

## Autoencoders

An autoencoder maps x to a latent code z and reconstructs x from it. A bottleneck, noise or other constraints encourage the code to preserve selected structure rather than copy input trivially. Pixel reconstruction loss favors some information differently from a semantic objective. A low reconstruction error need not produce a useful classification embedding, and a high error can arise from a new camera rather than an anomalous object.

## Variational autoencoders and ELBO

A VAE uses a prior p(z), a decoder distribution p_theta(x|z) and an approximate posterior q_phi(z|x). Its evidence lower bound is `E_q[log p_theta(x|z)] - KL(q_phi(z|x) || p(z))`. The difference between log p_theta(x) and this bound is a nonnegative KL divergence to the true posterior. The first term rewards reconstruction likelihood; the second regularizes the latent distribution. A deterministic reconstruction penalty is not automatically the same as a specified likelihood without assumptions about output noise.

For a Gaussian approximate posterior, the reparameterization `z = mu + sigma*epsilon` with epsilon sampled from a standard Gaussian allows gradients through mu and sigma. A strong decoder may ignore latent variables, and changing the balance of reconstruction and KL changes the model's behavior. Show both generated samples and reconstruction/latent diagnostics.

## Generative adversarial networks

A GAN trains a generator to produce samples and a discriminator to distinguish generated from real examples. In the original minimax form, discriminator training and generator training optimize opposing objectives. The original saturating generator loss can provide weak gradients when the discriminator confidently rejects poor samples. A common nonsaturating alternative maximizes the discriminator's log probability of generated samples being real. Other losses change the game and its stability.

Generator loss decreasing does not prove sample quality improves: the discriminator may simply be weak. Mode collapse produces a narrow variety of convincing outputs. Training can oscillate because both objectives change as the opponent changes. Evaluate diversity, conditional consistency and downstream use, not one loss trace. Pix2pix uses paired conditional data; CycleGAN uses unpaired domains with cycle-consistency and adversarial terms. Cycle consistency does not guarantee truthful recovery of medically or geographically meaningful details.

## Autoregressive and diffusion models

An autoregressive model factors a joint distribution into ordered conditional predictions. It can optimize likelihood but generation may require a sequence of steps. A diffusion model adds noise through a defined forward process and learns a reverse denoising/score-related process. Training often predicts noise, clean signal or a parameterized combination. Sampling choices trade compute and quality and must match the model's assumptions.

Conditioning with text, masks or images changes which distribution is modeled. Guidance can strengthen conditioning while reducing diversity or increasing artifacts. Evaluate on held-out conditions and check whether identity, geometry or small objects are preserved. A sharpened image can look more detailed while inventing structure.

## Where this material fits

The generative-model lectures and optional ELBO explanation remain part of the reading route; the historical diffusion implementation remains optional. For the current tasks, the important distinction is what a reconstruction preserves and what it infers. That provides a concrete reason to understand the model objectives even without training a generator.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [https://cs231n.stanford.edu/slides/2025/lecture_13.pdf](https://cs231n.stanford.edu/slides/2025/lecture_13.pdf)

- [https://cs231n.stanford.edu/slides/2025/lecture_14.pdf](https://cs231n.stanford.edu/slides/2025/lecture_14.pdf)

- [https://yunfanj.com/blog/2021/01/11/ELBO.html](https://yunfanj.com/blog/2021/01/11/ELBO.html)

</details>
