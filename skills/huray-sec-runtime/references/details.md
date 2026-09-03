# huray-sec-runtime — 상세 (필요 시 로드)

## 편법 반박 (Rationalization)
| 편법 | 현실 |
|---|---|
| "다운로드 폴더가 편한데 잠깐이면 괜찮아" | 잠깐이어도 고객 데이터 유입 위험. 전용 폴더로. |
| "매번 승인 누르기 귀찮으니 skip 켜자" | skip-permissions 금지. 삭제·push·결제는 직접 승인. |
| "그 키 아마 안 샜을 거야" | 노출 가능성 있으면 교체가 기본. 추정으로 넘기지 않음. |
| "테스트 데이터에 실데이터 조금 섞여도 됨" | Git 히스토리 영구 잔존. 실데이터 제외. |

## Red Flags — STOP
- `pwd`가 `~`, `~/Downloads`, `~/Desktop`, 홈 직속
- 폴더에 `.env` / `*.pem` / `credentials*.json` / `.aws/`
- `--dangerously-skip-permissions` / `auto-accept` / skip 요청
- 삭제·`git push`·외부 API·DB 쓰기·결제를 승인 없이 자동 실행

## 사고 대응 (공통)
자격증명·고객 데이터 노출 의심 → **30분 내 보고**: 중단 → 신고 → 보존.
- **보고처:** 1차 = **'정보보호 신고' 스페이스**, 서버·클라우드는 **SRE 한은영** 함께.
- **폐기 ≠ 삭제:** 노출 키·토큰은 **즉시 교체(rotate)**. 노출 **커밋·로그·메시지는 삭제·force-push·history rewrite 금지**(보존). 서버는 **재기동·삭제 전 스냅샷부터**.
- **증적 보존:** 노출 커밋 해시·PR·Actions 로그 URL, 터미널/CLI·Claude Code 대화 로그(`~/.claude/projects/`), 접근 로그, 화면 캡처, 발견 시각·경위 → 사내 GoogleDrive 사고 폴더에 올려 링크를 위 보고처에(외부 전송 금지, 최소 6개월 보관).

## 완화 요청 접수 (AI가 규칙을 바꾸지 않음)
완화·불편 신호 →
1. 규칙 그대로 적용, 대안 안내(**임의 완화 금지**).
2. friction 로그 기록:
   ```bash
   printf '%s\t%s\t%s\t%s\t%s\n' "$(date '+%F %H:%M')" "huray-sec-runtime" "완화|예외|추가통제" "<사용자 원문>" "<무엇을 못하게 되는가>" >> ~/.claude/huray-sec-friction.log
   ```
3. "개선요청으로 접수했습니다" 안내. 취합은 `/huray-sec-review`.
