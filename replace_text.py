import json

def replace_text(data, new_texts, index=0):
    new_texts_len = len(new_texts)

    if isinstance(data, list):
        for item in data:
            index = replace_text(item, new_texts, index)
    elif isinstance(data, dict):
        if 'type' in data and 'text' in data:
            data['text'] = new_texts[index % new_texts_len]['text']
            index += 1
        elif 'type' in data and 'options' in data and 'text' in data['options']:
            data['options']['text'] = new_texts[index % new_texts_len]['text']
            index += 1
        if 'boxes' in data:
            index = replace_text(data['boxes'], new_texts, index)
        if 'options' in data and 'doc' in data['options']:
            doc_content = data['options']['doc']['content']
            for content in doc_content:
                if 'content' in content:
                    for item in content['content']:
                        if 'text' in item:
                            item['text'] = new_texts[index % new_texts_len]['text']
                            index += 1
    return index

if __name__ == "__main__":
    with open('test.json', 'r', encoding='utf8') as file:
        data = json.load(file)

    # Example new texts to replace the old ones
    new_texts = [
        {'type': 'headline', 'text': 'New Headline'},
        {'type': 'paragraph', 'text': 'New paragraph text.'},
        {'type': 'LpButtonReact', 'text': 'Click Here'}
    ]

    replace_text(data, new_texts)

    with open('test_updated.json', 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
