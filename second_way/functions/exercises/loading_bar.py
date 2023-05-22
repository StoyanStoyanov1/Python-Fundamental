def loading_bar(current_percent):
    if current_percent < 100:
        return f"{current_percent}% [{'%' * (current_percent // 10) + '.' * (10 - current_percent // 10)}]" \
               f"\nStill loading..."
    else:
        return f"100% Complete!\n[{'%' * 10}]"


percent = int(input())
print(loading_bar(percent))