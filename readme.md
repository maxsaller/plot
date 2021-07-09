## General purpose plotting script

| **Contents**                       |
| ---------------------------------- |
| 1. [Installation](#installation)   |
| 2. [Functionality](#functionality) |

#### Installation
The script is written in `python3` and requires the following libraries

|                |                                                                               |
| -------------- | ----------------------------------------------------------------------------- |
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

#### Functionality

For the automatically generated syntax guide use `plot -h`.

The script is generally invoked as follows:

`plot` `<plottype>` `<files...>` `<optional_arguments...>`

The plottypes available are

|        |              |
| ------ | ------------ |
| `xy`   | XY line plot |
| `bar`  | Bar chart    |
| `hist` | Histogram    |


The following optional arguments are also available

|                  |                                                                             |
| ---------------- | --------------------------------------------------------------------------- |
| `-s` / `--stack` | For each file, stack columns in vertical subplots (xy, bars, hist)          |
| `-j` / `--join`  | For each file, group columns in one plot (xy)                               |
| `-b` / `--bins`  | How many equal-width bins to use for plotting the histogram (hist)          |
| `-c` / `--cols`  | Which columns to plot. Note that this applies to all files (xy, bars, hist) |
