# import requests

# response = requests.post(
#     f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
#     headers={
#         "authorization": f"sk-TR8ff584izCeMUKEATQpdUvs9L5W4z4eq6YKugVaEtHhQk4q",
#         "accept": "image/*"
#     },
#     files={"none": ''},
#     data={
#         "prompt": "I cried when my mother-in-law told me to make 100 heads of kimchi outside in the winter.",
#         "output_format": "jpeg",
#     },
# )   

# if response.status_code == 200:
#     with open("./test.jpeg", 'wb') as file:
#         file.write(response.content)
# else:
#     raise Exception(str(response.json()))