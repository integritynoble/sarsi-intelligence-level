#!/usr/bin/env python3
"""Figures and tables for the index paper, generated from records/index_sim/index_sim.json and the measured rows.

    python3 tools/index_paper_assets.py records/index_sim ../ail_index_v2
"""
from __future__ import annotations
import json, sys, glob
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 8, "font.family": "serif", "axes.grid": True, "grid.alpha": 0.25,
                     "axes.spines.top": False, "axes.spines.right": False, "figure.dpi": 200})

def fig_resolution(res, out: Path):
    r = res["resolution"]; key = [k for k in r["rows"][0] if k.startswith("items_for")][0]
    M = np.array([x["n_models"] for x in r["rows"]]); K = np.array([x[key] for x in r["rows"]], dtype=float)
    fig, ax = plt.subplots(figsize=(3.4, 2.5))
    ax.loglog(M, K, "o-", color="#17324D", label="measured")
    ref = K[0] * (M / M[0]) ** 2
    ax.loglog(M, ref, "--", color="#C05621", label=r"$\propto M^2$")
    ax.set_xlabel("models on the leaderboard, $M$"); ax.set_ylabel("items needed")
    ax.set_title(f"resolving neighbours: slope {r['log_log_slope']}", fontsize=8)
    ax.legend(frameon=False, fontsize=7); fig.tight_layout(); fig.savefig(out / "fig_resolution.pdf"); plt.close(fig)

def fig_saturation(res, out: Path):
    s = res["saturation"]; x = [r["frontier_logits"] for r in s]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.5))
    a1.plot(x, [r["composite_spread_fixed"] for r in s], "o-", color="#C05621", label="fixed suite")
    a1.plot(x, [r["composite_spread_refreshed"] for r in s], "s-", color="#3A7D44", label="refreshed witnesses")
    a1.set_xlabel("frontier advance (logits)"); a1.set_ylabel("spread of the bounded composite"); a1.set_ylim(0, None)
    a1.set_title("a fixed suite compresses", fontsize=8); a1.legend(frameon=False, fontsize=7)
    a2.plot(x, [r["separation_fixed"] for r in s], "o-", color="#C05621", label="fixed suite")
    a2.plot(x, [r["separation_refreshed"] for r in s], "s-", color="#3A7D44", label="refreshed witnesses")
    a2.plot(x, [r["at_ceiling_fixed"] for r in s], "^:", color="#2B6CB0", label="at ceiling (fixed)")
    a2.set_xlabel("frontier advance (logits)"); a2.set_ylabel("separation reliability / share")
    a2.set_title("and stops separating", fontsize=8); a2.legend(frameon=False, fontsize=7)
    fig.tight_layout(); fig.savefig(out / "fig_saturation.pdf"); plt.close(fig)

def tex_sample(res) -> str:
    rows = res["sample_requirements"]; items = sorted({r["n_items"] for r in rows}); grid = {}
    for r in rows: grid.setdefault(r["n_models"], {})[r["n_items"]] = r
    head = " & ".join(["$M$"] + [f"$K={k}$" for k in items])
    body = []
    for m in sorted(grid):
        cells = []
        for k in items:
            g = grid[m][k]; cells.append(f"{g['spearman']:.2f} / {g['adjacent_pairs_separated']:.2f} / {g['median_se']:.2f}")
        body.append(" & ".join([str(m)] + cells) + r" \\")
    return (r"\begin{tabular}{@{}l" + "c" * len(items) + r"@{}}\toprule" + "\n" + head + r" \\ \midrule" + "\n" +
            "\n".join(body) + "\n" + r"\bottomrule\end{tabular}")

def tex_saturation(res) -> str:
    s = res["saturation"]
    rows = [f"{r['frontier_logits']} & {r['composite_mean_fixed']:.2f} & {r['composite_spread_fixed']:.3f} & {r['composite_spread_refreshed']:.3f} & {r['separation_fixed']:.2f} & {r['separation_refreshed']:.2f} & {r['at_ceiling_fixed']:.2f} \\\\" for r in s]
    return (r"\begin{tabular}{@{}lcccccc@{}}\toprule Frontier & \multicolumn{3}{c}{bounded composite} & \multicolumn{2}{c}{separation} & at ceiling \\ \cmidrule(lr){2-4}\cmidrule(lr){5-6}"
            + "\n" + r"(logits) & mean, fixed & spread, fixed & spread, refreshed & fixed & refreshed & fixed \\ \midrule" + "\n" + "\n".join(rows) + "\n" + r"\bottomrule\end{tabular}")

