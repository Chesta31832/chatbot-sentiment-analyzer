from src.sentiment_analyzer import SentimentAnalyzer
from src.conversation_manager import ConversationManager
from src.chatbot import Chatbot
from src.utils import print_sentiment, print_header, print_summary
from colorama import Fore, Style

def main():
    analyzer = SentimentAnalyzer()
    conversation = ConversationManager()
    bot = Chatbot()
    
    print_header("CHATBOT WITH SENTIMENT ANALYSIS")
    print(f"{Fore.CYAN}Type 'quit', 'exit', or 'bye' to end the conversation.{Style.RESET_ALL}\n")
    
    while True:
        # Get user input
        user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}").strip()
        
        if not user_input:
            continue
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print(f"\n{Fore.CYAN}Ending conversation...{Style.RESET_ALL}")
            break
        
        # Analyze sentiment (Tier 2)
        scores, sentiment = analyzer.analyze_with_label(user_input)
        conversation.add_message('user', user_input, scores)
        
        # Display sentiment
        print_sentiment(user_input, sentiment, scores['compound'])
        
        # Generate bot response
        response = bot.get_response(user_input, sentiment)
        conversation.add_message('bot', response)
        
        print(f"{Fore.GREEN}Bot: {Style.RESET_ALL}{response}\n")
    
    # Tier 1: Overall sentiment analysis
    if conversation.get_user_messages():
        overall = conversation.get_overall_sentiment()
        trend = conversation.get_sentiment_trend()
        print_summary(overall, trend)
    else:
        print(f"{Fore.YELLOW}No messages to analyze.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
