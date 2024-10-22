
def get_text() -> str:
    return """\
# Hello Refinaid Markdown Parser

This is a markdown parser that will help you to summerize your ticket content.

- Author: [Hugo ChunHo Lin](https://github.com/1chooo)
- Date: 2024-04-30
- Version: v0.0.1

## Code Snippet

```python
def hello():
    print("Hello, Refinaid!")

if __name__ == "__main__":
    hello()
```

## Math Formula

$$ f(x) = x^2 + 2x + 1 $$

## Table
| Name | Age |
|------|-----|
| Hugo | 22  |

## Image
![Refinaid](https://avatars.githubusercontent.com/u/148614740?s=200&v=4)

## List
- Item 1
- Item 2

## Quote

> "The only way to do great work is to love what you do." - Steve Jobs

## Task List

- [x] Task 1
- [ ] Task 2

## Reference

- [refinaid/gradio-playground/markdown-parser](https://github.com/refinaid/gradio-playground)
"""


def render_preview(input_markdown_content: str) -> str:
    return input_markdown_content

def get_how_to_material() -> str:
    return """\
## How to Use

### 1. Create `gr.Blocks` Object

With `gr.Blocks` object, you can create a block that contains multiple components.

```python
with gr.Blocks(
    title='Refinaid Markdown Parser',
) as demo:
    
    gr.HTML(
        "<h1 align=center>Refinaid Markdown Parser</h1>"
    )

    ...
    
demo.launch()
```

### 2. Add `gr.Textbox` Component

With `gr.Textbox` object, you can create a textbox that allows users to input text.

```python
input_markdown_content = gr.Textbox(
    interactive=True,
    label="📝 Input your content here (shift + enter to change line)",
    render=True,
    value=...
)
```

### 3. Add `gr.Markdown` Component

With `gr.Markdown` object, you can create a markdown preview that displays the parsed markdown content.

```python
prev_markdown_content = gr.Markdown(
    value=...
)
```

### 4. Define Listener Function

Define a listener function that will be triggered when the input content changes.

```python
def render_preview(input_markdown_content: str) -> str:
    return input_markdown_content
```
"""