def tex_coverage(res) -> str:
    rows = [f"{r['coverage']} & {r['spearman']:.3f} & {r['median_se']:.2f} & {r['median_se_partial_models']:.2f} \\\\" for r in res["coverage"]]
    return (r"\begin{tabular}{@{}lccc@{}}\toprule Coverage & Spearman & median SE & SE, partial models \\ \midrule" + "\n" + "\n".join(rows) + "\n" + r"\bottomrule\end{tabular}")

ROWS = [   # the bare-model index readings this paper publishes, named explicitly: a glob over records/ also matches
           # pair calibration runs and superseded runs, which are not index rows
    ("index_deepseek.json", "DeepSeek \\texttt{deepseek-chat}", "public, 3 seeds/family"),
    ("private_llm_deepseek.json", "DeepSeek \\texttt{deepseek-chat}", "private, 4 salt-derived seeds"),
    ("index_qwen.json", "Qwen 3.8 27B \\texttt{qwen3.8:27b}", "public, 3 seeds/family"),
]

def tex_rows(pkg: Path) -> str:
    out = []
    for fname, label, split in ROWS:
        R = json.loads((pkg / "records" / fname).read_text())
        ix = R.get("index"); hil = R.get("hil") or R.get("HIL")
        if ix:
            c, score, gain = ix["curve"], ix["HIL_Index"], ix["harness_gain"]
            fcr, dec = ix["false_completion_rate"], ix["decline_rate"]; b = ix.get("bare", {})
        else:
            c, score, gain = hil["curve"], hil["HIL_score"], hil["harness_gain"]
            eps = [e for v in R.get("rungs", {}).values() for e in v.get("episodes", [])]; n = max(len(eps), 1)
            fcr = sum(1 for e in eps if e.get("false_completion")) / n; dec = sum(1 for e in eps if e.get("held_back")) / n
            b = R.get("rungs", {}).get("HG0", {}).get("profile", {}) or {}
        prof = ", ".join(str(b.get(k)) for k in ("C", "SA", "T_frontier") if b.get(k))
        out.append(f"{label} & {split} & \\textbf{{{score}}} & {c['HG0']}/{c['HG1']}/{c['HG2']} & {gain} & {fcr:.2f} & {dec:.2f} & {prof} \\\\")
    return (r"\begin{tabular}{@{}p{3.2cm}p{2.4cm}cccc c>{\raggedright\arraybackslash}p{1.5cm}@{}}\toprule Model & Split & Index & HG0/HG1/HG2 & Gain & FCR & Decl. & Profile \\ \midrule" + "\n" + "\n".join(out) + "\n" + r"\bottomrule\end{tabular}")

def main(res_dir: Path, out: Path):
    res = json.loads((res_dir / "index_sim.json").read_text()); out.mkdir(parents=True, exist_ok=True)
    fig_resolution(res, out); fig_saturation(res, out)
    pkg = Path(__file__).resolve().parents[1]
    (out / "tab_sample.tex").write_text(tex_sample(res))
    (out / "tab_saturation.tex").write_text(tex_saturation(res))
    (out / "tab_coverage.tex").write_text(tex_coverage(res))
    (out / "tab_rows.tex").write_text(tex_rows(pkg))
    e = res["equating"]; r = res["resolution"]; b = res["bluff"]
    facts = {"equating": e, "resolution_slope": r["log_log_slope"],
             "resolution_rows": {x["n_models"]: x[[k for k in x if k.startswith("items_for")][0]] for x in r["rows"]},
             "bluff_share": b["share_where_net_reverses_the_order"],
             "saturation_first": res["saturation"][0], "saturation_last": res["saturation"][-1],
             "coverage": {x["coverage"]: x for x in res["coverage"]}}
    (out / "facts.json").write_text(json.dumps(facts, indent=1))
    print("assets:", sorted(p.name for p in out.glob("*.tex")), "+ 2 figures"); print(json.dumps(facts, indent=1)[:900])

if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
