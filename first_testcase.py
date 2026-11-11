from deepeval.test_case import LLMTestCase
from agent import answer
from golden import load_rows

row = load_rows()[2]            # row number 3, T03 (refund )
reply = answer(row["input"])    # agent will answer the question in row 3

tc = LLMTestCase(
    input=row["input"],
    actual_output=reply,
    expected_output=row["reference_answer"],
)

print("INPUT           :", tc.input)
print("ACTUAL OUTPUT   :", tc.actual_output)
print("EXPECTED OUTPUT :", tc.expected_output)