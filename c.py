import math

def isqrt(x):
    """Returns the integer square root of x."""
    l, r = 0, 1
    while r * r <= x:
        r *= 2
    while l < r:
        m = (l + r) // 2
        if m * m <= x:
            l = m + 1
        else:
            r = m
    return l - 1

def solve(k):
    """Solves the problem for a given k and returns the output string."""
    results = []
    if k < 700:
        for m in range(1, int(1e9) + 1):
            if (6 * m * m) % k != 0:
                continue
            s = 36 * (k + 1) ** 2 - 24 * (2 * k * (k + 1) + k + 1 - ((6 * m * m) // k))
            if s < 0:
                continue
            r = isqrt(s)
            if r * r == s:
                ans = (-6 * (k + 1) + r) // 12
                if ans > 0:
                    results.append(f"{{{k},{ans + 1}}},\n")
                    return results
    else:
        for start in [int(9e8), int(1e8), int(2e8), int(3e8), int(4e8), int(5e8), int(6e8), int(7e8), int(8e8), int(9e8)]:
            end = start + int(1e8)
            for m in range(start, end + 1):
                if (6 * m * m) % k != 0:
                    continue
                s = 36 * (k + 1) ** 2 - 24 * (2 * k * (k + 1) + k + 1 - ((6 * m * m) // k))
                if s < 0:
                    continue
                r = isqrt(s)
                if r * r == s:
                    ans = (-6 * (k + 1) + r) // 12
                    if ans > 0:
                        results.append(f"{{{k},{ans + 1}}},\n")
                        return results
    return results

# Run the solver for k = 1 to 2500 and store the results
output_data = []
for i in range(1, 2501):
    output_data.extend(solve(i))

# Save the results to a file
output_file_path = "/mnt/data/output.txt"
with open(output_file_path, "w") as f:
    f.writelines(output_data)

# Return the file path for download
output_file_path
