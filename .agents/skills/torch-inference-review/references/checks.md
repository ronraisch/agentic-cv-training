# Checks

Test repeated calls, empty batches, bad shape, nonfinite and integer inputs, input mutation, caller mode restoration on error, CPU outputs and requires_grad=False. Separate eval from inference_mode. Bound retained output memory and batch size. Record seed, model version and preprocessing; cross-device determinism is not guaranteed.
