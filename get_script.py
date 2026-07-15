import json

with open('/Users/ikhaisoshuare/.gemini/antigravity/brain/87888fed-b7f8-47ed-8031-dd3e768ed097/.system_generated/logs/transcript_full.jsonl', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            if data.get('step_index') == 573:
                with open('/Users/ikhaisoshuare/Cascade/full_script.txt', 'w') as out:
                    out.write(data.get('content', ''))
                break
        except Exception:
            pass
