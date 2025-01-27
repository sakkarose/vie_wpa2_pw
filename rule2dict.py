import itertools

def generate_wordlist(rule_file):
    wordlist =
    with open(rule_file, 'r') as f:
        for line in f:
            line = line.strip()
            parts = line.split('?d')
            # Generate all possible combinations of digits for the ?d placeholders
            for digits in itertools.product('0123456789', repeat=line.count('?d')):
                word = ''.join([parts[i] + digits[i] for i in range(len(parts) - 1)]) + parts[-1]
                wordlist.append(word)
    return wordlist

if __name__ == '__main__':
    rule_file = 'your_rule_file.rule'
    wordlist = generate_wordlist(rule_file)
    for word in wordlist:
        print(word)
