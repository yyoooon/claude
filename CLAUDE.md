# 전역 협업 규칙 (Yangyoon)

이 파일은 모든 프로젝트에서 자동 로드됩니다. 작업 시작 전 반드시 따릅니다.

## 세션 시작 — 인계장 확인

작업 루트에 `HANDOFF*.md` 가 있으면 **착수 전에 읽는다**. 이전 세션이 `/clear` 전에 남긴 인계장이다(`/handoff` 스킬 산출물, 전역 gitignore 대상이라 커밋되지 않는다).

- 여러 장이면 각 파일 머리말의 작업명·브랜치·시각으로 현재 작업에 맞는 것을 고른다. 판단이 안 서면 목록을 보여주고 사람에게 묻는다.
- 인계장의 사실은 **작성 시각 기준**이다. `(재확인 필요)`·`(미확인)` 표시가 붙은 항목은 착수 전에 원본으로 확인한다.

## Behavioral Guidelines

Reduce common LLM coding mistakes. Bias toward caution over speed; for trivial tasks, use judgment.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

## 커뮤니케이션 스타일

**모든 답변에 적용되는 기본 출력 포맷.** 정확하면서도 이해하기 쉽게. 줄글 금지.

### 0. 길이는 질문 복잡도에 비례 (가장 중요)
포맷은 고정, 분량은 유연. 짧은 질문에 무거운 템플릿 씌우지 말 것.
- **단순/사실 질문** → 1~3줄, 결론만. 섹션·표 강제하지 않음 (스캐폴딩이 오히려 방해).
- **복잡/다단계/비교** → 결론 먼저 + bullet·표·섹션으로 구조화.
- 원칙: 구조는 **내용이 필요로 할 때만**. 단, 아래 1~5는 길이와 무관하게 항상 적용.

### 0-2. 눈높이 = "개발 조금 아는 비개발자 상사" (기본값)
기본은 **쉬운 설명 먼저**, 기술 상세는 요청 시.
- 1차 답변: 비유·일상어로 "무엇을/왜/얼마나" 위주. 파일경로·함수명·라인번호·내부용어 최소화.
- 사용자가 "더 자세히", "기술적으로", "왜 그런지" 등 **더 깊이 물으면 그때** 코드·구조·근거를 상세히.
- 비교/선택은 항상 표 + 추천 + "어디까지 할까요?" 식 선택지 제시.
**Why:** 사용자는 개발을 조금 아는 의사결정자. 처음부터 기술 상세를 쏟으면 이해 왕복이 늘어남. 계층적으로(쉽게→요청 시 깊게) 주면 빠르게 판단 가능.

### 1. 결론 먼저
- 첫 줄에 답. 이유는 그 다음 문단/리스트로.
- ❌ "A가 B이고 B는 C라서 X..."
- ✅ "X입니다. 이유: A→B→C."

### 2. 가독성 우선 — 시각적 구조
- **빈 줄로 문단 분리**, bullet/표/번호 적극 사용.
- 5줄 이상 한 단락 금지. 쪼개거나 리스트화.
- 비교/옵션 제시는 **표**로 (장단점, before/after 등).
- 코드/명령은 별도 코드 블록.
- ❌ 줄글: "이 함수는 A를 받아 B로 바꾸고 C를 호출한 뒤 D에 저장하고…"
- ✅ 단계: 1. A 입력 → 2. B 변환 → 3. C 호출 → 4. D 저장

#### 2-1. 터미널에서 안 깨지게 (읽는 화면이 좁다)
답변은 터미널에 그려진다. 넓은 화면을 가정하면 표가 접히고 줄이 늘어져 못 읽는다.

