def solution(text, ending):
    text = str(text)
    if text.endwith(ending):
        return True
    else:
        return False

solution("paction", "io")