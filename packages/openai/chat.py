from openai import OpenAI

ROLE = """
When requested to show chess position, always use the FEN notation, 
and show the FEN position in a code block startin with ```fen and ending with ```.
When requested to write code, pick Python.
"""

MODEL = "gpt-3.5-turbo"
AI = None

def req(msg):
    return [{"role": "system", "content": ROLE}, 
            {"role": "user", "content": msg}]

def ask(input):
    comp = AI.chat.completions.create(model=MODEL, messages=req(input))
    if len(comp.choices) > 0:
        return comp.choices[0].message.content
    return "ERROR"


"""
%cd packages/sample
import hello_openai as h
args['input']="write a function returning the sum of the numbers up to a provided number"
r = h.main(args)
"""
def main(args):
    global AI
    AI = OpenAI(api_key=args.get("OPENAI_API_KEY"))

    input = args.get("input", "")
    output = ask(input)

    return {"body": {"output": output}}
