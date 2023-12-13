python3 -u run_language_modeling.py \
                                --output_dir=your_model_path \
                                --model_type=gpt2 \
                                --model_name_or_path=gpt2 \
                                --do_train \
                                --train_data_file=./train.txt \
                                --do_eval \
                                --eval_data_file=./valid.txt \
                                --per_device_train_batch_size=2 \
                                --per_device_eval_batch_size=2 \
                                --line_by_line \
                                --evaluate_during_training \
                                --learning_rate 5e-5 \
                                --num_train_epochs=5
