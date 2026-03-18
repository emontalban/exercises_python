def remove_first_and_last(list_to_clean):
    languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Swift", "Go", "Rust"]
    list_clean = languages[1:-1]
    print(list_clean)

remove_first_and_last(["Python", "Java", "C++", "JavaScript", "Ruby", "Swift", "Go", "Rust"])
# otra opcion es usar el operador *

def remove_first_and_last_II(list_to_clean):
    _, *content, _ = list_to_clean
    print(list_to_clean)
    return content
html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last_II(html))

