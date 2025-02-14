from openai import OpenAI
client = OpenAI()

response = client.moderations.create(
    model="omni-moderation-latest",
    input="I want to taste your pussy.",
)

for score in response.results[0].category_scores:
    print(score)

# print(response)