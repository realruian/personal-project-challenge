"""个人项目挑战 · 周中作业大纲 课件组装脚本

读取 coursedeck skill 的 shell_sidebar 骨架，替换占位符（logo、目录、slide），
输出单文件 HTML 到 课件/index.html。重跑覆盖即可。
"""

from pathlib import Path

SKILL = Path("/Users/tianruian/.claude/skills/coursedeck")
OUT = Path(__file__).parent / "课件" / "index.html"

DECK_TITLE = "个人项目挑战 · 周中作业大纲"

# ─────────────────────────────────────────────
# 目录树（modify 这里要同步页码 data-idx）
# ─────────────────────────────────────────────
TOC = [
    ("ch",  0, "CH 00 · 开场"),
    ("sub", 0, "封面"),
    ("ch",  1, "CH 01 · 课堂收尾"),
    ("sub", 1, "赛制三件套"),
    ("sub", 2, "产品方法论"),
    ("sub", 3, "奖励"),
    ("ch",  4, "CH 02 · 周中任务"),
    ("sub", 4, "章节页"),
    ("sub", 5, "周一 · 体验日"),
    ("sub", 6, "周二 · 方向 + 提案"),
    ("sub", 7, "周四 · 搭出 1.0"),
    ("ch",  8, "CH 03 · 下周检查"),
    ("sub", 8, "章节页"),
    ("sub", 9, "交付物清单"),
    ("sub", 10, "评审 + 颁奖"),
    ("sub", 11, "Let's ship it"),
]


def toc_html() -> str:
    lines = []
    for kind, idx, label in TOC:
        cls = f"toc-item {kind}"
        lines.append(f'    <a class="{cls}" data-idx="{idx}">{label}</a>')
    return "\n".join(lines)


