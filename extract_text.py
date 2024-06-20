import json

def extract_text(data, results=None):
    if results is None:
        results = []

    if isinstance(data, list):
        for item in data:
            extract_text(item, results)
    elif isinstance(data, dict):
        if 'type' in data and 'text' in data:
            results.append({'type': data['type'], 'text': data['text']})
        elif 'type' in data and 'options' in data and 'text' in data['options']:
            results.append({'type': data['type'], 'text': data['options']['text']})
        if 'boxes' in data:
            extract_text(data['boxes'], results)
        if 'options' in data and 'doc' in data['options']:
            doc_content = data['options']['doc']['content']
            for content in doc_content:
                if 'content' in content:
                    for item in content['content']:
                        if 'text' in item:
                            results.append({'type': content['type'], 'text': item['text']})
    return results

if __name__ == "__main__":
    with open('test_updated.json', 'r', encoding='utf8') as file:
        data = json.load(file)

    text_elements = extract_text(data)

    for element in text_elements:
        print(element)
        # print(f"Type: {element['type']}, Text: {element['text']}")
