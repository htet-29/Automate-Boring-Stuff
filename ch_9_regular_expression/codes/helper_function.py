def safe_search(pattern, text, group_no=0, default="None"):
    match = pattern.search(text)
    return match.group(group_no) if match else default
