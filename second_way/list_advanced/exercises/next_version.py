def next_version(current_version):
    return str(int(current_version) + 1)


version = "".join([digit for digit in input().split(".")])
print(*next_version(version), sep=".")
