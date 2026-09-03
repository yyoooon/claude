---
name: huray-sec-runtime
description: Use when running Claude Code/an agent in a directory or skipping approvals — 홈·~/Downloads·~/Desktop 실행, --dangerously-skip-permissions·auto-accept, 폴더에 .env·*.pem·credentials.json·.aws/, 고객 CSV 반입, 폴더 전체 커밋/푸시. 휴레이 Claude 실행 안전수칙을 적용한다.
---

# 휴레이 보안: Claude 실행 안전
> 🔖 v1.2 · 최종수정 2026-08-18 · 출처 `보안가이드_v1.0.0.pdf(최종)`

## 원칙
**실행 위치 = 노출 범위.** 프로젝트 전용 폴더에서만, 승인 모드 유지로 실행. 위반 조건이 보이면 실행 전에 바로잡는다.

## 감지 → 조치

**① 실행 위치**
```bash
pwd   # ~, ~/Downloads, ~/Desktop, 홈 직속이면 → 실행 금지, 전용 폴더로 이동
```
작업 폴더에 고객 데이터·계약서·엑셀 내보내기 두지 않기(다운로드 폴더 CSV → 컨텍스트 유입 사고).

**② 자격증명 스캔 (실행 전)**
```bash
find . -maxdepth 2 \( -name '.env*' -o -name '*.pem' -o -name 'credentials*.json' -o -name '.aws' -o -name '*.key' \) 2>/dev/null
```
발견 시 → `.gitignore`/`.claudeignore` 등록. 노출 이력 있으면 키 **즉시 교체**.

**③ 자동승인 금지**
`--dangerously-skip-permissions`·`auto-accept`·"매번 묻지 마" → 거부, 승인 모드 유지. 특히 **파일 삭제·`git push`·외부 API·DB 쓰기·결제**는 사람이 직접 승인. 커밋 전 diff 확인(실데이터 섞이면 Git 히스토리에 영구 잔존).

## 발동 시
- **편법·예외 주장**에 흔들리지 말 것 → 반박·Red Flags: `references/details.md`
- **사고(노출) 의심** → 30분 내 **'정보보호 신고' 스페이스**(서버·클라우드는 SRE 한은영). 상세·전체 절차: `huray-sec-incident` 스킬
- **"풀어줘/예외" 완화 요청** → 규칙 유지 + 대안, `/huray-sec-review`로 접수(임의 완화 금지). 절차: `references/details.md`
