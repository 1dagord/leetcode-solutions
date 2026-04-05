import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from enum import StrEnum
from matplotlib.gridspec import GridSpec
from pathlib import Path
from .graphql import Queries, Variables
from .leetcode import Response



class Color(StrEnum):
    EASY = "#51A7A8"
    MEDIUM = "#F4BA40"
    HARD = "#D34740"

class Plotter(ABC):
    def show(self):
        plt.show()

    @classmethod
    def save(cls):
        filename = cls.__name__.replace("Plotter", "") + ".png"
        plt.savefig(Path(__file__).parent.parent / "assets" / filename)

    @abstractmethod
    def plot(self):
        ...

class ProblemsSolvedPlotter(Plotter):
    def __init__(self):
        self.response = Response(Queries.PROBLEMS_SOLVED)

    def plot(self):
        """Creates pie chart of difficulties of solved problems"""
        _all, *difficulties = [
            obj
            for obj in self.response.matchedUser \
                .get("submitStatsGlobal") \
                .get("acSubmissionNum")
        ]
        difficulties = dict(map(lambda d: d.values(), difficulties))

        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            difficulties.values()
            , labels=list(map(lambda c: (c.name.title()), Color))
            , colors=list(map(lambda c: c.value, Color))
            , autopct=lambda pct: "{:.0f}\n{:.2f}%".format(
                pct / 100 * _all.get("count"),
                pct
            )
            , textprops=dict(color="w")
            , radius=1.2
            # , pctdistance=0.7
            , startangle=-90
        )
        plt.setp(autotexts, size=12, weight="bold")
        plt.title("LeetCode Submission Difficulty")

class ProblemsSolvedWithPercentilesPlotter(Plotter):
    def __init__(self):
        self.response = Response(Queries.PROBLEMS_SOLVED)

    def plot(self):
        """
            Creates pie chart of difficulties of solved
            problems with percentiles, all as pie plots
        """
        _all, *difficulties = [
            obj
            for obj in self.response.matchedUser \
                .get("submitStatsGlobal") \
                .get("acSubmissionNum")
        ]
        difficulties = dict(map(lambda d: d.values(), difficulties))

        percentages = [
            obj
            for obj in self.response \
                .matchedUser \
                .get("problemsSolvedBeatsStats")
        ]
        percentages = dict(map(lambda p: p.values(), percentages))

        fig = plt.figure()
        gs = GridSpec(2, 3, height_ratios=[2, 1])
        ax0 = fig.add_subplot(gs[:-1, :])
        ax1 = fig.add_subplot(gs[-1, 0])
        ax2 = fig.add_subplot(gs[-1, 1])
        ax3 = fig.add_subplot(gs[-1, 2])
        
        wedges, texts, autotexts = ax0.pie(
            difficulties.values()
            , labels=list(map(lambda c: (c.name.title()), Color))
            , colors=list(map(lambda c: c.value, Color))
            , autopct=lambda pct: "{:.0f}".format(
                pct / 100 * _all.get("count")
            )
            , textprops=dict(color="w")
            , radius=1.2
            # , pctdistance=0.7
            , startangle=-90
        )
        ax0.legend(
            wedges, difficulties.keys()
            , title="Difficulty"
            , loc="center right"
            , bbox_to_anchor=(1.25, 0, 0.5, 1)
        )
        ax0.set_title("Number of Solved LeetCode Problems")
        plt.setp(autotexts, size=12, weight="bold")

        for ax, (diff, pct) in zip([ax1, ax2, ax3], percentages.items()):
            wedges, texts = ax.pie(
                [pct, 100 - pct]
                # , labels=[diff, None]
                , colors=[getattr(Color, diff.upper()), (0,0,0,0)]
                # , autopct=lambda p: f"{p:.2f}%" if p == pct else None
                # , pctdistance=0.3
                , startangle=90
            )
            ax.set_xlabel(f"{diff}\n{pct}%", weight="bold")
            plt.setp(texts, size=10, weight="bold")

        small_plots = fig.add_subplot(gs[-1, :])
        small_plots.axis('off')
        small_plots.set_title("Percentiles by Difficulty")


if __name__ == "__main__":
    plotter = ProblemsSolvedPlotter()
    plotter.plot()
    plotter.save()
    # plotter.show()