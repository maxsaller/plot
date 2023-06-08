## General purpose plotting script

| **Contents**                       |
|------------------------------------|
| 1. [Installation](#installation)   |
| 2. [Functionality](#functionality) |

## Installation
The script is written in `python3` and requires the following libraries

|                |                                                                               |
|----------------|-------------------------------------------------------------------------------|
| - `argparse`   | (built-in)                                                                    |
| - `numpy`      | [Install with `pip install numpy`](https://pypi.org/project/numpy/)           |
| - `matplotlib` | [Install with `pip install matplotlib`](https://pypi.org/project/matplotlib/) |

In order to maximise utility of the script, it is recommended to add
the following to your `.bashrc`, `.profile` or similar

```bash
alias plot="/path/to/plot.py"
```

this allows the script to be invokes anywhere using the `plot` command.
For convenience, typing  `make install` will (try to) add this line to `/home/$USER/.bashrc`.
The remaining instructions will assume this step has been taken.

## Functionality

For the automatically generated syntax guide use `plot -h`.

The script is generally invoked as follows:
```bash
plot <files...> <optional_arguments...>
```

The following optional arguments are available:

| **Argument**          | **Description**                                                              |
|-----------------------|------------------------------------------------------------------------------|
| `-t`  / `--type`      | Plot type (xy, bars, hist), default is xy line plot                          |
| `-s`  / `--stack`     | For each file, stack columns in vertical subplots (xy, bars, hist)           |
| `-j`  / `--join`      | For each file, group columns in one plot (xy)                                |
| `-b`  / `--bins`      | How many equal-width bins to use for plotting the histogram (hist)           |
| `-c`  / `--cols`      | Which columns to plot. Note that this applies to all files (xy, bars, hist)  |
| `-x`  / `--exact`     | Link to a file containing exact/benchmark data. Each column will be plotted! |
| `-ls` / `--linestyle` | Line style for xy plotstyle (solid, dashed, dashdot, dotted, none)           |
| `-m`  / `--marker`    | Marker style for xy plots (".", ",", "o", "s", "x", "+", "^", "v", " ")      |
| `-s`  / `--skip`      | Data point skip interval for large/dense datasets.                           |
