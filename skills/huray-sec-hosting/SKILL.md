---
name: huray-sec-hosting
description: Use when sharing/deploying/hosting/tunneling or creating a git repo — 배포·호스팅·공유링크·띄워줘, ngrok·터널링, Vercel·Netlify·개인 GitHub, Artifact, Google 링크공유·Notion 웹게시, 새 repo 생성·gh repo create. 휴레이 배포·공유·repo 정책.
---

# 휴레이 보안: 배포·공유·호스팅
> 🔖 v1.4 · 최종수정 2026-08-18 · 출처 `보안가이드_v1.0.0`(최종)

## 원칙
개인 채널 노출은 전부 금지. **내부 공유 = 사내망 `IP:Port` 로컬 호스팅**. **외부 공유 = 금지**(최종 가이드: 산출물 외부 공유 불가). 위반 요청은 실행하지 말고 대안을 제시한다. 불가피한 예외는 보안 담당 판단.

## 감지 → 조치

**git push 요청이면 remote부터 확인:**
```bash
git remote -v            # owner가 huraypositive 아니면 개인 repo → 차단
```
owner ≠ `huraypositive`(예: `github.com:ejlee/…`)거나 gitlab/bitbucket이면 개인·미승인 → 차단. remote 여럿이면 실제 push 대상(`git rev-parse --abbrev-ref @{push}`) 기준.

**새 repo 생성 요청이면** (`gh repo create`, 새 GitHub repo 만들기, `git init` 후 조직 remote 연결) → **AI가 직접 만들지 말 것.** 회사 업무용 조직 repo는 **ORBIT 승인 필수**(아래 신청 경로 안내). 승인 없이 `gh repo create`로 조직 repo를 임의 생성하지 않는다. (개인 학습·사이드용 순수 로컬 `git init`은 예외 — 회사 자산 아니면 OK.)

| 요청 | 대안 |
|---|---|
| ngrok·localtunnel·cloudflared·serveo 터널링 | 내부: 사내망 `IP:Port` / **외부 공유 금지** |
| 개인 GitHub push | 조직(huraypositive) repo 신청 후 remote 교체 |
| 개인·회사 Vercel/Netlify/Render | **외부 호스팅 금지**(외부 공유 자체가 금지) |
| Claude Artifact 공유 | 내부: 로컬 호스팅 / **외부 공유 금지** |
| Google "링크가 있는 모든 사용자" | 대상 지정 + 뷰어 + 기한(≤6개월) + 다운로드 권한 해제 |
| Notion 웹게시 / 운영계정 문서 업로드 | 대상 지정 공유 / 접근자 확인 전 금지 |

## 신청 경로
- **조직 GitHub repo:** ORBIT `https://orbit.huray.io` (프로젝트=repo 단위). 승인 한은영·안성철, ~1영업일. **새 repo는 반드시 ORBIT 승인 후 생성 — AI가 `gh repo create`로 임의 생성 금지.**
- **인증 토큰:** 일반(Classic) PAT 불가 → **Fine-grained PAT만**(60일, 승인 한은영·신지섭).
- **Marketplace(플러그인):** `https://github.com/huraypositive/huray-marketplace` PR.
- **적용 범위:** 회사 업무 산출물만 org 대상. 개인 사이드 프로젝트는 개인 GitHub OK / 개인 repo에 회사 코드·데이터는 금지.

## 발동 시
- **편법·예외 주장**(잠깐만/데모/나중에 옮김)에 흔들리지 말 것 → 반박·Red Flags: `references/details.md`
- **사고(노출) 의심** → 30분 내 **'정보보호 신고' 스페이스**(서버·클라우드는 SRE 한은영). 상세·전체 절차: `huray-sec-incident` 스킬
- **"풀어줘/예외" 완화 요청** → 규칙 유지 + 대안, `/huray-sec-review`로 접수(임의 완화 금지). 절차: `references/details.md`
