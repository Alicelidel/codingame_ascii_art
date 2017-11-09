island = [
      [2, 5, 8, 9, 2],
      [10, 1, 1, 7, 7],
      [7, 1, 1, 6, 7],
      [2, 12,  5, 8, 2]
  ]


new_island = island.copy()


new_island[0] = '111'

print('-----------------------')
for elem in island:
    print(*elem)
print('-----------------------')
for elem in new_island:
    print(*elem)