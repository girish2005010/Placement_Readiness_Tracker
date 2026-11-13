
# Task 3: Runner-up Score

n = int(input())

scores = list(map(int, input().split()))

# Remove duplicate scores
unique_scores = list(set(scores))

# Sort scores in ascending order
unique_scores.sort()

# Print second-highest distinct score
print(unique_scores[-2])