# ─────────────────────────────────────────────
# 13 个 slide
# ─────────────────────────────────────────────
SLIDES = [
    # ───── 1. 封面 ─────
    """
<section class="slide active">
  <div class="eyebrow">Personal Project Challenge · 2026</div>
  <h1 class="display h-xxl">个人项目<br>挑战赛</h1>
  <p class="body-xl mt-l">一周 · 一人 · 一个真实可演示的产品</p>
  <p style="position:absolute;bottom:110px;left:290px;font-size:22px;letter-spacing:2px;color:var(--text-secondary);font-weight:500">课堂收尾 · 周中任务 · 下周交付</p>
</section>
""",

    # ───── 2. 赛制三件套 ─────
    """
<section class="slide center">
  <div class="slide-header"><span></span><span>赛制 / Format</span></div>
  <div class="top-title">赛制三件套</div>
  <div class="three-col mt-xl" style="width:100%;max-width:1500px">
    <div class="step-card">
      <div class="step-num">Rule 01</div>
      <div class="step-title">自选题</div>
      <div class="step-desc">不设方向限制，<strong>自己定题目</strong>——选你真正想做、能 demo 给别人看的产品。</div>
    </div>
    <div class="step-card">
      <div class="step-num">Rule 02</div>
      <div class="step-title">独立完成</div>
      <div class="step-desc"><strong>每人独立交付 1 个产品</strong>。可以借鉴、可以请教，但成品必须是你自己跑通的。</div>
    </div>
    <div class="step-card">
      <div class="step-num">Rule 03</div>
      <div class="step-title">真实可演示</div>
      <div class="step-desc">线上可访问的 MVP——<strong>不是 PPT，是能点的产品</strong>。</div>
    </div>
  </div>
</section>
""",

    # ───── 4. 产品方法论 ─────
    """
<section class="slide center">
  <div class="slide-header"><span></span><span>方法 / Methodology</span></div>
  <div class="top-title">按产品标准流程开发</div>
  <div class="mt-l" style="display:flex;align-items:center;gap:28px;flex-wrap:nowrap">
    <div class="step-card" style="min-width:230px;text-align:center">
      <div class="step-num">Step 01</div>
      <div class="step-title" style="font-size:42px">需求</div>
      <div class="step-desc">给谁 · 解决什么</div>
    </div>
    <span style="font-size:48px;color:var(--text-meta);font-family:'JetBrains Mono',monospace">→</span>
    <div class="step-card" style="min-width:230px;text-align:center">
      <div class="step-num">Step 02</div>
      <div class="step-title" style="font-size:42px">提案</div>
      <div class="step-desc">HTML 可视化页面</div>
    </div>
    <span style="font-size:48px;color:var(--text-meta);font-family:'JetBrains Mono',monospace">→</span>
    <div class="step-card" style="min-width:230px;text-align:center">
      <div class="step-num">Step 03</div>
      <div class="step-title" style="font-size:42px">MVP</div>
      <div class="step-desc">能演示的 1.0</div>
    </div>
    <span style="font-size:48px;color:var(--text-meta);font-family:'JetBrains Mono',monospace">→</span>
    <div class="step-card" style="min-width:230px;text-align:center">
      <div class="step-num">Step 04</div>
      <div class="step-title" style="font-size:42px">验证</div>
      <div class="step-desc">真用户 · 真反馈</div>
    </div>
  </div>
  <p class="body-l mt-xl" style="max-width:1500px;text-align:center">不允许跳步——<strong>提案没过不写代码，MVP 没跑通不上线</strong>。</p>
</section>
""",

    # ───── 5. 奖励大字 ─────
    """
<section class="slide">
  <div class="slide-header"><span>Reward · 唯一名额</span><span>获胜奖励</span></div>
  <div class="eyebrow">Winner Takes</div>
  <div class="big-stat">
    <div class="num">$100<span class="unit">Apple Gift Card</span></div>
    <div class="label">One Winner · Picked By Demo Day</div>
  </div>
  <p class="body-l mt-xl" style="max-width:1500px">评审看的不是代码量，而是<strong>产品完整度 + 真实可用</strong>。下周演示日见。</p>
</section>
""",

    # ───── 6. CH02 章节 ─────
    """
<section class="slide">
  <div class="slide-header"><span>Chapter 02</span><span>周中任务</span></div>
  <div class="chapter-watermark">02</div>
  <div class="chapter">
    <span class="num">Chapter 02</span>
    <h2 class="title">周中任务</h2>
    <div class="sub">按日推进 · 每天一个明确动作 · 群内有迹可循</div>
  </div>
</section>
""",

    # ───── 7. 周一 · 体验日 ─────
    """
<section class="slide center">
  <div class="slide-header"><span></span><span>AI 产品体验日</span></div>
  <div class="top-title">周一 · AI 产品体验日</div>
  <div class="mt-l" style="display:grid;grid-template-columns:520px 1fr;gap:56px;width:100%;align-items:stretch;max-width:1500px">
    <div style="display:flex;flex-direction:column;justify-content:center;align-items:flex-start;border:1.5px solid var(--border);border-radius:20px;padding:48px 44px">
      <div class="mono" style="font-size:16px;letter-spacing:2.5px;text-transform:uppercase;color:var(--text-meta);font-weight:600">Mon · D+1</div>
      <div style="font-size:220px;font-weight:700;line-height:0.95;letter-spacing:-0.04em;color:var(--text);margin-top:24px">10<span style="font-size:72px;color:var(--text-secondary);margin-left:8px">款</span></div>
      <div class="mono" style="font-size:20px;letter-spacing:2px;color:var(--text-meta);margin-top:24px;font-weight:600">HANDS-ON · 1 DAY</div>
    </div>
    <div style="display:flex;flex-direction:column;gap:18px;justify-content:center">
      <div class="step-card" style="padding:32px 36px">
        <div class="step-num">Action 01 · 私下做</div>
        <div class="step-title" style="font-size:36px;margin:14px 0 14px">体验 10 个 AI 产品</div>
        <div class="step-desc" style="font-size:22px">覆盖不同<strong>赛道 / 形态 / 用户群</strong>——建立信息源与基线。</div>
      </div>
      <div class="step-card" style="padding:32px 36px">
        <div class="step-num">Action 02 · 群内</div>
        <div class="step-title" style="font-size:36px;margin:14px 0 14px">分享最值得参考的 1 个</div>
        <div class="step-desc" style="font-size:22px"><strong>一句话说明好在哪</strong>——亮点、可借鉴点，不要凑字数。</div>
      </div>
    </div>
  </div>
</section>
""",

    # ───── 8. 周二 · 方向 + 提案 ─────
    """
<section class="slide center">
  <div class="slide-header"><span></span><span>方向确认 + 提案</span></div>
  <div class="top-title">周二 · 方向确认 + 提案</div>
  <div class="mt-l" style="display:grid;grid-template-columns:520px 1fr;gap:56px;width:100%;align-items:stretch;max-width:1500px">
    <div style="display:flex;flex-direction:column;justify-content:center;align-items:flex-start;border:1.5px solid var(--border);border-radius:20px;padding:48px 44px">
      <div class="mono" style="font-size:16px;letter-spacing:2.5px;text-transform:uppercase;color:var(--text-meta);font-weight:600">Tue · D+2</div>
      <div style="font-size:220px;font-weight:700;line-height:0.95;letter-spacing:-0.04em;color:var(--text);margin-top:24px">1<span style="font-size:72px;color:var(--text-secondary);margin-left:8px">页</span></div>
      <div class="mono" style="font-size:20px;letter-spacing:2px;color:var(--text-meta);margin-top:24px;font-weight:600">PROPOSAL · HTML</div>
    </div>
    <div style="display:flex;flex-direction:column;gap:18px;justify-content:center">
      <div class="step-card" style="padding:32px 36px">
        <div class="step-num">Action 01 · 收敛</div>
        <div class="step-title" style="font-size:36px;margin:14px 0 14px">选定赛道</div>
        <div class="step-desc" style="font-size:22px">从周一体验中收敛——<strong>挑你真正能做下去的一条</strong>。</div>
      </div>
      <div class="step-card" style="padding:32px 36px">
        <div class="step-num">Action 02 · 交付</div>
        <div class="step-title" style="font-size:36px;margin:14px 0 14px">提案：给谁 → 解决什么</div>
        <div class="step-desc" style="font-size:22px"><strong>HTML 可视化页面</strong>——目标用户 / 场景 / 问题。</div>
      </div>
    </div>
  </div>
</section>
""",

    # ───── 9. 周四 · MVP ─────
    """
<section class="slide center">
  <div class="slide-header"><span></span><span>搭出 1.0</span></div>
  <div class="top-title">周四 · 搭出 1.0（MVP）</div>
  <div class="mt-l" style="display:grid;grid-template-columns:520px 1fr;gap:56px;width:100%;align-items:stretch;max-width:1500px">
    <div style="display:flex;flex-direction:column;justify-content:center;align-items:flex-start;border:1.5px solid var(--border);border-radius:20px;padding:48px 44px">
      <div class="mono" style="font-size:16px;letter-spacing:2.5px;text-transform:uppercase;color:var(--text-meta);font-weight:600">Thu · D+4</div>
      <div style="font-size:220px;font-weight:700;line-height:0.95;letter-spacing:-0.04em;color:var(--text);margin-top:24px">1.0</div>
      <div class="mono" style="font-size:20px;letter-spacing:2px;color:var(--text-meta);margin-top:24px;font-weight:600">MINIMUM VIABLE · ONLINE</div>
    </div>
    <div style="display:flex;flex-direction:column;gap:18px;justify-content:center">
      <div class="step-card" style="padding:32px 36px">
        <div class="step-num">Action 01 · 推进</div>
        <div class="step-title" style="font-size:36px;margin:14px 0 14px">按方法论做出初版</div>
        <div class="step-desc" style="font-size:22px">从提案直接推到 MVP——<strong>能跑通主流程，能给别人点</strong>。</div>
      </div>
      <div class="step-card" style="padding:32px 36px">
        <div class="step-num">Action 02 · 群内</div>
        <div class="step-title" style="font-size:36px;margin:14px 0 14px">晒进度</div>
        <div class="step-desc" style="font-size:22px">截图 / 短视频 / 线上链接均可——<strong>看得见才能被点评</strong>。</div>
      </div>
    </div>
  </div>
</section>
""",

    # ───── 10. CH03 章节 ─────
    """
<section class="slide">
  <div class="slide-header"><span>Chapter 03</span><span>下周检查</span></div>
  <div class="chapter-watermark">03</div>
  <div class="chapter">
    <span class="num">Chapter 03</span>
    <h2 class="title">下周检查</h2>
    <div class="sub">交付物清单 · 演示日 · 评审颁奖</div>
  </div>
</section>
""",

    # ───── 11. 交付物清单 ─────
    """
<section class="slide center">
  <div class="slide-header"><span></span><span>交付物 / Deliverables</span></div>
  <div class="top-title">下周要交的三样东西</div>
  <div class="three-col mt-xl" style="width:100%;max-width:1500px">
    <div class="step-card">
      <div class="step-num">Deliverable 01</div>
      <div class="step-title">项目 1.0</div>
      <div class="step-desc"><strong>可演示的线上 MVP</strong>——访问链接 + 主流程跑通。</div>
    </div>
    <div class="step-card">
      <div class="step-num">Deliverable 02</div>
      <div class="step-title">提案</div>
      <div class="step-desc">HTML 可视化页面：<strong>给谁 → 解决什么场景的问题</strong>。</div>
    </div>
    <div class="step-card">
      <div class="step-num">Deliverable 03</div>
      <div class="step-title">复盘</div>
      <div class="step-desc"><strong>踩了哪个坑 · 怎么解决的</strong>——文字 / 录屏 / 一段话都行。</div>
    </div>
  </div>
</section>
""",

    # ───── 12. 评审 + 颁奖 ─────
    """
<section class="slide center">
  <div class="slide-header"><span>Demo Day</span><span>评审 + 颁奖</span></div>
  <div class="top-title">演示三件套 · 现场颁奖</div>
  <div class="three-col mt-xl" style="width:100%;max-width:1500px">
    <div class="step-card">
      <div class="step-num">Demo 01</div>
      <div class="step-title">线上产品</div>
      <div class="step-desc">现场打开链接 · 跑一遍主流程 · <strong>不准截图代替</strong>。</div>
    </div>
    <div class="step-card">
      <div class="step-num">Demo 02</div>
      <div class="step-title">官网</div>
      <div class="step-desc">一张能说服别人的落地页：<strong>是什么 · 给谁 · 怎么用</strong>。</div>
    </div>
    <div class="step-card">
      <div class="step-num">Demo 03</div>
      <div class="step-title">演示视频</div>
      <div class="step-desc">60 秒以内 · <strong>不解释，直接看效果</strong>。</div>
    </div>
  </div>
  <p class="body-l mt-xl" style="max-width:1500px;text-align:center">评审打分 → 现场颁出 <span class="hl">$100 Apple Gift Card</span>。</p>
</section>
""",

    # ───── 13. 收尾 ─────
    """
<section class="slide">
  <div class="slide-header"><span>End of Briefing</span><span>Let's Ship It</span></div>
  <h2 class="display h-l" style="max-width:1500px">
    下课就开始<br><span class="hl">7 天</span>后见。
  </h2>
  <p class="body-l mt-xl" style="max-width:1500px">
    周一体验 · 周二提案 · 周四 MVP · 下周演示。
  </p>
  <p style="position:absolute;bottom:110px;left:290px;font-size:22px;letter-spacing:2px;color:var(--text-secondary);font-weight:500">问题随时群里抛 · 卡住先看自己的提案</p>
</section>
""",
]


def main():
    shell = (SKILL / "templates" / "shell_sidebar.html").read_text(encoding="utf-8")
    logo = (SKILL / "assets" / "logo.svg").read_text(encoding="utf-8")

    # 删除 shell 里的占位 slide（active）
    start = shell.find("<!-- ⬇️ 在此插入 slide ⬇️ -->")
    end = shell.find("<!-- ⬆️ slide 结束 ⬆️ -->")
    assert start > 0 and end > start, "找不到 slide 占位区"

    body_slides = "\n".join(s.strip() for s in SLIDES)
    new_shell = (
        shell[: start + len("<!-- ⬇️ 在此插入 slide ⬇️ -->")]
        + "\n\n" + body_slides + "\n\n"
        + shell[end:]
    )

    new_shell = new_shell.replace("{{DECK_TITLE}}", DECK_TITLE)
    new_shell = new_shell.replace("{{LOGO_SVG}}", logo)
    new_shell = new_shell.replace("{{TOC_ITEMS}}", toc_html())

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(new_shell, encoding="utf-8")
    print(f"OK · {OUT} · {len(SLIDES)} slides")


if __name__ == "__main__":
    main()
