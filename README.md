# Meeting Minutes & Action Extractor Skill for Autonomous Agents

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue.svg)](https://modelcontextprotocol.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](requirements.txt)

Transforms conversational meeting transcripts into structured minutes containing clear consensus decisions, assigned task items, and follow-up schedules.

## Capabilities
- **Action Item Parsing**: Automatically identifies responsibilities, owners, and promised timelines.
- **Consensus & Decision Capture**: Segregates agreed architectural and strategic decisions from conversational chatter.
- **Zero Latency**: Instant heuristic extraction using standard library regex patterns.

## MCP Server Integration
```bash
python mcp_server.py
```

### Available MCP Tools
- `extract_meeting_minutes`: Parse meeting transcript into structured decisions and action items.
