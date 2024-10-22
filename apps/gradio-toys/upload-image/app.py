import gradio as gr
import numpy as np
from PIL import Image


def show_image(img):
    # Convert To PIL Image
    image = Image.open(img)
    # Convert the image to a NumPy array
    image_array = np.array(image)

    return image_array

def build_upload_image_app():
    with gr.Blocks(title='Refinaid - Upload Image',) as demo:
        gr.HTML(
            "<h1 align=center>Refinaid - Upload Image</h1>"
        )

        gr.Interface(
            fn=show_image,
            inputs=gr.Image(label="Input Image Component", type="filepath"),
            outputs=gr.Image(label="Output Image Component", type="filepath"),
            allow_flagging="never",
            examples=[
                ["./arch.png"],
            ],
        )

        gr.Markdown(
            value="""\
## How to use

### 1. With `gr.Interface`:
```python
gr.Interface(
    fn=...,     # Your function here
    inputs=gr.Image(label="Input Image Component", type="filepath"),
    outputs=gr.Image(label="Output Image Component", type="filepath"),
    allow_flagging="never",
    examples=[
        ...,    # Add your examples here
    ],
)
```

### 2. Define your function:

```python
def show_image(img):
    # Convert To PIL Image
    image = Image.open(img)
    # Convert the image to a NumPy array
    image_array = np.array(image)

    return image_array
```

### 3. Launch the app and upload an image to see the output.
"""
        )

    return demo


if __name__ == "__main__":
    build_upload_image_app().launch()
