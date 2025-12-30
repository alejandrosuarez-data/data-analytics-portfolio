import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    csv_path = Path("/Users/alejandrosuarez/Desktop/My Freelancing/Data Analyst/Data Projects/Amazon-Sales/Data/amazon_products_analysis.csv")

    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    print(df.columns.tolist())

    # ensure numeric
    df["has_coupon"] = pd.to_numeric(df["has_coupon"], errors="coerce")
    df["is_sponsored_flag"] = pd.to_numeric(df["is_sponsored_flag"], errors="coerce")
    df["avg_units"] = pd.to_numeric(df["avg_units"], errors="coerce")

    # pivot into 2x2 matrix
    pivot = df.pivot_table(
        index="has_coupon",
        columns="is_sponsored_flag",
        values="avg_units",
        aggfunc="mean"
    ).rename(
        index={0: "No Coupon", 1: "Has Coupon"},
        columns={0: "Organic", 1: "Sponsored"}
    )

    fig, ax = plt.subplots(figsize=(7, 4.5))
    im = ax.imshow(pivot.values)

    ax.set_xticks(range(pivot.shape[1]))
    ax.set_yticks(range(pivot.shape[0]))
    ax.set_xticklabels(pivot.columns)
    ax.set_yticklabels(pivot.index)

    ax.set_title("Avg Units Bought Last Month\nCoupon vs Sponsored")
    ax.set_xlabel("Sponsored Status")
    ax.set_ylabel("Coupon Status")

    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            val = pivot.values[i, j]
            ax.text(j, i, f"{val:,.0f}", ha="center", va="center")

    plt.colorbar(im, ax=ax, label="Avg Units")
    plt.tight_layout()
    plt.savefig("../figures/coupon_vs_sponsored.png", dpi=300)
    print("Figure saved to ../figures/coupon_vs_sponsored.png")
    plt.show()

if __name__ == "__main__":
    main()
