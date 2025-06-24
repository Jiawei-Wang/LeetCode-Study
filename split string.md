## tiktok phone screen 2025

question: split string into multiple strings, then add index to each string, index also takes up space, ensure each string is at most 80 chars

example:

input: "this is a really long long long long long long long long long long long long long long string"

output: ["this is a really long long long long long long long long long long long long 1/2", "long long string 2/2"


## chat gpt answer

Great question — this is a classic case of **dynamic prefix length affecting the final split**, and many candidates trip over it. Let's break it down and then talk through how to *correctly* solve it.

---

### ✅ The Initial Part You Got Right:

Your idea to:

1. Split the string into words.
2. Build lines by appending words until it exceeds 80 characters.
3. Start a new line when the limit would be exceeded.

This is *exactly right* — it's the foundation of a greedy line-wrapping algorithm and is commonly used in text formatting like word processors.

---

### ❌ The Challenge You Got Stuck On:

The follow-up introduces **indexing each line** with a dynamic-length prefix like `1/5`, `2/5`, ..., which **counts toward the 80-character limit**.

That means:

* The prefix length depends on the **total number of lines** (e.g., `5` vs `100`).
* And it also varies **within the lines**: `1/100` is 5 chars, but `55/100` is 6 chars.

So you can't determine how much space to reserve until you *know* how many lines you’ll need — but you can't determine that unless you *know* how much space to reserve. **It's a circular dependency.**

---

### ✅ Key Insight:

The prefix **changes the effective line length**, and you must **iterate** until the count stabilizes.

---

### ✅ The Correct Algorithm (Outline):

This requires a **multi-pass approach**:

1. **Start by estimating**: Assume the prefix length is, say, 4 characters (`1/5` = 3 digits + 1 space). Use `80 - 4 = 76` as max line length.
2. **Wrap the text** with that assumption.
3. **Count how many lines** you ended up with, call it `n`.
4. Now, **calculate the real maximum prefix length**: for `n = 100`, the longest prefix will be `100/100`, which is 7 characters.
5. Use `80 - max_prefix_length` as the new max line length.
6. **Repeat** the wrapping with this new length.
7. If the number of lines increases, go back to step 4.
8. Once the number of lines **stabilizes**, you're done.

This is basically a **fixpoint iteration**.

---

### ✅ Example Implementation (in Python):

Here’s how you'd write it:

```python
def wrap_with_indices(text, max_len=80):
    words = text.split()
    
    def wrap(words, max_content_len):
        lines = []
        current_line = []
        current_len = 0
        for word in words:
            if current_len + len(word) + (1 if current_line else 0) <= max_content_len:
                current_line.append(word)
                current_len += len(word) + (1 if current_line else 0)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_len = len(word)
        if current_line:
            lines.append(" ".join(current_line))
        return lines

    # Iteratively determine correct max_content_len
    n = 1
    while True:
        prefix_lengths = [len(f"{i+1}/{n}") for i in range(n)]
        max_prefix = max(prefix_lengths) if prefix_lengths else 0
        content_len = max_len - max_prefix - 1  # -1 for space after prefix
        lines = wrap(words, content_len)
        if len(lines) == n:
            break
        n = len(lines)

    # Add prefixes
    result = [f"{i+1}/{n} {line}" for i, line in enumerate(lines)]
    return result
```

---

### 🔍 Key Takeaways for Interviews:

* Admit circular dependencies when you spot them.
* Suggest iterative/refinement algorithms when a value (like total line count) affects the very computation that determines it.
* Use concrete examples (e.g., line prefix length for `5` vs `100`) to show awareness of edge cases.

Would you like me to help you turn this into a concise explanation you can memorize for next time?