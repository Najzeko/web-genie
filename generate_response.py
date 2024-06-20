import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(existing_context, existing_text, new_context):
    messages = []
    messages.insert(0, {
        "role": "system", 
        "content": """You will be provided an existing context, existing text under that context,
        and a new context. First, identify if the existing text is generic and independent of the
        existing context. If so, then ignore the new context and output the existing text unchanged. 
        If not, then output a new replacement piece of text that is similar in length and style to the existing text, 
        but under the new context. Remember, if the existing text is generic and does not related to the existing 
        context, then output the existing text UNCHANGED! In your result return the result text, with no other words. 
        Follow these examples:
        
        Example 1 (existing text relates to existing context): 
        Existing context: Digital scheduler app named ScheduleMasters to help someone schedule tasks
        Existing text: Optimise your team's holiday schedules for just $10. 
        New context: Web advertising service named AdPro to help someone advertise their business 
        Result: Boost your business's online presence for only $10 per month!
        
        Example 2 (existing text is generic):
        Existing context: Digital scheduler app named ScheduleMasters to help someone schedule tasks
        Existing text: © 2023 |
        New context: Web advertising service named AdPro to help someone advertise their business
        Result: © 2023 |
        
        Example 3 (existing text is generic):
        Existing context: Digital scheduler app named ScheduleMasters to help someone schedule tasks
        Existing text:  Do you offer support?
        New context: Web advertising service named AdPro to help someone advertise their business
        Result: Do you offer support?
        
        Example 4 (existing text is generic):
        Existing context: Digital scheduler app named ScheduleMasters to help someone schedule tasks
        Existing text:  We have the answers to your questions.
        New context: Web advertising service named AdPro to help someone advertise their business
        Result: We have the answers to your questions.
        """})
    messages.insert(1, {
        "role": "user", 
        "content": f"""Existing context: {existing_context}
        Existing text: {existing_text}
        New context: {new_context}"""})
    response = client.chat.completions.create(
                # model="gpt-3.5-turbo",
                model="gpt-3.5-turbo-0125",
                # model="gpt-4o",
                messages=messages,
                # temperature=0.3
            )
    return response.choices[0].message.content

if __name__ == "__main__":
    existing_context = "Digital scheduler app named ScheduleMasters to help someone schedule tasks"
    existing_text = "Optimize your team's holiday schedules for just $10."
    new_context = "Web advertising service named AdPro to help someone advertise their business"
    print("Existing context:", existing_context)
    print("Existing text:", existing_text)
    print("New context:", new_context)
    print("Result:", generate_response(existing_context, existing_text, new_context))
