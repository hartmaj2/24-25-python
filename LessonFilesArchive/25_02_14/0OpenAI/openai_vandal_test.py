import openai
client = openai.OpenAI()

num_of_files = 5
for i in range(num_of_files):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=
        [
            {
                "role": "developer",
                "content" : f"Jsi profesionální vandalizátor počítačů. Rád píšeš výhružné ale vtipné, krátké a výstižné hlášky o tom, že počítač tvé oběti byl zvandalizován. Zvandlalizování počítače proběhlo vytvořením mnoha nežádoucích textových souborů, které se uživateli objeví na ploše. Celkem uživatel obdrží {num_of_files} nevyžádaných souborů. Tento vzkaz napiš pro soubor číslo {i+1}"
            },
            {
                "role": "user",
                "content": "Napiš krátký vzkaz, který následně pošlu do textového souboru zvandalizovaného počítače:"
            }
        ]
    )
    result_message = completion.choices[0].message.content
    output_file = open(f"/Users/janhartman/Desktop/vandal{i+1}.txt","w")
    output_file.write(result_message)
    output_file.close()