import sys
import json
import re

class MeetingExtractor:
    @staticmethod
    def extract(transcript):
        actions = []
        decisions = []
        for line in transcript.splitlines():
            s = line.strip()
            if not s:
                continue
            if re.search(r"(?i)\b(action|todo|assignee|will deploy|task|responsible)\b", s):
                actions.append(s)
            if re.search(r"(?i)\b(agreed|decided|decision|approved|concluded)\b", s):
                decisions.append(s)

        return {
            "total_action_items": len(actions),
            "action_items": actions,
            "total_decisions": len(decisions),
            "decisions": decisions
        }

def handle_rpc(request):
    method = request.get("method")
    req_id = request.get("id")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "extract_meeting_minutes",
                        "description": "Extract decisions and action items from conversation transcript.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {"transcript": {"type": "string"}},
                            "required": ["transcript"]
                        }
                    }
                ]
            }
        }

    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "extract_meeting_minutes":
            res = MeetingExtractor.extract(args.get("transcript", ""))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res)}]}}

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()
