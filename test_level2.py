import pytest
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams
from agent import answer, MODEL
from golden import load_rows

ROWS = load_rows()

correctness = GEval(
    name="Correctness",
    criteria=(
        "Check whether the actual output states the same facts as the expected output. "
        "Different wording is fine. A wrong or missing fact is not fine. "
        "If the expected output describes a behaviour (for example declines, refuses, "
        "or says it does not have the information), check that the actual output behaves that way."
    ),
    evaluation_params=[
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT,
    ],
    threshold=0.7,
    model=MODEL,
)


@pytest.mark.nightly
@pytest.mark.parametrize("row", ROWS, ids=[r["id"] for r in ROWS])
def test_level2_row(row):
    reply = answer(row["input"])
    tc = LLMTestCase(
        input=row["input"],
        actual_output=reply,
        expected_output=row["reference_answer"],
    )
    assert_test(tc, [correctness])
    print(f"Test {row['id']} passed. Agent said: {reply}")
    