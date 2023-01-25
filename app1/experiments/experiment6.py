import webbrowser

user_term = input("Enter search therm: ").strip().replace(' ', '+')

webbrowser.open(f"https://google.com/search?q={user_term}")