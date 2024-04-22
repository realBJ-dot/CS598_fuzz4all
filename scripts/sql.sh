python Fuzz4All/fuzz.py --config config/full_run/sql_innodb.yaml main_with_config \
                            --folder outputs/sql-demo/ \
                            --batch_size 5 \
                            --model_name bigcode/starcoderbase-1b \
                            --target /home/v8/v8/out/x64.debug/d8
