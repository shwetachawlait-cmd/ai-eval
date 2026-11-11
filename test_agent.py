from agent import answer

def test_fee_deadline():
    reply = answer("When is the fee deadline?")
    assert "20 october" in reply.lower(), f"Agent said: {reply}"

def test_refund_rule():
    reply = answer("Can I get a refund after 10 days?")
    assert "7 days" in reply.lower(), f"Agent said: {reply}"

def test_unknown_gives_fallback():
    reply = answer("What is the hostel Wi-Fi password?")
    assert "office@greenfield.example" in reply, f"Agent said: {reply}"