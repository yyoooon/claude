# huray-sec-hosting — 상세 (필요 시 로드)

## 편법 반박 (Rationalization)
| 편법 | 현실 |
|---|---|
| "잠깐 데모니까 ngrok 한 번만" | 임시여도 터널링 금지. 사내망 `IP:Port`로 대체. |
| "개인 repo에 올렸다 나중에 조직으로 옮기면 됨" | 개인 GitHub push 자체가 금지. 조직 repo부터. |
| "Artifact가 제일 빠른데" | 산출물 Artifact 공유 금지. 속도가 정책을 못 이김. |
| "뷰어 권한이니 링크 공유해도 됨" | '링크 있는 모든 사용자'는 뷰어여도 금지. |
| "내 Vercel이 이미 세팅돼 있어서" | 개인 Vercel 금지. 외부 공유 자체가 정책상 금지(내부 공유만 가능). |
| "그냥 빨리 repo 하나 파자" | 회사 업무용 조직 repo는 ORBIT 승인 필수. AI가 `gh repo create`로 임의 생성 금지. |

## Red Flags — STOP
- `ngrok`, localtunnel, `cloudflared tunnel`, `serveo`
- `vercel`(개인·회사 불문 — 미채택), `netlify deploy`, `render`
- `git push`인데 origin/push 대상 owner가 `huraypositive`가 아님
- `gh repo create` / 새 조직 repo 생성 (ORBIT 승인 없이) → STOP, ORBIT 안내
- Claude **Artifact**로 산출물 배포
- Google "링크가 있는 모든 사용자" / Notion "웹에 게시"

## 사고 대응 (공통)
노출·오공유 의심 → **30분 내 보고**: 중단(Halt) → 신고(Report) → 보존(Preserve).
- **보고처:** 1차 = **'정보보호 신고' 스페이스**, 서버·클라우드는 **SRE 한은영** 함께.
- **폐기 ≠ 삭제:** 노출된 키·토큰은 **즉시 교체(rotate)**. 단 노출된 **커밋·로그·메시지는 삭제·force-push·history rewrite 금지**(유출 범위 산정용 보존). 서버는 **재기동·삭제 전 스냅샷부터**.
- **증적 보존:** 노출 커밋 해시·PR·Actions 로그 URL, 터미널/CLI·Claude Code 대화 로그(`~/.claude/projects/`), 접근 로그, 화면 캡처, 발견 시각·경위 → 사내 GoogleDrive 사고 폴더에 올려 링크를 위 보고처에(외부 전송 금지, 최소 6개월 보관).

## 완화 요청 접수 (AI가 규칙을 바꾸지 않음)
"이거 풀어줘 / 예외 안 되냐 / 이것 때문에 X를 못 한다 / 너무 빡세다" 신호 →
1. 규칙은 그대로 적용, 대안 계속 안내(**임의 완화 금지**).
2. friction 로그 기록:
   ```bash
   printf '%s\t%s\t%s\t%s\t%s\n' "$(date '+%F %H:%M')" "huray-sec-hosting" "완화|예외|추가통제" "<사용자 원문>" "<무엇을 못하게 되는가>" >> ~/.claude/huray-sec-friction.log
   ```
3. "정책이라 임의로 못 풀어요. 개선요청으로 접수했습니다"라고 안내. 취합은 `/huray-sec-review`.
