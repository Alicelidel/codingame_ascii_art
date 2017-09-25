n = int(input())
lines = sorted(
    [tuple(
        map(int, input().split())
    ) for _ in range(n)], key=lambda x: x[1]
)
print(lines)
points = []

while lines:
    points.append(lines[0][1])
    print(points)
    lines = [(b, e) for b, e in lines if b > points[-1]]
    print(lines)

print(len(points))
print(*points)