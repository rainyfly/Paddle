import os

filenames = [
  "paddle/fluid/platform/profiler/trace_event.h",
  "paddle/fluid/platform/profiler.cc",
  "paddle/fluid/platform/profiler/event_tracing.h",
  "paddle/fluid/framework/data_layout_transform.cc",
   "paddle/fluid/framework/operator.cc",
  "paddle/fluid/imperative/prepared_operator.cc",
  "paddle/fluid/operators/marker_op.cc",
  "paddle/fluid/operators/marker_op.cu",
  "paddle/fluid/operators/elementwise/mkldnn/elementwise_add_mkldnn_op.cc",
  "paddle/fluid/operators/elementwise/mkldnn/elementwise_sub_mkldnn_op.cc",
 "paddle/fluid/operators/mkldnn/conv_mkldnn_op.cc",
 "paddle/fluid/operators/mkldnn/conv_transpose_mkldnn_op.cc",
"paddle/fluid/operators/mkldnn/fc_mkldnn_op.cc",
"paddle/fluid/operators/mkldnn/mul_mkldnn_op.cc",
"paddle/fluid/platform/mkldnn_helper.h",
"paddle/fluid/platform/mkldnn_reuse.h"
]

def main():
  src_dir = "/ssd5/chenjian26/Frameworks/Paddle"
  dst_dir = "/ssd5/chenjian26/PaddleForPr/Paddle"
  for filename in filenames:
    with open(os.path.join(src_dir, filename)) as srcfp:
      with open(os.path.join(dst_dir, filename), 'w') as dstfp:
        contents = srcfp.readlines()
        for content in contents:
          dstfp.write(content)
  
  

if __name__ == "__main__":
  main()

