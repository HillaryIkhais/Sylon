import os
import sys

# Ensure the Cascade directory is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.llm_client import call_llm

print("\n🚀 Starting Sylon Alibaba Cloud Test...")
print("Connecting to endpoint: https://dashscope-intl.aliyuncs.com/compatible-mode/v1")

prompt = "Hello Qwen! Are you actively running on Alibaba Cloud DashScope?"
print(f"\nUser: {prompt}\n")

try:
    response = call_llm(prompt, system_prompt="You are Sylon's AI reasoning engine, running on Alibaba Cloud Qwen-Max.")
    print(f"Sylon Qwen Engine: {response}\n")
    print("✅ Successfully verified Alibaba Cloud API connection!")
except Exception as e:
    print(f"❌ Connection failed. Did you add your DASHSCOPE_API_KEY to the .env file?\nError: {e}")
