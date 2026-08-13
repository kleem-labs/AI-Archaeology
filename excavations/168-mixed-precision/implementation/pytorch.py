"""Excavation 168: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

fp32=torch.ones(1_000_000,dtype=torch.float32); fp16=fp32.half()
assert fp16.element_size()==fp32.element_size()//2; print({"fp32_bytes":fp32.nelement()*fp32.element_size(),"fp16_bytes":fp16.nelement()*fp16.element_size()})
