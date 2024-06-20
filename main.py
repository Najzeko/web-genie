import json
from extract_text import extract_text
from replace_text import replace_text

if __name__ == "__main__":
    with open('test.json', 'r', encoding='utf8') as file:
        data = json.load(file)

    text_elements = extract_text(data)
    print("EXTRACTED TEXT ELEMENTS:")
    for element in text_elements:
        print(element)

    existing_context = "Digital scheduler app named ScheduleMasters to help someone schedule tasks"
    new_context = "Web advertising service named AdPro to help someone advertise their business"

    replace_text(data, existing_context, new_context)

    # Save the modified JSON data
    with open('test_replaced.json', 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Text replacement completed and saved to test_replaced.json")
