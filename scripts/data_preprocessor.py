# scripts/data_preprocessing.py

import pandas as pd
import re
import emoji

class DataPreprocessor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_path)
        print("Data loaded successfully.")
        print(f"Checking for NaN values in the 'Message' column:")
        nan_count = self.df['Message'].isnull().sum()
        print(f"Number of NaN values in 'Message' column: {nan_count}")

    def remove_emojis(self, text):
        if not isinstance(text, str):
            return text
        return emoji.replace_emoji(text, replace='')

    def remove_english_from_amharic(self, text):
        # Check if the input is a string, otherwise return as is
        if isinstance(text, str):
            # Use regex to remove English letters and common symbols
            amharic_only_text = re.sub(r'[A-Za-z0-9.,!?:;\'\"() {}\-_/]', '', text)
            return amharic_only_text
        return text

    def preprocess_data(self):
        # Remove NaN values
        self.df.dropna(subset=['Message'], inplace=True)
        # Remove emojis
        self.df['Message'] = self.df['Message'].apply(self.remove_emojis)
        # Remove English characters
        self.df['Cleaned_Message'] = self.df['Message'].apply(self.remove_english_from_amharic)
        print("Data preprocessing completed.")

    def save_data(self):
        self.df.to_csv(self.output_path, index=False)
        print(f"Cleaned text saved to {self.output_path}.")