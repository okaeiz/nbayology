# NBAyology

NBAyology is a Python-based analysis tool designed to provide basic information about NBA players. The tool utilizes a dataset of player information and allows users to query a player's active status. This project is intended for anyone interested in developing a foundational NBA data analysis application.

## Features

- Query active status of NBA players.
- Basic player information lookup using a local dataset (get it from [Kaggle](https://www.kaggle.com/datasets/wyattowalsh/basketball) and extract the `.csv` files into the `data/` directory).

## Project Structure

```plaintext
.
├── data
│   ├── player.csv                # Primary data file containing player information
│   └── other_data_files.csv       # Additional files (e.g., team, game data)
├── model.py                       # Main script with the NBAAnalyzer class
├── .gitignore                     # Specifies files and directories ignored by Git
└── README.md                      # Project documentation
```

## Prerequisites

- Python 3.x
- Required Python packages:
  - pandas
  - scikit-learn

Install packages with:
```bash
pip install pandas scikit-learn
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/okaeiz/nbayology.git
   ```
2. Place the `player.csv` file (and any other relevant data files) in the `data` directory.

3. Ensure `data/` is listed in `.gitignore` to keep data files out of version control.

## Usage

Run the script:
```bash
python3 model.py
```

Then, follow the prompts to query player information. For example, you can check if a player is active by typing:
```plaintext
player Stephen Curry
```

Type `quit` to exit the program.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

