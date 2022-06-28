import re

def main():
  file_lists = [
    'python/paddle/fluid/dygraph/layers.py',
    'python/paddle/fluid/dygraph/varbase_patch_methods.py',
    'python/paddle/fluid/dataloader/dataloader_iter.py'
  ]
  # modify python/paddle/fluid/dygraph/layers.py
  with open(file_lists[0], 'r') as f:
    content = f.read()
  content = re.sub(r'(with profiler.*?outputs = self.forward\(\*inputs, \*\*kwargs\))', r'outputs = self.forward(*inputs, **kwargs)', content, flags=re.DOTALL)
  with open(file_lists[0], 'w') as f:
    f.write(content)
  # modify python/paddle/fluid/dygraph/varbase_patch_methods.py
  with open(file_lists[1], 'r') as f:
    content = f.read()
  content = re.sub(r'record_event = .*?Backward\)', r'', content, flags=re.DOTALL)
  content = re.sub(r'record_event.begin\(\)', r'', content, flags=re.DOTALL)
  content = re.sub(r'record_event.end\(\)', r'', content, flags=re.DOTALL)
  with open(file_lists[1], 'w') as f:
    f.write(content)
  
  # modify python/paddle/fluid/dygraph/varbase_patch_methods.py
  with open(file_lists[2], 'r') as f:
    content = f.read()
  content = re.sub(r'trace_event = .*?Dataloader\)', r'', content, flags=re.DOTALL)
  content = re.sub(r'trace_event.begin\(\)', r'', content, flags=re.DOTALL)
  content = re.sub(r'trace_event.end\(\)', r'pass', content, flags=re.DOTALL)
  with open(file_lists[2], 'w') as f:
    f.write(content)
  

if __name__ == '__main__':
  main()