import unittest
import pandas as pd
from io import StringIO
from data_preprocessor import DataPreprocessor  # Assuming the class is saved in a file named data_preprocessor.py

class TestDataPreprocessor(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.sample_data = """Message
        "Hello, world! ሰላም ልዑል!"
        "This is a test message. ይህ ሙከራ መልእክት ነው።"
        "Another message with emojis 😊 እንደምን አለህ?"
        """
        self.input_path = 'test_input.csv'
        self.output_path = 'test_output.csv'
        
        # Create a sample CSV file
        with open(self.input_path, 'w', encoding='utf-8') as f:
            f.write(self.sample_data)
        
        # Initialize the DataPreprocessor
        self.preprocessor = DataPreprocessor(self.input_path, self.output_path)
    
    def test_load_data(self):
        self.preprocessor.load_data()
        self.assertIsNotNone(self.preprocessor.df)
        self.assertEqual(len(self.preprocessor.df), 3)
    
    def test_remove_emojis(self):
        self.preprocessor.load_data()
        self.preprocessor.df['Message'] = self.preprocessor.df['Message'].apply(self.preprocessor.remove_emojis)
        self.assertNotIn('😊', self.preprocessor.df['Message'].iloc[2])
    
    def test_remove_english_from_amharic(self):
        self.preprocessor.load_data()
        self.preprocessor.df['Cleaned_Message'] = self.preprocessor.df['Message'].apply(self.preprocessor.remove_english_from_amharic)
        self.assertNotIn('Hello', self.preprocessor.df['Cleaned_Message'].iloc[0])
        self.assertNotIn('world', self.preprocessor.df['Cleaned_Message'].iloc[0])
        self.assertIn('ሰላም', self.preprocessor.df['Cleaned_Message'].iloc[0])
    
    def test_preprocess_data(self):
        self.preprocessor.load_data()
        self.preprocessor.preprocess_data()
        self.assertNotIn('😊', self.preprocessor.df['Cleaned_Message'].iloc[2])
        self.assertNotIn('Hello', self.preprocessor.df['Cleaned_Message'].iloc[0])
        self.assertIn('ሰላም', self.preprocessor.df['Cleaned_Message'].iloc[0])
    
    def test_save_data(self):
        self.preprocessor.load_data()
        self.preprocessor.preprocess_data()
        self.preprocessor.save_data()
        saved_df = pd.read_csv(self.output_path)
        self.assertEqual(len(saved_df), 3)
        self.assertIn('ሰላም', saved_df['Cleaned_Message'].iloc[0])

if __name__ == '__main__':
    unittest.main()