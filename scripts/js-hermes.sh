python Fuzz4All/fuzz.py --config config/full_run/javascript_hermes.yaml main_with_config \
                            --folder outputs/js-hermes-demo-few-shot-v3/ \
                            --batch_size 5 \
                            --model_name bigcode/starcoderbase-1b \
                            --target /home/hermes_workingdir/build/bin/hermes
