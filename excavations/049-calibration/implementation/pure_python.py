def calibration_gap(confidences,correct): return abs(sum(confidences)/len(confidences)-sum(correct)/len(correct))
