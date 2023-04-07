from transformers import AutoTokenizer, BloomForCausalLM
from transformers import BloomConfig, BloomModel

# model = BloomForCausalLM.from_pretrained("bigscience/bloom-560m")
tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-560m")
inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")

configuration = BloomConfig()
model = BloomForCausalLM(configuration)

model = BloomModel(configuration)
model.prepare_decoder_input_ids_from_labels()