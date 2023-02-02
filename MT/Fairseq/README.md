# Learning-to-Enhance-the-Text-Position-Embedding-and-Coherence
This repository is developed under Fairseq framework.

## Installation
```
> pip install --editable ./ 
> pip install -r requirements.txt
```
```
> git clone https://github.com/NVIDIA/apex
> cd apex
> pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" \
  --global-option="--deprecated_fused_adam" --global-option="--xentropy" \
  --global-option="--fast_multihead_attn" ./
```

> Note: CUDA version=11.1

## Data preprocessing
* IWSLT'14 De-En
```
> ./examples/translation/preprocess_iwslt14_de_en.sh
```
* WMT'14 En-DE
```
> ./examples/translation/preprocess_wmt14_en_de.sh
```

## Model training
* IWSLT'14 De-En
```
> ./examples/translation/train_disentangled_transformer.sh
```
* WMT'14 En-De
```
> ./examples/translation/train_disentangled_transformer.sh \
  --dataset wmt14_en_de
```

## Performance evaluation
* IWSLT'14 De-En
```
> ./examples/translation/evaluate_disentangled_transformer.sh
```
* WMT'14 En-De
```
> ./examples/translation/evaluate_disentangled_transformer.sh \
  --dataset wmt14_en_de
> bash ./scripts/compound_split_bleu.sh \
  ./checkpoints/wmt14_en_de/disentangled_transformer/evaluate/evaluate.log
```

