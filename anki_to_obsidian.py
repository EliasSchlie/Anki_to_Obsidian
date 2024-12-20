def main():
    file_path = '/Users/eliasschlie/Documents/GitHub/Anki_to_Obsidian/exported_notes/biology_notes.txt'

    with open(file_path, 'r') as file:
        content = file.read()

    notes = content.split("\n")
    notes = notes[216:]

    i = 0
    for note in notes:
        name, defi = note.rstrip().split("\t\t")
        defi = defi[0].upper() + defi[1:]
        name = name[0].upper() + name[1:]
        ali = None
        if name[-1] == ")":
            name, ali = name.split(" (")
            ali = ali[:-1]
        elif name.__contains__("/"):
            name, ali = name.split("/")
            name = name.strip()
            ali = ali[:-1]
        i += 1
        create_note(name, defi, ali, i)


def create_note(name, defi, ali, i):
    ali = f"\naliases:\n  - {ali}" if ali else ""
    if len(name.split()) > 3: 
        decision = input(f"\n\n{i} Name: {name}\n Content {defi} \nis longer than 3 words. Do you want to continue? (y/n) ")
        if decision == "n":
            return
    content = word_template(name, defi, ali)
    
    # Create and write to a .md file
    with open(f"/Users/eliasschlie/Documents/GitHub/SecondBrainSynk/Anki to Obsidian/{name}.md", "w") as file:
        file.write(content)
    print(f"{i} {name}.md")

def word_template(name, defi, ali):
    return f"""---
Type:
  - "[[Word]]"
  - "[[Anki to Obsidian]]"{ali}
---
# {name}
= {defi} [[+k Biological Psychology - Dr. Paula Mommersteeg#^anki|(S.6)]]

---
# Sources:
1. <% tp.file.cursor(10) %>
5. 
6. [[+k Biological Psychology - Dr. Paula Mommersteeg#^anki]]
# Relevant:
"""


main()