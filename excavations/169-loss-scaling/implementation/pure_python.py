"""Excavation 169: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def scale_loss(loss,scale): return loss*scale
def unscale_gradient(gradient,scale): return gradient/scale
def demo():
    visible=scale_loss(.000001,1000); recovered=unscale_gradient(visible,1000)
    assert abs(recovered-.000001)<1e-15
    return {"scaled":visible,"recovered":recovered}

if __name__ == "__main__":
    print(demo())
