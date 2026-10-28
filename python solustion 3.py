def stock_tracker():
    # Empty portfolio list (Stock data store panna)
    portfolio = {}
    
    print("--- STOCK PORTFOLIO TRACKER ---")
    
    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Summary")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        # 1. Add Stock
        if choice == "1":
            ticker = input("Enter Stock Ticker (e.g., AAPL, TSLA): ").upper().strip()
            try:
                shares = int(input("Enter number of shares: "))
                price = float(input("Enter current price per share ($): "))
                
                if ticker in portfolio:
                    portfolio[ticker]['shares'] += shares
                else:
                    portfolio[ticker] = {'shares': shares, 'price': price}
                print(f"🎉 Success: Added {shares} shares of {ticker}!")
            except ValueError:
                print("❌ Error: Invalid number or price entered.")
                
        # 2. Remove Stock
        elif choice == "2":
            ticker = input("Enter Stock Ticker to remove: ").upper().strip()
            if ticker in portfolio:
                del portfolio[ticker]
                print(f"🔥 Removed {ticker} from portfolio.")
            else:
                print("❌ Stock not found in your portfolio.")
                
        # 3. View Portfolio Summary
        elif choice == "3":
            if not portfolio:
                print("\nYour portfolio is empty!")
            else:
                print("\n--- Portfolio Summary ---")
                total_portfolio_value = 0
                for ticker, data in portfolio.items():
                    stock_value = data['shares'] * data['price']
                    total_portfolio_value += stock_value
                    print(f"• {ticker}: {data['shares']} shares @ ${data['price']:.2f} each = Total Value: ${stock_value:.2f}")
                print(f"\n💰 Total Portfolio Net Worth: ${total_portfolio_value:.2f}")
                print("-------------------------")
                
        # 4. Exit
        elif choice == "4":
            print("Exiting Tracker. Happy Investing! 👋")
            break
        else:
            print("❌ Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    stock_tracker()
