def optimal_storage(program_lengths):
    program_lengths.sort()
    total_time = 0
    current_time = 0
    for length in program_lengths:
        current_time += length
        total_time += current_time
    mean_retrieval_time = total_time / len(program_lengths)
    return mean_retrieval_time
lengths = [10,20,43,7,15,30,25]
mrt = optimal_storage(lengths)
print("Sorted order of programs:", lengths)
print("Minimum Mean Retrieval Time:", mrt)
