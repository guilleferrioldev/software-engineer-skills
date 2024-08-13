# Bucket sort

# Time complexity = O(n + k) 
# Space complexity = O(n)

"""
Bucket sort is a sorting technique that involves dividing elements into various groups, or buckets. These buckets are formed by uniformly 
distributing the elements. Once the elements are divided into buckets, they can be sorted using any other sorting algorithm. Finally, the
sorted elements are gathered together in an ordered fashion.

How does Bucket Sort work?
- 1. Create an array, where each slot represents a bucket.

- 2. Insert elements into the buckets from the input array based on their range. 

- 3. Sort the elements within each bucket. 

- 4. Gather the elements from each bucket and put them back into the original array. 

- 5. The original array now contains the sorted elements. 
"""

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
