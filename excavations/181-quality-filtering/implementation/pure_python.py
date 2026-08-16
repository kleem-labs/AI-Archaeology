"""Excavation 181: dependency-free evidence for this chapter.
"""

def structural_signals(text):
    lines=[x.strip() for x in text.splitlines() if x.strip()]; repeated=1-len(set(lines))/max(1,len(lines)); sentences=sum(x.endswith((".","?","!")) for x in lines)
    return {"repeated_line_share":repeated,"sentence_count":sentences}
def demo():
    spam=structural_signals("MENU\nMENU\nMENU"); report=structural_signals("Tiger seen.\nTrack direction recorded."); assert spam["repeated_line_share"]>report["repeated_line_share"]
    return {"spam":spam,"report":report,"decision":"audit thresholds by source"}

if __name__ == "__main__":
    print(demo())
