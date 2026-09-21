import pandas as pd
import matplotlib.pyplot as plt


def load_df():
    df = pd.read_csv("Tabela4.csv", sep=";", decimal=",", encoding="latin1", header=None)
    df = df.dropna(axis=1, how="all")
    df = df.iloc[1:].copy()

    df.columns = ["Sigla", "Código", "Estado"] + [
        str(int(float(v))) for v in df.iloc[0, 3:]
    ]
    df = df.iloc[1:].copy().reset_index(drop=True)

    for c in df.columns[3:]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    return df


def rank_idh(df):
    r = df.sort_values("2024", ascending=False)
    print(r[["Sigla", "Estado", "2024"]])


def best_gain(df):
    df = df.copy()
    df["Melhora"] = df["2024"] - df["1991"]
    best = df.loc[df["Melhora"].idxmax()]
    print("\nEstado com maior melhora:")
    print(best[["Sigla", "Estado", "1991", "2024", "Melhora"]])
    return df


def worst_states(df):
    bad = df[df["Melhora"] < 0]
    print("\nEstados que tiveram piora:")
    print(bad[["Sigla", "Estado", "1991", "2024", "Melhora"]])


def long_df(df):
    anos = [c for c in df.columns if str(c).isdigit()]
    fix = [c for c in df.columns if c not in anos]

    long = df.melt(
        id_vars=fix,
        value_vars=anos,
        var_name="Ano",
        value_name="IDH",
    )
    long["Ano"] = long["Ano"].astype(int)
    long["IDH"] = pd.to_numeric(long["IDH"], errors="coerce")
    return long


def plot_mg(long):
    mg = long[long["Sigla"] == "MG"].sort_values("Ano")
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(mg["Ano"], mg["IDH"], marker="o", markersize=3, linewidth=1.5)
    ax.set_title("Evolução do IDH de Minas Gerais (1991–2024)")
    ax.set_xlabel("Ano")
    ax.set_ylabel("IDH")
    ax.set_ylim(0.3, 0.9)
    fig.tight_layout()
    plt.show()


def plot_states(long):
    fig, ax = plt.subplots(figsize=(12, 7))

    for sigla, g in long.groupby("Sigla"):
        g = g.sort_values("Ano")
        ax.plot(
            g["Ano"],
            g["IDH"],
            marker="o",
            markersize=3,
            linewidth=1.5,
            label=sigla,
        )

    ax.set_title("Evolução do IDH por estado (1991–2024)")
    ax.set_xlabel("Ano")
    ax.set_ylabel("IDH")
    ax.set_ylim(0.3, 0.9)
    ax.legend(ncol=3, bbox_to_anchor=(1.02, 1), loc="upper left", title="UF")
    fig.tight_layout()
    plt.show()


def main():
    df = load_df()
    rank_idh(df)
    df = best_gain(df)
    worst_states(df)
    long = long_df(df)
    plot_mg(long)
    plot_states(long)


if __name__ == "__main__":
    main()
