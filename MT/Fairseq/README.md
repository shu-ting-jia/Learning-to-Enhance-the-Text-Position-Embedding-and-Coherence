# Learning-to-Enhance-the-Text-Position-Embedding-and-Coherence
This repository is developed under Fairseq framework.

## Installation
```
> pip install --editable ./ 
> pip install -r requirements.txt
> pip install torch==1.10.0+cu111 torchvision==0.11.0+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
> pip install packaging
> pip install sacrebleu==1.5.1
> pip install numpy==1.23.2
> pip install sklearn
> pip install -U scikit-learn scipy matplotlib
> pip install sacremoses
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
> bash examples/translation/preprocess_iwslt14_de_en.sh
```
* WMT'14 En-DE
```
> bash examples/translation/preprocess_wmt14_en_de.sh
```

## Model training
* IWSLT'14 De-En
```
> bash examples/translation/train_transformer.sh
```
* WMT'14 En-De
```
> bash examples/translation/train_transformer_wmt14.sh \
 
```

## Performance evaluation
* IWSLT'14 De-En
```
> bash examples/translation/evaluate_transformer.sh
```
* WMT'14 En-De
```
> bash examples/translation/evaluate_transformer.sh \
  --dataset wmt14_en_de
> bash ./scripts/compound_split_bleu.sh \
  ./checkpoints/wmt14_en_de/transformer/evaluate/evaluate.log
```

## Pretraining weight
* 

  |Dataset|BLEU|Pretrained weights|
  |:------:|:--:|:----------------:|
  |WMT'14 En-De|28.18|[Download](https://drive.google.com/file/d/1F_hHJ5TaKKmp2hOUUjT0jnC2sALD4fof/view?usp=share_link)|
  |IWSLT'14 De-En|34.91|[Download](https://drive.google.com/file/d/1ux5JCGxialLAlBYwp66RqH79_QGijVjp/view?usp=share_link)|
  


