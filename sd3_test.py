from diffusers import StableDiffusionPipeline
import torch

model_id = "stabilityai/stable-diffusion-3-medium"

# Hugging Face API 토큰을 사용하여 인증
from huggingface_hub import login
login(token="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")

pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True)
pipe = pipe.to("cuda")  # GPU가 없는 경우 "cpu"로 변경

prompt = "맑은 날 해바라기 밭의 그림"
image = pipe(prompt).images[0]

# 이미지 저장 또는 표시
image.save("output.png")
image.show()
