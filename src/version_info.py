import os
import sys
import langchain
import openai

print(f"python ver: {sys.version_info}")
print(f"API_KEY:{os.getenv('OPENAI_API_KEY')}")
print(f"langchain ver: {langchain.__version__}")
print(f"openai ver: {openai.__version__}")