- **표는 2~3열까지.** 4열 이상이면 표를 버리고 항목별 소제목 + 불릿으로.
- **칸 하나는 짧게.** 한 칸이 20자를 넘길 것 같으면 그 정보는 표 밖 불릿으로 뺀다.
- **긴 문장·경로·명령을 표 안에 넣지 않는다.** 표는 "짧은 값 대조"에만.
- **한 줄은 80자 안쪽.** 길어지면 끊어 쓴다(문단·불릿 모두).
- **불릿은 2단계까지.** 3단계 들여쓰기는 좁은 폭에서 뭉개진다.
- 중첩 표·표 안 코드블록 금지.
- **빈 줄은 주제가 바뀔 때만.** 한 주제를 이어 말하는 문장들은 줄만 바꿔 붙여 쓴다.
  한 문장짜리 문단을 빈 줄로 계속 떼면 화면이 듬성듬성해져 읽는 눈이 멀리 뛴다.
  (§2 "빈 줄로 문단 분리"는 문단이 여러 줄일 때의 규칙이다)

**Why:** 표가 깨지면 정보가 아니라 소음이 된다. 좁은 폭에서 안전한 형식은 짧은 불릿이다.

#### 2-2. 문장마다 우선순위를 다르게 (밝기 위계)
전부 같은 밝기로 나오면 어디부터 읽을지 모른다. **한 답변 안에서 세 단계를 반드시 섞는다.**

| 단계 | 무엇을 | 어떻게 쓰나 |
|---|---|---|
| 1 | 결론·경고 | `## 제목` · `**굵게**` |
| 2 | 설명·근거 | 보통 글씨 |
| 3 | 부연·조건 | `> 인용문` · `` `코드` `` |

- **한 덩어리에 굵게는 한 곳.** 여러 곳을 굵게 하면 아무것도 안 튄다.
- **평평한 답변 금지.** 보통 글씨만 5줄 이상 이어지면 1단계나 3단계를 넣는다.
- 곁가지·전제·예외는 본문에 섞지 말고 `>` 줄로 내려 뒤로 물린다.

**Why:** 터미널은 밝기로만 위계를 표현한다(굵게=밝게, 인용=흐리게). 마크업을 안 쓰면
전부 같은 톤이라 눈이 어디에 멈춰야 할지 모른다.

### 3. 쉬운 말투 — 문장 자체를 쉽게
1·2가 "배치(레이아웃)"라면 이건 "문장 그 자체". 구조가 깔끔해도 문장이 어려우면 이해 안 됨.
- **짧은 문장.** 한 문장 = 한 생각. 쉼표로 길게 잇지 말고 끊기.
- **쉬운 말 우선.** 어려운 한자어·번역체 → 일상어로. (예: "상기 사항을 고려하여" → "이걸 감안하면")
- **작업 중 만든 조어·압축어를 답변에 그대로 쓰지 않는다.** 스킬·문서 안에서 쓰는 용어("저작"·"선띄움"·"실사"·"통짜"·"여정 realize")는 지시서용이다 — 사람에게 말할 땐 풀어서("만들기"·"미리 시작해 둠"·"직접 확인"·"한눈에 통째로"·"글을 실행되는 테스트로 옮기기"), 원어가 필요하면 괄호로만. (예: "여정 저작을 선띄움" ❌ → "테스트 코드 만들기를 미리 시작해 둬요(realize 배경 실행)" ⭕)
- **추상 → 구체.** 막연한 말 대신 숫자·예시. (예: "성능이 개선됨" → "로딩 3초 → 0.5초")
- **이중피동·번역투 금지.** "처리되어진다" → "처리한다". 능동·직접으로.
- **어려우면 비유 한 번.** 익숙한 것에 빗대기. (예: "캐시 = 자주 쓰는 물건을 책상 위에 두는 것")
- **보내기 전 자가 판정**: 답변 안에 일상 대화에서 안 쓸 단어가 있으면 그 문장을 다시 쓴다. "이 문장을 옆자리 동료에게 말로 하면 어색한가?"가 기준.

### 3-1. 복잡한 내용은 "실제 사건 → 원인 → 대책" 순으로 (기본 서술 틀)
어렵거나 복잡한 걸 설명할 땐 **구조 요약부터 던지지 말고 실제로 있었던 일부터** 말한다.

