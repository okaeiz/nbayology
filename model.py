import os
import pandas as pd
import re

class NBAAnalyzer:
    def __init__(self):
        """Initialize the NBA analysis system and load data."""
        self.player_data = pd.DataFrame()  # Initialize as empty DataFrame
        try:
            self.load_data()
            print("Note: Limited data available. Showing player active status only.")
        except FileNotFoundError as e:
            print(f"Error loading data: {e}")
        except KeyError as e:
            print(f"Missing expected column(s): {e}")

    def load_data(self):
        """Load player data and relevant statistics."""
        # Define the path using the current file’s directory
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'player.csv')
        
        try:
            self.player_data = pd.read_csv(data_path)
            print("Available columns in player data:", self.player_data.columns.tolist())
            
            # Use 'full_name' for player names and 'is_active' for status if available
            if 'full_name' in self.player_data.columns and 'is_active' in self.player_data.columns:
                self.player_name_column = 'full_name'
                self.active_status_column = 'is_active'
            else:
                print("Expected columns ('full_name' and 'is_active') not found.")
                self.player_name_column = None
                self.active_status_column = None
            
            # Filter only the necessary columns
            self.features = [self.player_name_column, self.active_status_column]
            
            # Check if necessary columns are available
            if not all(self.features):
                raise KeyError("Required columns for player name and active status are missing.")
            
            # Drop rows with missing values
            self.player_data = self.player_data[self.features].dropna()
        
        except FileNotFoundError:
            print("The file 'data/player.csv' was not found. Please check the path and try again.")

    def process_question(self, question):
        """Answer questions about player active status."""
        player_name = re.search(r'player (\w+ \w+)', question.lower())
        if player_name:
            return self.analyze_player(player_name.group(1))
        return "Please specify a player in the format: 'player [name]'."

    def analyze_player(self, player_name):
        """Provide active status for a given player."""
        # Ensure the player name and status columns exist before proceeding
        if not self.player_name_column or not self.active_status_column:
            return "Required player columns not available in dataset."

        # Filter player data by name (case-insensitive match)
        player_data = self.player_data[
            self.player_data[self.player_name_column].str.lower() == player_name.lower()
        ]

        if player_data.empty:
            return f"Could not find data for player: {player_name}"

        # Retrieve and format active status
        is_active = player_data[self.active_status_column].values[0]
        status = "active" if is_active else "inactive"
        return f"{player_name.title()} is currently {status} in the league."

def main():
    # Initialize the analyzer
    analyzer = NBAAnalyzer()
    
    print("NBA Analysis System")
    print("Ask questions about players. Type 'quit' to exit.")
    
    while True:
        print("\nWhat would you like to know about an NBA player?")
        question = input().strip()
        
        if question.lower() == 'quit':
            break
        
        try:
            answer = analyzer.process_question(question)
            print("\nAnswer:", answer)
        except Exception as e:
            print(f"Error processing question: {str(e)}")

if __name__ == "__main__":
    main()
