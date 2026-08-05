def convolve(signal,kernel): return [sum(signal[i+j]*kernel[j] for j in range(len(kernel))) for i in range(len(signal)-len(kernel)+1)]
