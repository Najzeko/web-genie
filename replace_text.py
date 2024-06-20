import json
from generate_response import generate_response

def replace_text(data, existing_context, new_context, index=0):
    if isinstance(data, list):
        for item in data:
            index = replace_text(item, existing_context, new_context, index)
    elif isinstance(data, dict):
        if 'type' in data and 'text' in data:
            original_text = data['text']
            new_text = generate_response(existing_context, original_text, new_context)
            print(f"Original text: {original_text}\nNew text: {new_text}\n")
            data['text'] = new_text
            index += 1
        elif 'type' in data and 'options' in data and 'text' in data['options']:
            original_text = data['options']['text']
            new_text = generate_response(existing_context, original_text, new_context)
            print(f"Original text: {original_text}\nNew text: {new_text}\n")
            data['options']['text'] = new_text
            index += 1
        if 'boxes' in data:
            index = replace_text(data['boxes'], existing_context, new_context, index)
        if 'options' in data and 'doc' in data['options']:
            doc_content = data['options']['doc']['content']
            for content in doc_content:
                if 'content' in content:
                    for item in content['content']:
                        if 'text' in item:
                            original_text = item['text']
                            new_text = generate_response(existing_context, original_text, new_context)
                            print(f"Original text: {original_text}\nNew text: {new_text}\n")
                            item['text'] = new_text
                            index += 1
    return index

if __name__ == "__main__":
    with open('test.json', 'r', encoding='utf8') as file:
        data = json.load(file)

    existing_context = "Digital scheduler app named ScheduleMasters to help someone schedule tasks"
    new_context = "Web advertising service named AdPro to help someone advertise their business"

    replace_text(data, existing_context, new_context)

    with open('test_replaced.json', 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
