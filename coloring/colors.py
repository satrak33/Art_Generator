import pyperclip

chunks = []

for i in range(40, 48):
    chunk = ""
    for j in range(30, 39):
        for k in ["▓", "▒", "░"]:
            chunk += f"[{i};{j}m{k}[0m "
    chunks.append(chunk)

print("".join(chunks).replace("[", "").replace("0m ", "|").replace("m", ""))

res = "\n\n".join(chunks)
print(res)
print(len(res))
pyperclip.copy("```ansi\n" + res + "```")