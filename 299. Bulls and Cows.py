class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_count = {}

        for i in range(len(secret)):
            if secret[i] in secret_count:
                secret_count[secret[i]] += 1
            else:
                secret_count[secret[i]] = 1

        guess_count = {}

        for i in range(len(guess)):
            if guess[i] in guess_count:
                guess_count[guess[i]] += 1
            else:
                guess_count[guess[i]] = 1

        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret_count[secret[i]] -= 1
                guess_count[guess[i]] -= 1
                if secret_count[secret[i]] == 0:
                    del secret_count[secret[i]]
                if guess_count[guess[i]] == 0:
                    del guess_count[guess[i]]

        cows = 0
        for num in guess_count:
            if num in secret_count:
                cows += min(secret_count[num], guess_count[num])

        return f"{bulls}A{cows}B"
