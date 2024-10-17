from gradio_client import Client

def generate_prompt(user_input:str):
	prompt = (f"You are a helpful musician assistant that generates lyrics based on the given user mood and prompt. Generate a 1 minute long lyric for {user_input} Be metaphorical and don’t write lyrics that are straightforward.")

	client = Client("huggingface-projects-gemma-2-9b-it")
	result = client.predict(
			message=prompt,
			max_new_tokens=1024,
			temperature=0.6,
			top_p=0.9,
			top_k=50,
			repetition_penalty=1.2,
			api_name="/chat"
			)

	lyric = result
	lyric = lyric.split("\n")

	lyric = [x for x in lyric if len(x.split(" ")) > 3]
	lyric = lyric[:-1]
	return lyric