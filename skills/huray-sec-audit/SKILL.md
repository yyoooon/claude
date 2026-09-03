---
name: huray-sec-audit
description: Use to scan existing/past work for Huray security violations — 보안 점검·기존 위반 스캔·시크릿 노출 확인·개인 repo·다운로드 고객데이터·/huray-sec-audit. severity별 리메디에이션 체크리스트를 만든다.
---

# 휴레이 보안: 기존 위반 스캔 (소급)
> 🔖 버전 **v1.1** · 최종수정 **2026-08-18** · 출처 `보안가이드_v1.0.0.pdf(최종)`

## 핵심 원칙
과거 위반은 **조용히 지우지 않는다.** 발견 → severity 분류 → 체크리스트로 **사람이 결정**. AI는 안전한 기계적 준비까지만; **자격증명 교체·계정/공유 설정 변경·영구 삭제·휴지통 비우기는 사람**이 한다(안전규칙). **예외: 커밋/공유된 시크릿의 키 교체는 지체 없이 = 사고 처리.**

## 스캔 (현재 프로젝트 = cwd 기준, 공통 위치 포함)

```bash
# 1) git remote가 개인 repo인지
git remote -v 2>/dev/null

# 2) 현재 파일의 하드코딩 시크릿 흔적
grep -rInE '(sk-[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[baprs]-|ghp_[A-Za-z0-9]{20,}|(api[_-]?key|secret|password|token)["'"'"' ]*[:=][ "'"'"']*[A-Za-z0-9/_\-]{12,})' \
  --exclude-dir={node_modules,.git,dist,build,.next} . 2>/dev/null | head -50

# 3) 자격증명 파일이 있고 gitignore 안 됐는지
find . -maxdepth 3 \( -name '.env*' -o -name '*.pem' -o -name 'credentials*.json' -o -name '*.key' -o -name '.aws' \) \
  -not -path '*/node_modules/*' 2>/dev/null
git ls-files 2>/dev/null | grep -iE '\.env|\.pem$|credentials.*\.json|\.key$'   # 실제 추적(커밋)되는 시크릿 = 사고

# 4) git 히스토리에 시크릿이 커밋된 적 있는지
git log --all --oneline -- '*.env' '*.pem' 'credentials*.json' '*.key' 2>/dev/null | head

# 5) 로컬 고객데이터(다운로드·바탕화면·홈)
find ~/Downloads ~/Desktop -maxdepth 2 -type f \( -iname '*.csv' -o -iname '*고객*' -o -iname '*계약*' -o -iname '*환자*' -o -iname '*개인정보*' \) 2>/dev/null | head -30

# 6) 개인 배포/호스팅 흔적
find . -maxdepth 3 \( -name 'vercel.json' -o -name '.vercel' -o -name 'netlify.toml' -o -name 'render.yaml' \) 2>/dev/null
```

- git remote owner가 `huraypositive`가 아니면 개인 repo(🟠).
- 추적(커밋)되는 `.env/*.pem/*.key`나 히스토리 커밋 흔적, grep 시크릿 매치 → 노출 = 🔴 사고.

## severity 분류 → 처리

| severity | 발견 | 처리 | 주체 |
|---|---|---|---|
| 🔴 **사고** | 시크릿이 커밋·추적·히스토리·공유됨 | ① **키 즉시 교체(rotate)** ② **30분 내 보고** → **'정보보호 신고' 스페이스**·SRE(**한은영**) ③ **노출 커밋·로그 보존**(force-push·history rewrite·로그삭제 **금지** — 유출 범위 산정용) ④ `.gitignore` 등록 | ①②=**사람**(자격증명), ④=AI. 히스토리 정리는 SRE와 범위 산정 후 별도 |
| 🟠 **높음** | 개인 GitHub repo / 개인 Vercel·Netlify·Render 운영 | 조직 repo로 이전. **외부 호스팅은 승인 경로 없음(회사 Vercel 미채택) → 내리고 담당자(신민철) 문의** | 이전 준비(`remote set-url` 등)=AI, 계정/삭제=사람 |
| 🟡 **중** | `~/Downloads`·바탕화면 고객데이터, Google/Notion 과다공유, gitignore 안 된 자격증명 파일(미커밋) | 전용 폴더로 이동/파기, 공유설정 변경, ignore 등록 | 이동·ignore 준비=AI, **삭제·휴지통 비우기·공유설정 변경=사람** |

## 산출물
`../보안점검_YYMMDD.md`에 저장:
- severity별 발견 목록(파일/remote/위치)
- 각 항목: 처리 방법 + **[AI가 할 것] / [사람이 할 것]** 구분 + 체크박스
- 🔴이 있으면 최상단에 "즉시: 키 교체 + 30분 보고" 경고

## 하지 말 것
- 발견한 파일을 **임의 삭제·휴지통 비우기** → 금지(사람 결정, CLAUDE.md #6).
- 노출된 **키를 AI가 직접 교체 시도**(콘솔 로그인·자격증명) → 금지. 사람에게 넘긴다.
- 사고 시 **커밋/로그 삭제·force-push·history rewrite** → 금지(**보존 우선**). 히스토리 정리는 SRE(한은영)와 범위 산정 후.
- 스캔 결과(경로·시크릿 값)를 **외부로 전송** → 금지. 값은 마스킹해 보고.

원문: `보안가이드_v1.0.0.pdf(최종)`. 관련: `/huray-sec-review`(개선 루프).
