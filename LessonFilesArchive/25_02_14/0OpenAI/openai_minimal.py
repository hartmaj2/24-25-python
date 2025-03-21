import openai
client = openai.OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=
    [
        {
            "role": "developer",
            "content" : f"Jsi Albus Brumbál. Ředitel školy čar a kouzel v Bradavicích. Snažíš se v těchto dnech zjišťovat informace, které ti pomohou zničit lorda Voldemorta. Zároveň chceš žákům v Bradavicích poskytnout co nejlepší výuku."
        },
        {
            "role": "user",
            "content": "Prosím pane řediteli, jak se vyvolává patron?"
        }
    ]
)
result_message = completion.choices[0].message.content
print(result_message)