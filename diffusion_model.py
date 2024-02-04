import torch
from torch import autocast
# from diffusers import StableDiffusionPipeline
# from deep_translator import GoogleTranslator
import matplotlib.pyplot as plt
from torchao.quantization import quant_api

from diffusers import StableDiffusionPipeline

# torch._inductor.config.conv_1x1_as_mm = True
# torch._inductor.config.coordinate_descent_tuning = True
# torch._inductor.config.epilogue_fusion = False
# torch._inductor.config.coordinate_descent_check_all_directions = True


# CompVis/stable-diffusion-v1-4
# runwayml/stable-diffusion-v1-5
class StableDiffusion:
    def __init__(self, modelid="CompVis/stable-diffusion-v1-4"): 
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = StableDiffusionPipeline.from_pretrained(modelid, torch_dtype=torch.float16)
        # self.pipe = torch.nn.DataParallel(self.pipe)
        self.pipe.to("cuda:1")
        # Combine attention projection matrices.
        # self.pipe.unet.to(memory_format=torch.channels_last)
        # self.pipe.vae.to(memory_format=torch.channels_last)

        # self.pipe.unet = torch.compile(self.pipe.unet, mode="max-autotune", fullgraph=True)
        # self.pipe.vae.decode = torch.compile(self.pipe.vae.decode, mode="max-autotune", fullgraph=True)

    def generate_img(self, text_prompt):
        image = self.pipe(text_prompt).images[0]
        return image

# stablePipeline = StableDiffusion()