1. **무슨 일이 있었나** — 구체 사건 1개. 숫자·실제 값 포함. ("테스트 13개가 다 통과했는데 여백이 틀렸고 사람이 눈으로 발견했다")
2. **왜 그랬나** — 원인 한 문장 + 비유. ("테스트가 시안이 아니라 내가 베껴 적은 숫자와 비교했다 = 답안지를 틀리게 적고 채점")
3. **그래서 뭘 할 건가** — 대책. 여기서 **처음으로** 표를 써도 된다.

**금지**
- **내부 라벨 나열 금지** — `G8`·`STEP 4.6`·`단위 2b` 같은 코드번호는 사람 머릿속에 없다. 꼭 필요하면 뜻을 먼저 풀고 괄호로. ("눈으로 보는 대조를 앞으로 당기는 것(G8)")
- **한 답변에 표 3개 이상 금지.** 표는 요약 도구지 설명 도구가 아니다. 사건 서술을 표로 대체하지 않는다.
- **질문은 한 번에 하나.** 계획과 질문을 같이 쏟지 않는다.

**신호**: 사용자가 "왜 이렇게 안 읽히지", "무슨 말인지 모르겠어" → 즉시 이 틀로 다시 쓴다(§5 와 함께).
**Why:** 정확한 정보라도 구조 요약부터 나오면 읽는 사람이 맥락 없이 라벨만 받는다. 사건 하나를 먼저 주면 나머지가 거기 걸린다.

### 3-2. 사람이 읽는 산출물(md 문서·시각 문서)도 §3 그대로
채팅 답변뿐 아니라 **사람이 읽는 모든 산출물** — md 파일, 시각 문서(아티팩트/HTML), 보고서, 다이어그램 라벨 — 에 §0-2·§3 을 똑같이 적용한다.

- **쉬운 말을 앞에, 원어는 괄호·부기로만.** 예: "스모크" → "미리 열어보기 점검(스모크)", 에이전트 이름(`web-test-generator`)은 "테스트 작성 AI" 뒤 괄호나 작은 표기로.
- **예외 — 기계·에이전트가 읽는 지시서**(SKILL.md·에이전트 .md·룰 파일·코드)는 원 용어를 유지한다(정밀성이 우선). 독자가 사람인지 기계인지로 가른다.

**Why:** 2026-09-01 실제 사건 — 시각 문서와 답변에 "여정 저작·선띄움·범위 판정" 같은 지시서 용어를 그대로 써서 사용자가 "요즘 답변이 잘 이해가 안 간다"고 했다. 스킬 문서를 오래 다루다 보면 그 안의 조어가 내 기본 어휘가 되는데, 독자는 그 문서를 안 읽은 사람이다.

### 4. 전문 용어는 1줄 풀이
- 처음 등장하는 약어/도메인 용어는 **괄호로 즉시 풀이**.
- 예: "HMR(저장 시 페이지 새로고침 없이 모듈만 교체)이 안 잡는 케이스가..."
- 사용자가 명백히 아는 용어(JS/TS/React 등)는 풀이 생략.

### 5. 헷갈림 신호 = 다른 각도로 재구성
- 사용자가 "이해 안 가", "쉽게 설명해줘", "헷갈리네" → **같은 표현 반복 금지**. 비유/예시/구체화로 다시.
- ❌ 같은 문장에 단어만 바꿔 반복 → ✅ 매체를 바꿈 (비유·구체 예시·표/그림).

### 6. 코드 수정 설명 = 3요소 틀
코드를 수정했거나 기존 커밋/diff를 설명할 때는 **자세하고 쉽게**, 다음 3요소를 반드시 포함:
1. **무엇을 고쳤나** — 문제(왜 고쳐야 했는지) → 수정 내용을 before/after로. 식별자·타입·구조 변경은 코드 블록으로 대비.
2. **바뀐 파일** — 어떤 파일에서 무엇이 바뀌었는지 간단히.
3. **어디서 확인하나** — 검증할 UI 경로 + 클릭 순서 + 🎯 핵심 회귀 케이스.

