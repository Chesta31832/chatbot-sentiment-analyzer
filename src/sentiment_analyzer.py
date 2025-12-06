from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Dict, Tuple

class SentimentAnalyzer:
    """Analyzes sentiment of text using VADER"""
    
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        
    def analyze(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment of given text
        
        Returns:
            dict: Contains 'neg', 'neu', 'pos', 'compound' scores
        """
        return self.analyzer.polarity_scores(text)
    
    def get_sentiment_label(self, compound_score: float) -> str:
        """
        Convert compound score to readable label
        
        Args:
            compound_score: Score between -1 and 1
            
        Returns:
            str: 'Positive', 'Negative', or 'Neutral'
        """
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"
    
    def analyze_with_label(self, text: str) -> Tuple[Dict[str, float], str]:
        """
        Analyze text and return scores with label
        
        Returns:
            tuple: (scores_dict, sentiment_label)
        """
        scores = self.analyze(text)
        label = self.get_sentiment_label(scores['compound'])
        return scores, label
