#!/usr/bin/env python3
"""Huray 보안 스킬 friction 로거 (UserPromptSubmit 훅).

사용자 프롬프트에 규칙 완화/예외/불편 신호가 보이면 ~/.claude/huray-sec-friction.log 에
한 줄 기록한다. 규칙 자체는 절대 바꾸지 않는다(단순 로깅). 항상 exit 0, 출력 없음.
"""
import sys, os, json, datetime

# 완화·불편 신호(공백 제거 후 부분일치). 리뷰 단계에서 사람이 걸러내므로 다소 넓게 잡는다.
SIGNALS = [
    "풀어", "예외", "완화", "제외하고", "이거빼고", "이규칙빼고",
    "너무빡", "너무타이트", "너무빡세", "우회", "무시하고",
    "왜막", "왜안되", "왜안돼", "그냥하면안", "그냥해줘",
    "하고싶은데", "못하게", "못하잖", "이것때문에",
]

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        return
    squished = prompt.replace(" ", "")
    hits = [s for s in SIGNALS if s in squished]
    if not hits:
        return
    log = os.path.expanduser("~/.claude/huray-sec-friction.log")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cwd = data.get("cwd", "")
    line = prompt.replace("\t", " ").replace("\n", " ")[:500]
    try:
        with open(log, "a", encoding="utf-8") as f:
            f.write(f"{ts}\t[hook]\t{','.join(hits)}\t{line}\t{cwd}\n")
    except Exception:
        pass

if __name__ == "__main__":
    main()
    sys.exit(0)