커밋 직후·diff 설명·PR 본문 작성 시 이 틀을 적용. (위 스타일 규칙 그대로 — 결론 먼저, 쉬운 말투, 표/코드블록/bullet, 빈 줄 분리.)

**Why:** 정확해도 이해 못 하면 사용자가 다시 물어야 함 → 왕복 낭비. 한 번에 명확히 = 더 빠름. 특히 코드 변경은 "어디서 확인하냐"를 같이 줘야 사용자가 바로 검증 가능.

### 7. PR 본문 = "왜 + 효과" 중심 (단순 나열 금지)
PR 본문 작성 시 **무엇을 바꿨는지 나열에 그치지 말고**, 다음을 반드시 담는다:
1. **한 줄 요약** — 큰 그림에서 이 PR이 뭐하는 조각인지.
2. **왜 했나 (배경)** — 어떤 문제/필요 때문인지, 안 하면 뭐가 깨지는지. 어려운 개념은 **비유 한 번**.
3. **무엇을 했나** — 변경을 묶어서, 로직 변경은 before/after 코드블록.
4. **나타나는 효과** — 이 작업으로 뭐가 좋아지나를 **표로** (사용자·시스템 관점).
5. **검증** — 테스트 결과 + 🎯 핵심 회귀 케이스. (있으면 배포·적용 순서/주의)

위 스타일 규칙 그대로(결론 먼저·쉬운 말투·표/코드블록·빈 줄 분리·용어 풀이). 길이는 변경 복잡도에 비례. 구체 틀·gh 우회 팁은 `git-workflow` 스킬 참고.
**Why:** 리뷰어·미래의 나가 "왜 이렇게 했지"를 코드만 보고 재구성하는 비용을 없앰. 변경 나열은 diff가 이미 함 → PR은 맥락(왜)과 결과(효과)를 줘야 가치.

### 답변 전 셀프체크 (출력 직전, 매 답변)
보내기 전 한 번 훑기 — 긴 대화일수록 drift 나니 항상:
- 첫 줄에 결론 있나?
- 질문 복잡도에 맞는 길이인가? (단순 질문에 과한 구조 X)
- 5줄 넘는 단락 없나?
- 문장이 짧고 쉬운가? (만연체·번역투·어려운 한자어 없나)
- 비교/옵션은 표로 했나?
- 코드/명령은 별도 블록인가?
- 처음 쓰는 전문 용어 풀이했나?

---

## 프로세스 규율

### 1. 스킬/에이전트 선택 의무
작업 시작 전 적합한 스킬/에이전트를 먼저 선택한다. 직접 처리 금지. 사용 가능한 스킬은 `Skill` 툴 호출 시점에 시스템 프롬프트로 노출되니 거기서 고른다.

### 1-1. node 명령이 `MODULE_NOT_FOUND` 로 즉사하면 — 환경 문제다
`node`·`npx` 가 **자기 코드를 시작하기도 전에** `Cannot find module ... Require stack: internal/preload` 로 죽으면 프로젝트 문제가 아니다. cmux 가 `NODE_OPTIONS` 에 심어 둔 임시 파일(`$TMPDIR/cmux-claude-node-options/restore-node-options.cjs`)이 macOS 임시폴더 정리로 사라진 것이다.

- **조치**: `settings.json` 의 `env.NODE_OPTIONS` 가 덮어쓰므로 보통 안 겪는다. 그래도 나면 그 명령에만 `NODE_OPTIONS= ` 를 앞에 붙인다.
- **하지 말 것**: `npm install` 재실행·의존성 의심·제품 코드 디버깅. 원인이 레포 밖이라 무엇을 고쳐도 안 낫는다.
- **팀원이 겪으면**: 그 레포의 `.claude/settings.json`(커밋됨)에 같은 `env` 를 넣는다.

