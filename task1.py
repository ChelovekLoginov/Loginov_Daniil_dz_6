result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lin = line.split()
        result.append((lin[0], lin[5].strip('"'), lin[6]))
print(result)
