import matplotlib
import numpy as np
import argparse as ag
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

# argument parsing
parser = ag.ArgumentParser(description="""Universal command line plotting script
                           using python3 and libraries: argparse, numpy and
                           matplotlib.""")
parser.add_argument("plottype", type=str, metavar="ptype", default="xy",
                    choices=["xy", "bar", "hist"],
                    help="type of plot")
parser.add_argument("files", type=str, nargs="+",
                    help="data files to plot from")
parser.add_argument("--stack", "-s", action="store_true", default=False,
                    help="stack file columns in one plot.")
parser.add_argument("--join", "-j", action="store_true", default=False,
                    help="join file columns in one plot.")
parser.add_argument("--bins", "-b", type=int, default=100,
                    help="number of bins for histogram.")
parser.add_argument("--cols", "-c", type=int, nargs="+",
                    help="columns to plot.")
parser.add_argument("--linestyle", "-ls", type=str, default="solid",
                    choices=["solid", "dashed", "dashdot", "dotted", "none"],
                    help="Linestyle to draw with")
parser.add_argument("--marker", "-m", type=str, default=" ",
                    choices=[".", ",", "o", "s", "x", "+", "^", "v", " "],
                    help="Style of marker to draw with")
parser.add_argument("--skip", type=int, default=1,
                    help="Data point interval with which to plot")
args = parser.parse_args()

# argument logic
if args.stack and args.join:
    raise Exception("Cannot use --join and --stack simultaneously!")
ls_dict = {"solid": "-",
           "dashed": "--",
           "dashdot": "-.",
           "dotted": ":",
           "none": " "}
args.linestyle = ls_dict[args.linestyle]

# reading data from files
data = []
shapes = []
for i, file in enumerate(args.files):
    try:
        data.append(np.genfromtxt(file))
        shapes.append(data[i].shape)
    except OSError:
        print(f"Error: File <{file}> not found!")


# plotting xy
if args.plottype == "xy":
    # stacked
    if args.stack:
        for file in range(len(data)):
            if args.cols:
                cols = args.cols
            else:
                cols = range(1, shapes[file][-1])
            fig, ax = plt.subplots(len(cols), sharex=True)
            for i, col in enumerate(cols):
                ax[i].plot(data[file][::args.skip, 0],
                           data[file][::args.skip, col],
                           color=f"C{col - 1}",
                           linestyle=args.linestyle,
                           marker=args.marker,
                           label=f"col:{col}")
                ax[i].legend(frameon=False)
            fig.suptitle(f"{args.files[file]}")
            plt.tight_layout()
            if file == len(data) - 1:
                plt.show(block=True)
            else:
                plt.show(block=False)
    # joined
    if args.join:
        for file in range(len(data)):
            fig, ax = plt.subplots()
            if args.cols:
                cols = args.cols
            else:
                cols = range(1, shapes[file][-1])
            for col in cols:
                ax.plot(data[file][::args.skip, 0],
                        data[file][::args.skip, col],
                        color=f"C{col - 1}",
                        linestyle=args.linestyle,
                        marker=args.marker,
                        label=f"col:{col}")
                ax.legend(frameon=False)
            fig.suptitle(f"{args.files[file]}")
            plt.tight_layout()
            if file == len(data) - 1:
                plt.show(block=True)
            else:
                plt.show(block=False)
    # unstacked and unjoin
    if not args.stack and not args.join:
        for file in range(len(data)):
            if args.cols:
                cols = args.cols
            else:
                cols = range(1, shapes[file][-1])
            for col in cols:
                fig, ax = plt.subplots()
                ax.plot(data[file][::args.skip, 0],
                        data[file][::args.skip, col],
                        color=f"C{col - 1}",
                        linestyle=args.linestyle,
                        marker=args.marker)
                fig.suptitle(f"{args.files[file]}:{col}")
                plt.tight_layout()
                if file == len(data) - 1 and col == cols[-1]:
                    plt.show(block=True)
                else:
                    plt.show(block=False)

# plotting bar
if args.plottype == "bar":
    # stacked
    if args.stack:
        for file in range(len(data)):
            if args.cols:
                cols = args.cols
            else:
                cols = range(1, shapes[file][-1])
            fig, ax = plt.subplots(len(cols), sharex=True)
            for i, col in enumerate(cols):
                ax[i].bar(data[file][:, 0], data[file][:, col],
                          width=0.9 * (data[file][1, 0] - data[file][0, 0]),
                          color=f"C{col - 1}", label=f"col:{col}")
                ax[i].legend(frameon=False)
            fig.suptitle(f"{args.files[file]}")
            plt.tight_layout()
            if file == len(data) - 1:
                plt.show(block=True)
            else:
                plt.show(block=False)
    # unstacked and unjoin
    if not args.stack and not args.join:
        for file in range(len(data)):
            if args.cols:
                cols = args.cols
            else:
                cols = range(1, shapes[file][-1])
            for col in cols:
                fig, ax = plt.subplots()
                ax.bar(data[file][:, 0], data[file][:, col],
                       width=0.9 * (data[file][1, 0] - data[file][0, 0]),
                       label=f"{args.files[file]}:{col}")
                ax.legend(frameon=False)
                plt.tight_layout()
                if file == len(data) - 1 and col == cols[-1]:
                    plt.show(block=True)
                else:
                    plt.show(block=False)
    if args.join:
        raise Exception("Cannot use --join with plottype bar!")

# plotting hist
if args.plottype == "hist":
    # unstacked and unjoin
    if not args.stack and not args.join:
        for file in range(len(data)):
            if args.cols:
                cols = args.cols
            else:
                cols = range(1, shapes[file][-1])
            for col in cols:
                fig, ax = plt.subplots()
                ax.hist(data[file][:, col],
                        label=f"{args.files[file]}:{col}")
                ax.legend(frameon=False)
                plt.tight_layout()
                if file == len(data) - 1 and col == cols[-1]:
                    plt.show(block=True)
                else:
                    plt.show(block=False)
    # stacked
    if args.stack:
        for file in range(len(data)):
            if args.cols:
                cols = args.cols
            else:
                cols = range(1, shapes[file][-1])
            fig, ax = plt.subplots(len(cols), sharex=True)
            for i, col in enumerate(cols):
                ax[i].hist(data[file][:, col], bins=args.bins,
                           color=f"C{col - 1}", label=f"col:{col}")
                ax[i].legend(frameon=False)
            fig.suptitle(f"{args.files[file]}")
            plt.tight_layout()
            if file == len(data) - 1:
                plt.show(block=True)
            else:
                plt.show(block=False)
    if args.join:
        raise Exception("Cannot use --join with plottype bar!")
