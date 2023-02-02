#! /bin/bash
cd examples/translation/
bash prepare-iwslt14.sh
cd ../..
TEXT=examples/translation/iwslt14.tokenized.de-en

fairseq-preprocess \
    --source-lang de --target-lang en \
    --trainpref $TEXT/trainoutput --validpref $TEXT/valid --testpref $TEXT/outtest \
    --destdir data-bin/iwslt14.tokenized.de-en \
    --workers 20
