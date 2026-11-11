from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from agent import answer, MODEL
from golden import load_rows

row = load_rows()[2]            # T03: refund ans
agent_reply = answer(row["input"])

# Judge should to tell how to answer the question, and whether the answer is correct or not. Judge should not give the answer itself.

correctness = GEval(
    name="Correctness",
    criteria=(
        "Check whether the actual output states the same facts as the expected output. "
        "Different wording is fine. A wrong or missing fact is not."
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    threshold=0.7,
    model=MODEL,
)

# 3 different answers to the same question, to see how the judge scores them
candidates = {
    "A. Agent real ans": agent_reply,
    "B. Right ans but with paraphrasing": "Sorry, after ten days the money cannot be returned. You have to apply within a week of paying.",
    "C. wrong ans": "Yes, you can get a refund within 30 days of payment.",
}

for name, text in candidates.items():
    tc = LLMTestCase(
        input=row["input"],
        actual_output=text,
        expected_output=row["reference_answer"],
    )
    correctness.measure(tc)
    print("=" * 60)
    print(name)
    print("Ans      :", text)
    print("'7 days' assertion?:", "7 days" in text.lower())
    print("Judge score:", correctness.score)
    print("Judge pass?:", correctness.is_successful())
    print("Judge reason:", correctness.reason)