"""Five deterministic policy/extraction evaluation cases; no API key required."""
from main import _fallback_extract, classify, make_private_summary

COURSES = {
    "CS101": "Programming in Python",
    "MA102": "Engineering Mathematics",
    "PH103": "Engineering Physics",
    "EE104": "Electrical Engineering",
}

TESTS = [
    {
        "id": "T1", "request": "Please give me 2 days for CS101 due to fever.",
        "expected_reason": "medical", "expected_recommendation": "within_policy"
    },
    {
        "id": "T2", "request": "Need 5 days for MA102 because of a family event.",
        "expected_reason": "family", "expected_recommendation": "needs_faculty_review"
    },
    {
        "id": "T3", "request": "The PH103 upload system failed. I need three days.",
        "expected_reason": "technical", "expected_recommendation": "within_policy"
    },
    {
        "id": "T4", "request": "Need an extension for CS101 due to workload.",
        "expected_reason": "workload", "expected_recommendation": "needs_more_info"
    },
    {
        "id": "T5", "request": "Please give me 2 days for MA102 due to workload.",
        "expected_reason": "workload", "expected_recommendation": "needs_faculty_review"
    },
]


def run_evaluation():
    passed = 0
    print("EVALUATION HARNESS (5 test requests)")
    for test in TESTS:
        data = _fallback_extract(test["request"], COURSES)
        actual_recommendation = classify(data)
        reason_ok = data["reason"] == test["expected_reason"]
        recommendation_ok = actual_recommendation == test["expected_recommendation"]
        ok = reason_ok and recommendation_ok
        passed += int(ok)
        print(
            f"{test['id']}: reason={data['reason']} "
            f"({ 'PASS' if reason_ok else 'FAIL' }), "
            f"recommendation={actual_recommendation} "
            f"({ 'PASS' if recommendation_ok else 'FAIL' })"
        )
    print(f"\nScore: {passed}/5 test cases fully correct.")
    return passed


if __name__ == "__main__":
    run_evaluation()
