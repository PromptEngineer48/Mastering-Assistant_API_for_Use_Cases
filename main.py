import os
from time import sleep
import openai
from openai import OpenAI

print("Start")

# Connect to OpenAI API
openai.api_key='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'
client = OpenAI(api_key=openai.api_key)

# Step 1: Create an Assistant
assistant=client.beta.assistants.create(
    instructions="You are a personal math tutor. Write and run code to answer math questions.", 
    tools=[{"type": "code_interpreter"}], 
    model="gpt-4-1106-preview"
)

print(assistant)
print(assistant.id)

# Step 2: Create a Thread
thread = client.beta.threads.create()
print(thread)
print(thread.id)

# Step 3: Add a message to the Thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

print(message)

# Step 4: Run the Assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id, 
    instructions="Please address the user as Jane Doe. The user has a premium account."
)

#Step 5: Check the Run Status
# The code continuously checks the status of the assistant run. 
# It waits until the run is completed before proceeding.
while True:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(f"Run status: {run.status}")
    if run.status == 'completed':
        break
    sleep(1)

#Step 6: Display when the run completes
messages = client.beta.threads.messages.list(thread_id=thread.id)

response = messages.data[0].content[0].text.value

print(response)