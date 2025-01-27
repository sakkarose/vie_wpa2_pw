import itertools

def generate_wordlist(rule_file, output_file):
    with open(rule_file, 'r') as f, open(output_file, 'w') as outfile:
        for line in f:
            line = line.strip()
            parts = line.split('?d')
            for digits in itertools.product('0123456789', repeat=line.count('?d')):
                word = ''.join([parts[i] + digits[i] for i in range(len(parts) - 1)]) + parts[-1]
                outfile.write(word + '\n')

if __name__ == '__main__':
    rule_file = 'test.rule'
    output_file = 'test.txt'
    generate_wordlist(rule_file, output_file)