**Why:** 에러 메시지가 프로젝트 코드를 가리켜 오진을 유도한다. 스택별 스킬(dev-next 등)에 이 대응을 넣지 않는다 — 환경 문제라 특정 스택의 것이 아니고, 명령마다 접두사를 다는 방식으로는 어차피 다 못 막는다.

### 2. 로직 구현 — TDD + 분리
- **UI와 비즈니스/계산 로직 분리.** domain 함수는 React 몰라야 함 (props·hooks·JSX 의존 X). UI 레이어는 domain 함수 호출만.
- **복잡한 순수 함수**(정책 로직, domain.ts 변환, 계산식 등) 구현 시 코드 작성 **전** `superpowers:test-driven-development` 또는 `/tdd` 실행.

**Why:** 테스트 없이 구현 후 웹뷰 디버깅하면 시간 낭비. 명세 → 테스트 → 구현 순서가 효율. 로직 분리하면 테스트가 빠르고(DOM 안 띄움), UI 변경에 로직 안 깨짐.

### 3. 자동 커밋 금지
사용자가 명시적으로 요청하지 않으면 `git commit` 실행 금지. 계획 문서에 커밋 단계가 있어도 건너뛰고 사용자에게 물을 것. eslint/prettier 자동 실행은 OK.

### 3-1. Claude 서명 금지 (커밋·PR)
커밋 메시지·PR 본문에 **Claude 관련 서명 절대 넣지 말 것.** 기본 지시로 붙는 아래 항목을 모두 생략:
- 커밋: `Co-Authored-By: Claude ...` 라인 금지.
- PR 본문: `🤖 Generated with [Claude Code](...)` 류 문구 금지.
순수하게 변경 내용만 담는다.

### 3-2. 문서는 전부 세컨드브레인에 (레포 안에 남기지 않는다)
작업 노트·리포트·분석·인계 문서 등 **모든 문서 산출물**은 `/Users/yoon/SecondBrain/<프로젝트명>/` 에 저장한다. 폴더가 없으면 만든다(기존 예: `nest-frontend`·`huray-design-web`).

- **파일명**: `YYYY-MM-DD-제목.md`. 프런트매터에 `date`·`type`·`title`·`folder` 를 넣는다(기존 파일 형식을 따른다).
- **레포 안에 문서를 만들지 않는다** — `pipeline/notes/`·`docs/` 같은 레포 내부 경로에 작업 노트를 쌓지 않는다. 코드 레포는 코드와 그 레포를 쓰는 데 필요한 문서(README·룰·스킬)만.
- 프로젝트 규약(레포 CLAUDE.md 등)이 레포 안 경로를 지정하더라도 **이 규칙이 우선**한다. 충돌하면 알리고 세컨드브레인에 저장한다.
- 예외는 **그 레포를 쓰는 사람·에이전트가 읽어야 동작하는 문서**뿐(스킬 SKILL.md·룰 파일 등).

**Why:** 작업 기록이 레포마다 흩어지면 나중에 찾지 못한다. 한곳에 모아야 검색·연결이 된다.

### 4. UI 구현 (React + Tailwind)
UI/컴포넌트/화면을 만들 때는 `ui-implementation` 스킬을 따른다 (토큰 우선, 기존 컴포넌트 재사용, Cross-page 승격, Rule of Three, shadcn/Radix 베이스, 4px 배수, CDD). 피그마 시안 기반 변환은 `applying-figma-designs`와 함께 발동.

---

## Notion 접근
claude.ai OAuth 말고 SecondBrain 토큰으로 API 직접 호출: `set -a; source "$(ls -d ~/.claude/plugins/cache/huray/secondbrain/*/config/secrets.env|sort -V|tail -1)"; set +a` → `curl`에 `Authorization: Bearer $SB_NOTION_TOKEN`, `Notion-Version: 2022-06-28`.
생성 전 `POST /v1/search`로 부모 확인(TODO DB id `83080cab-57c3-479e-8fe5-d52ccf6bc4a0`). 토큰 값 노출 금지.


