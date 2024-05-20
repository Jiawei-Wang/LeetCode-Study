class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        original = s
        no_dash = original.replace("-", "")
        upper = no_dash.upper()
        reverse = upper[::-1]
        chunks = [reverse[i:i+k] for i in range(0, len(reverse), k)]
        print(chunks)
        joined = "-".join(chunks)
        return joined[::-1]

