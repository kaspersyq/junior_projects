# Email slicer

email = input('Enter your email address: ').strip()
username = email[:email.index('@')]
domain_name = email[email.index('@') + 1:]

if domain_name == 'gmail.com':
    print(f"Hey {username}, I see your email is registered with Google. That's cool!.")
else:
    print(f"Hey {username}, looks like you've got your own custom setup at {domain_name}. Impressive!")
