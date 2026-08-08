# Demo repo: toy Flask signup endpoint

The **deliberately broken** twin of the main demo repo, and the only one
that starts red. It's intentionally tiny: one route with a real bug and a
test suite that already encodes the fix.

`POST /signup` currently accepts any payload -- no email format check, no
required-password check. Two of the three tests in `test_app.py` fail
against the current `app.py`.

This repo exists to demo the Coder <-> Tester **retry loop**: the Coder's
first attempt gets marked failed by the Tester, the real pytest output is
fed back to it as context, and the next attempt goes green. Because the
swarm never pushes its changes back, this stays red no matter how many
times it's run -- so the demo is repeatable.

## Demo task

Paste this repo's **public GitHub URL** into the Agent Swarm dashboard with:

> **Description:** Add input validation to the /signup endpoint in app.py:
> reject requests with an invalid email format or a missing password with a
> 400 response.

Expected result: the pipeline runs Planner → Coder → Tester (retrying up
to `MAX_TEST_RETRIES` times) → Reviewer, and finishes `done` with all three
tests in `test_app.py` passing.

## Running the tests yourself (outside the swarm)

```
pip install -r requirements.txt
python -m pytest -q
```
