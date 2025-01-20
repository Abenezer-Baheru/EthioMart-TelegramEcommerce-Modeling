# EthioMart Telegram E-commerce Data Processing

## Introduction

EthioMart aims to become the primary hub for all Telegram-based e-commerce activities in Ethiopia. With the increasing popularity of Telegram for business transactions, various independent e-commerce channels have emerged. This decentralization presents challenges for both vendors and customers who need to manage multiple channels for product discovery, order placement, and communication. EthioMart plans to create a centralized platform that consolidates real-time data from multiple e-commerce Telegram channels into one unified channel, providing a seamless experience for customers to explore and interact with multiple vendors in one place.

## Business Objective

The project focuses on fine-tuning LLM’s for Amharic Named Entity Recognition (NER) system that extracts key business entities such as product names, prices, and locations from text, images, and documents shared across these Telegram channels. The extracted data will be used to populate EthioMart's centralized database, making it a comprehensive e-commerce hub.

## Data Overview

The data for this project is collected from five Telegram channels:
- @ZemenExpress
- @MerttEka
- @qnashcom
- @Leyueqa
- @modernshoppingcenter

The data includes text messages, images, and documents shared across these channels.

## Data Structure

The data is structured as follows:
- **Messages**: Text describing various products and entities.
- **Images**: Visual content related to the products.
- **Documents**: Additional information shared in the channels.

## Methodologies Used

- **Data Ingestion**: Custom scraper to collect data from Telegram channels.
- **Data Preprocessing**: Tokenizing, normalizing, and handling Amharic-specific linguistic features.
- **Entity Labeling**: Labeling entities such as product names, prices, and locations in CoNLL format.

## Task 1: Data Ingestion and Data Preprocessing

### Data Ingestion

A custom scraper was implemented to connect to the relevant Telegram channels and collect text, images, and documents in real-time. The scraper was designed to handle the unique structure of Telegram messages and extract relevant metadata such as sender and timestamp.

### Data Preprocessing

The collected text data was preprocessed by tokenizing, normalizing, and handling Amharic-specific linguistic features. The preprocessing steps included:
- **Tokenization**: Splitting text into individual tokens.
- **Normalization**: Converting text to lowercase and removing special characters.
- **Handling Amharic Linguistic Features**: Addressing unique aspects of the Amharic language, such as diacritics and character variations.

The preprocessed data was then structured into a unified format, separating metadata from message content, and stored for further analysis.

## Task 2: Label a Subset of Dataset in CoNLL Format

A subset of the dataset was labeled in the CoNLL format to identify and label entities such as products, prices, and locations in Amharic text. The labeling process involved:
- **Token Labeling**: Each token (word) was labeled on its own line, followed by its entity label.
- **Entity Types**: Entities were labeled as B-Product, I-Product, B-LOC, I-LOC, B-PRICE, I-PRICE, or O (outside any entities).
- **Saving in CoNLL Format**: The labeled data was saved in a plain text file in the CoNLL format, with blank lines separating individual sentences/messages.

## Task 3: Fine Tune NER Model

Objective: Fine-tune a Named Entity Recognition (NER) model to extract key entities (e.g., products, prices, and location) from Amharic Telegram messages.

Steps:
1. Use Google Colab or any other environment with GPU support for faster training.
2. Install necessary libraries.
3. Use the pre-trained XLM-Roberta or bert-tiny-amharic or afroxmlr model.
4. Load the labeled dataset in CoNLL format.
5. Tokenize the data and align the labels with tokens produced by the tokenizer.
6. Set up training arguments.
7. Use Hugging Face's Trainer API to fine-tune the model.
8. Evaluate the fine-tuned model on the validation set.
9. Save the model for future use.

## Task 4: Model Comparison & Selection

Compare different models and select the best-performing one for the entity extraction task.

Steps:
1. Fine-tune multiple models like XLM-Roberta, DistilBERT, or mBERT.
2. Evaluate the fine-tuned model on the validation set.
3. Compare models based on accuracy, speed, and robustness.
4. Select the best-performing model for production.

## Task 5: Model Interpretability

Use model interpretability tools to explain how the NER model identifies entities, ensuring transparency and trust in the system.

Steps:
1. Implement SHAP and LIME to interpret the model’s predictions.
2. Analyze difficult cases where the model might struggle to identify entities correctly.
3. Generate reports on how the model makes decisions and identify areas for improvement.

## Conclusion

The data ingestion and preprocessing tasks were successfully completed, resulting in a structured dataset ready for entity extraction. A subset of the dataset was labeled in the CoNLL format, providing a foundation for fine-tuning the NER model. The next steps involve fine-tuning the NER model and comparing different models for optimal performance.

## Recommendation

For future work, it is recommended to:
- Expand data collection to include more Telegram channels.
- Enhance preprocessing to improve handling of Amharic-specific linguistic features.
- Fine-tune the NER model using the labeled dataset for better entity extraction.

## Reference

- EthioMart Project Documentation
- Telegram API Documentation
- CoNLL Format Guidelines