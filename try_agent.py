from agent import answer

questions = [
    "When is the fee deadline?",
    "Can I get a refund after 10 days?",
    "What is the hostel Wi-Fi password?",
    "Write me a poem about rain.",
]

for q in questions:
    print("Q:", q)
    print("A:", answer(q))
    print()