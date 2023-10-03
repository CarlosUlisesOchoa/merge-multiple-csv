<div align="center">
  <h1>CSV Merger</h1>
  <img src="https://img.shields.io/badge/python-3.6%2B-blue" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" />
</div>

---

## Overview

This Python script merges multiple CSV files by appending rows to a single output CSV file. The script also processes each row to reformat the date and filter the columns before merging.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Example](#example)
- [Contact](#contact)

## Prerequisites

- Python 3.6 or later

## Installation

1. Clone this repository or download the script `csv_merger.py`.
2. Make sure you have Python installed, or download it from [Python's official website](https://www.python.org/).

## Usage

Open a terminal and navigate to the directory containing the script. Then, run the following command:

```bash
python csv_merger.py [OPTIONS]
```

## Options

- `-n, --name [FILENAME]`: Specifies the name of the output file (default: `merged.csv`).
- `-d, --delete`: Deletes input files after merging (default: False).

## Example

Let's say you have a directory `input` with the following CSV files:

- `file1.csv`
- `file2.csv`

After running the command:

```bash
python csv_merger.py -n "final_version" -d
```

An output file named `final_version.csv` will be created in the ouput directory, and the input files will be deleted if the `-d` flag is set.

## Contact

- Website [carlos8a.com](https://carlos8a.com)
- GitHub [@CarlosUlisesOchoa](https://github.com/carlosulisesochoa)
- X [@Carlos8aDev](https://twitter.com/carlos8adev)
