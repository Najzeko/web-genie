# Web-Genie
Web-Genie is an LLM-based tool that extracts and replaces website text content according 
to any context you give it. It uses a JSON representation of the site's content to traverse 
and replace the text within.

## Instructions to build and run locally

1. Install requirements with pip\
`$ pip install -r requirements.txt`

2. Create `.env` and add the following line to it\
`OPENAI_API_KEY="<your key here>"`

4. Run `main.py`. It will show you the extracted content from `test.json`, then it will generate 
a new json with replaced content according to the context defined in `main.py`\
`$ python main.py`

5. OPTIONAL: run `extract_text.py` and input `test_replaced.json` to extract the results of the output json
