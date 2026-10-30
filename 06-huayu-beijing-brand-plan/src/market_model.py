"""Market sizing and three-year financial projection for the brand plan.

All parameters are illustrative assumptions used to demonstrate the model
structure; replace them with field data before any real decision.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass
class Assumptions:
    market_size_2023: float = 2.8e8       # 桦树皮画市场规模（元）
    market_growth: float = 0.185          # 年增速
    sam_share: float = 0.15               # 可服务市场占 TAM 比例
    som_share: float = 0.02               # 3 年可获得市场份额
    cogs_ratio: float = 0.45              # 营业成本率
    opex_fixed: float = 1_200_000         # 年固定运营成本
    marketing_ratio: float = 0.15         # 营销费用率


# 产品线：名称、单价、首年销量、年销量增速
PRODUCTS = [
    ("DIY 材料包", 99, 8000, 0.35),
    ("文创衍生", 299, 3000, 0.40),
    ("装饰画", 2999, 400, 0.25),
    ("高端定制", 20000, 30, 0.15),
    ("体验课程", 199, 2000, 0.30),
]


def market_sizing(a: Assumptions, years: int = 5) -> dict:
    tam = [a.market_size_2023 * (1 + a.market_growth) ** y for y in range(years)]
    sam = [x * a.sam_share for x in tam]
    som = [x * a.som_share for x in sam]
    return {
        "years": list(range(1, years + 1)),
        "TAM": [round(x / 1e4, 1) for x in tam],   # 万元
        "SAM": [round(x / 1e4, 1) for x in sam],
        "SOM": [round(x / 1e4, 1) for x in som],
        "unit": "万元",
    }


def revenue_projection(a: Assumptions, years: int = 3) -> list[dict]:
    rows = []
    for y in range(years):
        revenue = 0.0
        detail = {}
        for name, price, base_volume, growth in PRODUCTS:
            volume = base_volume * (1 + growth) ** y
            line = price * volume
            detail[name] = round(line / 1e4, 1)
            revenue += line
        cogs = revenue * a.cogs_ratio
        marketing = revenue * a.marketing_ratio
        profit = revenue - cogs - marketing - a.opex_fixed
        margin = profit / revenue if revenue else 0
        rows.append(
            {
                "year": y + 1,
                "revenue_wan": round(revenue / 1e4, 1),
                "cogs_wan": round(cogs / 1e4, 1),
                "marketing_wan": round(marketing / 1e4, 1),
                "opex_wan": round(a.opex_fixed / 1e4, 1),
                "net_profit_wan": round(profit / 1e4, 1),
                "net_margin": round(margin, 4),
                "by_product_wan": detail,
            }
        )
    return rows


def break_even(a: Assumptions) -> dict:
    """Break-even revenue given blended contribution margin."""
    contribution = 1 - a.cogs_ratio - a.marketing_ratio
    be_revenue = a.opex_fixed / contribution
    return {
        "contribution_margin": round(contribution, 4),
        "break_even_revenue_wan": round(be_revenue / 1e4, 1),
    }


def scenarios(a: Assumptions) -> dict:
    out = {}
    for name, factor in {"pessimistic": 0.7, "base": 1.0, "optimistic": 1.3}.items():
        rows = revenue_projection(a, years=3)
        out[name] = {
            "year3_revenue_wan": round(rows[-1]["revenue_wan"] * factor, 1),
            "year3_net_margin": round(rows[-1]["net_margin"], 4),
            "multiplier": factor,
        }
    return out


def run(a: Assumptions | None = None) -> dict:
    a = a or Assumptions()
    return {
        "assumptions": asdict(a),
        "market": market_sizing(a),
        "projection": revenue_projection(a),
        "break_even": break_even(a),
        "scenarios": scenarios(a),
    }
