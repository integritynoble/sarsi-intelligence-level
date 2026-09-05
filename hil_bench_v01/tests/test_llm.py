from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

from hilbench import llm


def tool_call(path: str) -> dict:
    return {
        "choices": [
            {
                "message": {
                    "content": "",
                    "tool_calls": [
                        {
                            "id": "call-1",
                            "type": "function",
                            "function": {
                                "name": "read_file",
                                "arguments": json.dumps({"path": path}),
                            },
                        }
                    ],
                }
            }
        ]
    }


def final_response(content: str = '{"answer": 3}') -> dict:
    return {"choices": [{"message": {"content": content}}]}


class LLMExecutorTests(unittest.TestCase):
    def test_parse_accepts_bare_fenced_and_prose_wrapped_objects(self):
        cases = (
            '{"answer": 1}',
            '```json\n{"answer": 1}\n```',
            'Here is the result: {"answer": 1}',
        )
        for text in cases:
            with self.subTest(text=text):
                self.assertEqual(llm._parse(text), ({"answer": 1}, None))
        self.assertEqual(llm._parse("[]"), (None, "invalid_json"))

    def test_run_uses_openai_compatible_arguments_field_for_tool_calls(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            (workspace / "GOAL.md").write_text("visible goal", encoding="utf-8")
            responses = [tool_call("GOAL.md"), final_response()]

            def fake_call(_base, _key, _model, payload, _timeout):
                if len(responses) == 1:
                    self.assertEqual(payload["messages"][-1]["role"], "tool")
                    self.assertEqual(payload["messages"][-1]["content"], "visible goal")
                return responses.pop(0)

            with mock.patch.object(llm, "_call", side_effect=fake_call):
                text = llm.run("http://offline", "key", "model", "prompt", workspace)
            self.assertEqual(text, '{"answer": 3}')

    def test_read_file_tool_cannot_escape_workspace(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            workspace = parent / "workspace"
            workspace.mkdir()
            secret = parent / "private-key.json"
            secret.write_text("PRIVATE SENTINEL", encoding="utf-8")
            responses = [tool_call("../private-key.json"), final_response()]

            def fake_call(_base, _key, _model, payload, _timeout):
                if len(responses) == 1:
                    tool_output = payload["messages"][-1]["content"]
                    self.assertNotIn("PRIVATE SENTINEL", tool_output)
                return responses.pop(0)

            with mock.patch.object(llm, "_call", side_effect=fake_call):
                text = llm.run("http://offline", "key", "model", "prompt", workspace)
            self.assertEqual(text, '{"answer": 3}')


if __name__ == "__main__":
    unittest.main()
