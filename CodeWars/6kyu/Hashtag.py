def generate_hashtag(s):
    if s == "":
        return False
    else:
        
        sentence = []
        words = s.split()
        for word in words:
            sentence.append(word.title())
        compacted_title = "".join(sentence)
        
        final = f"#{compacted_title}"
        if len(final) > 140:
            return False
        else:
            return final

print(generate_hashtag('codewars Is Nice'))