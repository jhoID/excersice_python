def response(hey_bob):
    bob_responses = [
        "Sure.",
        "Whoa, chill out!",
        "Calm down, I know what I'm doing!",
        "Fine. Be that way!",
        "Whatever."
    ]

    hey_bob = hey_bob.strip()
    
    if hey_bob.endswith("?") and hey_bob.isupper():
        return bob_responses[2]
    elif hey_bob.endswith("?"):
        return bob_responses[0]
    elif hey_bob.isupper():
        return bob_responses[1]
    elif not hey_bob:
        return bob_responses[3]
    return bob_responses[4]
         

